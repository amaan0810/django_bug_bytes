# Request flow from browser to Django (Nginx · Gunicorn · Uvicorn · WSGI · ASGI)

*Updated edition: all the original content is kept, plus a new **Rule vs program** section, a **Gunicorn + Uvicorn workers** section, worked examples, and a few fixes.*

**Read in this order:** Section 0 (big picture), then Section 4 (rule vs program), then Section 9 (Gunicorn + Uvicorn), then the Q&A in Section 15.

## 0. The big picture (memorise this first)

```
Browser
  │ ① types https://mysite.com/books/
  ▼
DNS  → converts mysite.com → server IP (e.g. 13.233.10.5)
  │
  ▼
Nginx  (port 80/443, faces the internet)
  │ ② HTTPS, static files, buffering, load balancing
  │    → forwards dynamic requests with proxy_pass
  ▼
Gunicorn / Uvicorn  (port 8000, internal only)
  │ ③ runs Python, keeps Django loaded in workers
  ▼
WSGI / ASGI  (the "plug" / interface standard)
  │ ④ calls `application` in wsgi.py / asgi.py
  ▼
Django
  │ ⑤ Middleware (top → bottom)
  │ ⑥ URL resolver → view
  │ ⑦ View → ORM → Database
  │ ⑧ Middleware (bottom → top)
  ▼
Response travels back: Django → Gunicorn → Nginx → Browser
```

**Four layers, four jobs:**

| Layer | Job in one line |
| --- | --- |
| **Nginx** | Front door: HTTPS, static files, forwards everything else |
| **Gunicorn / Uvicorn** | Program that runs your Python code in workers |
| **WSGI / ASGI** | Rulebook that says how the server talks to Django |
| **Django** | Your actual app: middleware, URLs, views, ORM |

**Restaurant analogy (use it in interviews):**

| Real world | Web |
| --- | --- |
| Address lookup | **DNS** |
| Security guard + receptionist | **Nginx** |
| Manager with waiters | **Gunicorn** |
| Fast multitasking waiter | **Uvicorn** |
| Rules for passing orders to the kitchen | **WSGI / ASGI** |
| Kitchen | **Django** |
| Storeroom | **Database** |

**One-liner:** *"Nginx receives the request and forwards it to Gunicorn or Uvicorn, which run Django through the WSGI or ASGI interface; Django passes it through middleware, the URL router and the view, and the response goes back the same way."*

---

## 1. Browser & DNS

- The browser sends an **HTTP request**: method (`GET`/`POST`), URL, headers, cookies, body.

  ```
  GET /books/ HTTP/1.1
  Host: mysite.com
  Cookie: sessionid=abc123
  ```
- **DNS** finds the IP address for the domain. The browser then connects to that IP on port **443** (HTTPS) or **80** (HTTP).
- **HTTPS** = HTTP + TLS encryption. The TLS handshake happens with **Nginx**, not Django.

---

## 2. Nginx: web server + reverse proxy

**What:** a fast web server written in C. It's the **first thing every request hits**. **Reverse proxy:** receives requests *on behalf of* the backend and forwards them. Users never reach Gunicorn directly.

### Why we need it (Gunicorn alone isn't enough)

| Job | Simple reason |
| --- | --- |
| **HTTPS/SSL** | Nginx handles certificates and encryption |
| **Static/media files** | Serves CSS/JS/images straight from disk, with no Python involved |
| **Buffering slow clients** ⭐ | Waits for a slow upload to finish, *then* gives it to Gunicorn, so the worker isn't stuck |
| **Load balancing** | Spreads traffic across many Gunicorn servers |
| **Security** | Hides the app server, limits upload size, rate-limits |
| **Many connections** | Event-driven, so it handles thousands of connections cheaply |

### Examples

- `GET /static/style.css` → Nginx returns the file from disk → **Django is never touched**
- `GET /books/` → Nginx → `proxy_pass` → Gunicorn → Django → back

### Minimal config

```nginx
upstream django_app {
    server 127.0.0.1:8000;          # Gunicorn/Uvicorn (in Docker: web:8000)
}
server {
    listen 80;
    server_name mysite.com;
    client_max_body_size 10M;

    location /static/ { alias /app/staticfiles/; }   # collectstatic folder
    location /media/  { alias /app/media/; }

    location /ws/ {                                  # WebSockets (ASGI only)
        proxy_pass http://django_app;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location / {
        proxy_pass http://django_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

The `X-Forwarded-*` headers pass the **real user IP and http/https** to Django. Without them, Django sees every request as coming from `127.0.0.1` over plain `http`.

**Matching Django settings:**

```python
ALLOWED_HOSTS = ["mysite.com"]
STATIC_ROOT = BASE_DIR / "staticfiles"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ["https://mysite.com"]
```

**Errors to know:** **502 Bad Gateway** = Nginx can't reach Gunicorn (it's down, or on the wrong port). **504 Gateway Timeout** = Gunicorn took too long to answer.

---

## 3. Application server: why not `runserver`?

`python manage.py runserver` is for **development only**. It's slow, has no worker management, and isn't hardened for security. In production, an **application server** runs Django: it starts Python, loads your app once, and handles requests in workers.

|  | Nginx | Gunicorn / Uvicorn |
| --- | --- | --- |
| Type | Web server / proxy | Application server |
| Runs Python? | ❌ | ✅ |
| Faces the internet? | ✅ (80/443) | ❌ (internal 8000) |
| Talks to Django via | HTTP → app server | **WSGI / ASGI** |

---

## 4. Rule vs program ⭐ (the most confusing part)

People mix these up because the names look alike. Split them into two groups:

|  | What it is | Do you install it? |
| --- | --- | --- |
| **WSGI / ASGI** | **Rules / specification** for how a server calls a Python app | ❌ Nothing to install, it's just a standard |
| **Gunicorn / Uvicorn** | **Programs (servers)** that follow those rules | ✅ `pip install gunicorn` / `pip install uvicorn` |

**Analogy 1: USB-C is the rule, a charger is the product.**

- **WSGI** = the old port (sync, simple, older)
- **ASGI** = the new port (async, can do more: WebSockets, streaming)
- **Gunicorn** = a plug that fits the **WSGI** port
- **Uvicorn** = a plug that fits the **ASGI** port
- **Django has both ports:** `wsgi.py` and `asgi.py`. You choose which one to plug into.

**Analogy 2: the cricket rulebook.** The Laws of Cricket (WSGI/ASGI) don't play the match. Players (Gunicorn/Uvicorn) play by those laws. Any team that follows the laws can play any other team, which is why you can swap servers without rewriting Django.

**Which one is the "default"?**

- **Gunicorn** is the usual default pick for a **WSGI** setup (normal Django sites and REST APIs).
- **Uvicorn** is the usual default pick for an **ASGI** setup (async views, WebSockets).

**Why having a rule is useful:** any WSGI server can run any WSGI app. Gunicorn, uWSGI and mod\_wsgi can all run Django or Flask. Any ASGI server can run any ASGI app: Uvicorn, Daphne and Hypercorn can all run Django, FastAPI or Starlette.

**Quick mapping:**

| Rule | Server programs that follow it | Django file | Example frameworks |
| --- | --- | --- | --- |
| **WSGI** (sync) | Gunicorn, uWSGI, mod\_wsgi | `wsgi.py` | Django, Flask |
| **ASGI** (async) | Uvicorn, Daphne, Hypercorn | `asgi.py` | Django, FastAPI, Starlette |

---

## 5. WSGI: the sync interface

**What:** **W**eb **S**erver **G**ateway **I**nterface (PEP 3333). It's the **standard "plug"** between a Python server and a Python app. Any WSGI server works with any WSGI app.

**How it works:** the server calls one function per request and **waits** until it returns.

```python
# what WSGI looks like underneath (simplified)
def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"Hello"]
```

Django gives you this ready-made in `wsgi.py`:

```python
application = get_wsgi_application()
```

**Key facts:**

- **Synchronous**: one request occupies one worker/thread until it finishes.
- **HTTP only**: no WebSockets, no long-lived connections.
- Servers: **Gunicorn**, uWSGI, mod\_wsgi.

---

## 6. Gunicorn: the WSGI server

**What:** "Green Unicorn", a Python WSGI server built on a **master + workers** model.

```
Gunicorn master  (manages workers, restarts them if they crash)
 ├── worker 1 → Django copy → 1 request at a time
 ├── worker 2 → Django copy
 └── worker 3 → Django copy
```

```bash
gunicorn demo.wsgi:application --workers 3 --bind 0.0.0.0:8000
#        └─ file demo/wsgi.py  └─ variable inside it
```

- **Workers formula:** `(2 × CPU cores) + 1`. This is the starting point for **sync** workers only. Tune it by load testing.
- `--threads 4` → each worker can also handle 4 requests using threads
- `--timeout 30` → kills a worker that's stuck longer than 30s

**Example:** 3 workers, and 10 users arrive at once → 3 are served and 7 wait in the queue. If each view waits 2s on an external API, the workers sit idle while blocked. This is the weakness of sync.

---

## 7. ASGI: the async interface

**What:** **A**synchronous **S**erver **G**ateway **I**nterface, the successor to WSGI.

**How it works:** the app is an `async` function. While one request waits (network, DB), the **event loop** runs the others.

```python
# what ASGI looks like underneath (simplified)
async def application(scope, receive, send):
    await send({"type": "http.response.start", "status": 200, "headers": []})
    await send({"type": "http.response.body", "body": b"Hello"})
```

Django gives you this in `asgi.py`:

```python
application = get_asgi_application()
```

**Key facts:**

- **Asynchronous**: one worker can juggle many requests.
- Supports **HTTP + WebSockets + streaming/SSE + long-polling**.
- Servers: **Uvicorn**, Daphne, Hypercorn.

---

## 8. Uvicorn: the ASGI server

**What:** a fast ASGI server built on an event loop (uvloop).

```bash
uvicorn demo.asgi:application --host 0.0.0.0 --port 8000 --workers 2
```

**Daphne** = the ASGI server from the Django Channels team, often used for WebSockets.

**Example:** 1 Uvicorn worker, 100 users, each request waiting 1s on an API. With **async views and async libraries** they're all handled concurrently in about 1s, instead of queuing. With normal sync views Django pushes them to a thread pool, so you don't get this gain.

---

## 9. Gunicorn + Uvicorn workers ⭐ (common at companies)

The production combo: Gunicorn's process management + Uvicorn's async.

```bash
gunicorn demo.asgi:application -k uvicorn.workers.UvicornWorker --workers 3
```

- `-k` = **worker type**. Gunicorn lets you swap its default sync workers for Uvicorn's async workers.
- **Gunicorn master** = the manager (process management, restarts, timeouts, reloads)
- **Uvicorn workers** = do the real ASGI / async work
- Result: **Gunicorn's mature process management + Uvicorn's async**
- Restaurant: the experienced manager hires fast multitasking waiters

**Three commands side by side:**

| Command | Manager | Workers | Rule |
| --- | --- | --- | --- |
| `gunicorn demo.wsgi:application` | Gunicorn | Gunicorn sync | WSGI |
| `uvicorn demo.asgi:application` | Uvicorn | Uvicorn | ASGI |
| `gunicorn demo.asgi:application -k uvicorn.workers.UvicornWorker` | Gunicorn | Uvicorn | ASGI |

**Rule of thumb:** use the `wsgi` file with sync workers and the `asgi` file with Uvicorn workers. Never mix them (a `wsgi` file with a Uvicorn worker will not work).

**Which command should I run?**

| Situation | Run this |
| --- | --- |
| Local development | `python manage.py runserver` |
| Normal Django site or REST API in production | `gunicorn demo.wsgi:application` |
| Async views or WebSockets in production | `gunicorn demo.asgi:application -k uvicorn.workers.UvicornWorker` |
| Quick async setup, small project | `uvicorn demo.asgi:application --workers 2` |

**Gotchas:**

- For Uvicorn workers, a common starting point is **about 1 worker per CPU core** (each worker's event loop already handles many requests). The `2 × cores + 1` formula is for sync workers.
- Newer Uvicorn versions moved the Gunicorn worker class into a separate package (`uvicorn-worker`, used as `-k uvicorn_worker.UvicornWorker`). The old `uvicorn.workers.UvicornWorker` path still appears in many tutorials and may show a deprecation warning. Know both names for interviews.

---

## 10. Sync vs async: what actually changes in your code

```python
# SYNC view: blocks while waiting
import requests
def dashboard(request):
    a = requests.get(url1)   # 1s
    b = requests.get(url2)   # 1s
    c = requests.get(url3)   # 1s
    return JsonResponse(...)  # total ≈ 3s
```

```python
# ASYNC view: waits without blocking
import asyncio, httpx
async def dashboard(request):
    async with httpx.AsyncClient() as client:
        a, b, c = await asyncio.gather(
            client.get(url1), client.get(url2), client.get(url3)
        )
    return JsonResponse(...)  # total ≈ 1s
```

- `async def` = a function that can pause.
- `await` = *"I'm waiting, so serve someone else meanwhile."*
- **Only helps with waiting (I/O)**, not with CPU-heavy work.
- Needs **async libraries**: `httpx`/`aiohttp`, not `requests`; `asyncio.sleep`, not `time.sleep`.
- Async ORM: `await Book.objects.aget(pk=1)`, `async for b in Book.objects.all()`. Behind the scenes Django still runs the database call in a thread, so it keeps the event loop free but isn't fully async at the DB driver level.

### Worked example: 6 requests, each waiting 2s on an external API (all arrive at t=0)

**Before: sync, Gunicorn, 2 workers**

| Time | Worker 1 | Worker 2 | Queue |
| --- | --- | --- | --- |
| 0s - 2s | Request 1 | Request 2 | R3, R4, R5, R6 |
| 2s - 4s | Request 3 | Request 4 | R5, R6 |
| 4s - 6s | Request 5 | Request 6 | empty |

Total = **6s**. Requests 5 and 6 wait 4s before they even start.

**After: async view, Uvicorn, 1 worker**

| Time | What the event loop is doing |
| --- | --- |
| t = 0s | Starts R1 to R6, hits `await` on each, nothing blocks |
| t ≈ 2s | All 6 API replies arrive, all 6 finish |

Total ≈ **2s**, with fewer workers. If the work were CPU-heavy (say, resizing images) instead of waiting, async would give **no gain**.

### Mixing rules (asked a lot)

| Situation | What happens |
| --- | --- |
| `async def` view on **WSGI** | Works, but each request gets its own event loop → **no benefit** |
| Normal `def` view on **ASGI** | Works; Django runs it in a thread (`sync_to_async`) |
| Sync-only middleware on ASGI | Works, but adds context-switch overhead |
| `sync_to_async()` / `async_to_sync()` | Bridges between the two worlds (from `asgiref`) |

---

## 11. Inside Django (after WSGI/ASGI hands over)

```
HttpRequest created
  → Middleware (request phase, top → bottom):
      SecurityMiddleware → SessionMiddleware → CommonMiddleware
      → CsrfViewMiddleware → AuthenticationMiddleware (sets request.user) → ...
  → URL resolver (ROOT_URLCONF → urlpatterns) → matching view
  → View: ORM → DB → template / serializer
  → Middleware (response phase, bottom → top)
HttpResponse → back to Gunicorn/Uvicorn → Nginx → Browser
```

- **SessionMiddleware must come before AuthenticationMiddleware**, because auth reads the session.
- If a middleware returns a response early, the view never runs.

---

## 12. Real-time & background work (where ASGI fits)

| Need | Use |
| --- | --- |
| Normal pages / REST API | **WSGI + Gunicorn** |
| Many slow external API calls in one request | **ASGI** + async views |
| Chat, live notifications (WebSockets) | **ASGI + Django Channels** (+ Redis channel layer) |
| Sending emails, reports, image processing | **Celery** / a task queue. The user shouldn't wait at all |

**Async ≠ Celery.** Async = handle the waiting efficiently *during* the request. Celery = do the work *after* the response.

---

## 13. Production stack (draw this)

```
            ┌────────────── Docker / server ──────────────┐
User ──► Nginx ──► Gunicorn (WSGI) or Uvicorn (ASGI) ──► Django ──► PostgreSQL
           │                                           │
           └─ /static/, /media/ (or S3/CDN)            ├──► Redis (cache, broker)
                                                       └──► Celery workers
```

In **Docker Compose**, Nginx points to `web:8000`, because the service name is the hostname.

---

## 14. Master comparison table

|  | **Nginx** | **Gunicorn** | **Uvicorn** | **WSGI** | **ASGI** |
| --- | --- | --- | --- | --- | --- |
| What is it | Web server / reverse proxy | WSGI app server | ASGI app server | Sync interface standard | Async interface standard |
| Rule or program? | Program | Program | Program | **Rule** | **Rule** |
| Runs Python | ❌ | ✅ | ✅ | — (a spec) | — (a spec) |
| Concurrency | Event-driven | Processes/threads | Event loop | 1 request per worker | Many per worker |
| WebSockets | Proxies them | ❌ | ✅ | ❌ | ✅ |
| Django file | — | `wsgi.py` | `asgi.py` | `wsgi.py` | `asgi.py` |
| Analogy | Guard / receptionist | Manager + waiters | Multitasking waiter | Old port | New port |

---

## 15. 🔥 Rapid-fire interview Q&A

1. **What happens when you type a URL?** DNS → TLS with Nginx → proxy to Gunicorn → WSGI → Django middleware → URL → view → DB → response back.
2. **What is a reverse proxy?** A server in front of your backend that receives requests and forwards them. It acts for the *server*. (A forward proxy acts for the *client*.)
3. **Why Nginx + Gunicorn, not Gunicorn alone?** HTTPS, static files, buffering slow clients, load balancing, security.
4. **WSGI vs ASGI?** Sync and HTTP-only vs async, with HTTP + WebSockets + streaming.
5. **Is WSGI a server or a standard?** A standard (a rule). Gunicorn is the program that follows it.
6. **Gunicorn vs Uvicorn?** WSGI with processes/threads vs ASGI with an event loop.
7. **Why `-k uvicorn.workers.UvicornWorker`?** `-k` swaps Gunicorn's sync workers for Uvicorn's async workers, so you get Gunicorn's process management with ASGI support.
8. **Can Uvicorn alone run Django?** Yes, point it at `asgi.py`. Gunicorn on top adds more mature worker supervision.
9. **Why not `runserver` in production?** Dev-only, slow, not secure, no worker management.
10. **How many Gunicorn workers?** `2 × cores + 1` for sync workers. For Uvicorn workers, roughly 1 per core, then load test.
11. **Async view on WSGI?** Works, but gives no benefit.
12. **Sync view on ASGI?** Works; it runs in a thread pool.
13. **Is async faster for CPU work?** No. It only helps with I/O waiting.
14. **`requests` inside `async def`?** It blocks the event loop. Use `httpx`.
15. **WebSockets in Django?** ASGI server + Django Channels + Redis, with Nginx upgrade headers.
16. **Who serves static files?** Nginx / CDN / Whitenoise, never Django in production. Run `collectstatic` first.
17. **502 vs 504?** 502 = app server unreachable. 504 = app server too slow.
18. **Why the `X-Forwarded-For` / `X-Forwarded-Proto` headers?** To give Django the real client IP and protocol behind the proxy.
19. **Async vs Celery?** Async = efficient waiting during a request. Celery = background work after the response.

---

## 16. 30-second summary answer

> "When a user hits our site, DNS resolves the domain and the request reaches **Nginx**, our reverse proxy. It terminates HTTPS, serves static files directly, buffers slow clients, and forwards dynamic requests to the app server. For a normal Django app that's **Gunicorn**, a **WSGI** server running Django in multiple sync worker processes. If we need async views or WebSockets, we use **Uvicorn** (often as Gunicorn workers), which speaks **ASGI** and uses an event loop to handle many concurrent connections. WSGI and ASGI are not programs, just the interface standards between the server and Django, exposed by `wsgi.py` and `asgi.py`. Django then processes the request through middleware, the URL router and the view, talks to the database, and the response flows back the same way."

---

## Last-minute cheat sheet

- **Nginx** = front door (HTTPS, static, proxy)
- **WSGI / ASGI** = rules, nothing to install
- **Gunicorn** = program for WSGI. **Uvicorn** = program for ASGI.
- **Gunicorn + `-k` Uvicorn worker** = Gunicorn manages, Uvicorn does the async work
- **wsgi.py** pairs with sync workers. **asgi.py** pairs with Uvicorn workers.
- **Async** helps with waiting (I/O), not CPU work. **Celery** is for work after the response.