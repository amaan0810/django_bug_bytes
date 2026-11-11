# Django Interview Prep — Step-by-Step Guide (BugBytes edition)

> **Who this is for:** a developer with ~2 years of experience who wants to restart Django from scratch and be interview-ready.
> **Main source:** [BugBytes YouTube channel](https://www.youtube.com/@bugbytes3923) — every video link below is from that channel.
> **Gap fillers:** where BugBytes has no dedicated video (custom User model, request lifecycle, async views, security), the official docs are linked instead.

---

## How to use this guide

1. Go **phase by phase**, in order. Each phase has:
   - 📺 **Watch** — the videos, in the order to watch them
   - 🧠 **Know for interviews** — concepts you must be able to *explain out loud*
   - 🛠 **Build** — a small hands-on task (do it — interviewers can tell who has actually coded it)
2. Code along in this repo (one folder per phase is fine).
3. At the end of every phase, answer the questions in the **[Interview Question Bank](#interview-question-bank)** for that topic *without looking*.
4. Suggested pace: **~1–1.5 hrs/day → ~9 weeks**. Phases marked ⭐ are the most asked in interviews.

| Week | Phases                                                                    |
| ---- | ------------------------------------------------------------------------- |
| 1    | 0 – Setup & project structure, 1 – Django fundamentals                  |
| 2    | 2 – Request lifecycle & middleware ⭐, 3 – Models & ORM basics ⭐       |
| 3    | 3 – ORM advanced ⭐ (optimization, F/Q, transactions)                    |
| 4    | 4 – Auth & permissions ⭐                                                |
| 5    | 5 – Django REST Framework ⭐                                             |
| 6    | 6 – Performance & caching, 7 – ASGI vs WSGI, async, background tasks ⭐ |
| 7    | 8 – Testing, 9 – Architecture, settings & deployment                    |
| 8    | 9.5 – Docker for Django ⭐                                               |
| 9    | 10 – Modern Django (5.x / 6.x), revision + mock interviews               |

---

## ⚡ 2-Week Fast Track (for 2 yrs experience, Phase 0 + Phase 1 tutorial done)

> ~2–3 hrs/day. Video numbers = the numbered lists in each phase below.
> ✅ **Must** = interviewers ask this, don't skip. ⏭ **Skip** = rarely asked / niche. It's listed in [Revisit later](#-revisit-later-after-the-interview).

| Day | Topic                                     | ✅ Must watch / do                                                                            | ⏭ Skip for now            |
| --- | ----------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------- |
| 0   | Phase 1 primers                           | Django URLs (named/reverse/namespaces) · Context processors · AJAX & CSRF tokens · Model validators / ModelForms · Media files · Whitenoise | Path converters · DRY templates · Custom template filters · json_script · Restricting file types · Admin actions |
| 1   | Phase 2: Middleware & signals             | 1, 4, 7 + middleware docs + memorise the request-lifecycle diagram                            | 2, 3, 5, 6, 8, 9           |
| 2   | Phase 3a/3b: ORM basics & optimization    | 4, 6, 8, **9 ⭐⭐⭐**, 10                                                               | 1, 2, 3, 5, 7, 11, 12, 13  |
| 3   | Phase 3c/3d: Expressions & transactions   | 14, 15, 16, 21, 22 (+19 if time)                                                              | 17, 18, 20                 |
| 4   | Phase 3e: Model design + practice         | 24, 25, 30 + build the N+1 fix and "buy product" (`atomic` + `select_for_update` + `F`) | 23, 26–29, 31, 32         |
| 5   | Phase 4: Auth                             | 1 + **read Custom User docs + Security docs** + build a custom User (email login)       | 2–9                       |
| 6   | Phase 5a/5b: DRF serializers & views      | 1, 2, 3, 5, 6, 8, 9, 10, 11                                                                   | 4, 7, 12                   |
| 7   | Phase 5b/5c: ViewSets & auth              | 13, 14, 15, 16, **18, 19 (JWT)**                                                        | 17, 20, 21                 |
| 8   | Phase 5d/5e: Filtering, pagination, tests | 22, 23, 25, 26, 32                                                                            | 24, 27, 28, 29, 31         |
| 9   | Phase 6: Caching                          | 3, 4 + cache docs + practise "how do you debug a slow endpoint"                               | 2, 5, 7                    |
| 10  | Phase 7: ASGI/WSGI, async, Celery ⭐      | 1, 3, **4**, 7 + **async docs** + memorise the ASGI vs WSGI table                 | 2, 5, 6, 8, 9, 10          |
| 11  | Phase 8: Testing                          | 1, 4, 6                                                                                       | 2, 3, 5, 7–10             |
| 12  | Phase 9.5: Docker ⭐                      | 1, 2 + Dockerise your DRF project (web + Postgres + Redis + Celery)                           | 3, 4, 5, multi-stage build |
| 13  | Phase 9 + 10                              | Phase 9: 1, 6 · Phase 10: 2, 5 (fast playback)                                               | everything else in 9 & 10  |
| 14  | Revision                                  | All 75 questions in the bank out loud + 4 "Tell me about…" stories + 1 mock interview        | —                         |

**Build ONE project, not one per phase:** a "Products & Orders" DRF API you keep adding to. It gets a custom User (Day 5), ORM optimization and transactions (Days 2–4), JWT, ViewSets and pagination (Days 6–8), Redis cache (Day 9), Celery with `on_commit` (Day 10), tests (Day 11), and Docker (Day 12). Push it to GitHub. That's your portfolio piece.

**Never skip, even if you're short on time:** N+1 / `select_related` / `prefetch_related` · F & Q · transactions · custom User · CSRF/XSS/SQL injection · DRF permissions & JWT · ASGI vs WSGI · Celery + `on_commit` · request lifecycle · Dockerfile & compose basics.

### 🔁 Revisit later (after the interview)
- [ ] Phase 1 primers: path converters, DRY templates, custom template filters, json_script, restricting file types, admin actions

- [ ] Phase 2: videos 2, 3, 5, 6, 8, 9
- [ ] Phase 3: videos 1, 2, 3, 5, 7, 11, 12, 13, 17, 18, 19, 20, 23, 26–29, 31, 32
- [ ] Phase 4: videos 2–9 (guardian, allauth, social auth, MFA, sesame, hijack)
- [ ] Phase 5: videos 4, 7, 12, 17, 20, 21, 24, 27, 28, 29, 31
- [ ] Phase 6: videos 2, 5, 7
- [ ] Phase 7: videos 2, 5, 6, 8, 9, 10
- [ ] Phase 8: videos 2, 3, 5, 7, 8, 9, 10
- [ ] Phase 9: videos 2, 3, 4, 5, 7, 8, 9, 10
- [ ] Phase 9.5: videos 3, 4, 5 + multi-stage build
- [ ] Phase 10: videos 1, 3, 4, 6, 7
- [ ] Optional tracks (django-ninja, other primers)

---

## Master playlist list

| Playlist                                                                                                            | Videos | Use in this guide          |
| ------------------------------------------------------------------------------------------------------------------- | ------ | -------------------------- |
| [Django Introduction – Official Tutorial](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQaapZunsYsll5MphTRL1qB) | 14     | Phase 1                    |
| [Django ORM Deep Dive](https://www.youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2)                     | 35     | Phase 3 ⭐                 |
| [Django REST Framework – API Development](https://www.youtube.com/playlist?list=PL-2EBeDYMIbSXhV8FMC1hVD32Fi6e4l2u) | 32     | Phase 5 ⭐                 |
| [Django Primers](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQIu4aMZYqM6_w1ihIKWIql)                           | 45     | Pick-and-mix across phases |
| [django-allauth – Deep Dive](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQqZZoo5Dj8YAkPnZeJfcZS)              | 9      | Phase 4                    |
| [Django Media Files](https://www.youtube.com/playlist?list=PL-2EBeDYMIbQpw0N1BmAi9-acwhpxEfoo)                       | 3      | Phase 1 / 9                |
| [Django-Ninja – API library](https://www.youtube.com/playlist?list=PL-2EBeDYMIbS7bXwkMOS_ajeTdNRnhApX)              | 6      | Optional (DRF alternative) |

---

## Phase 0 — Setup & project structure

📺 **Watch**

1. [Django 101 – High-level overview of Django project components](https://www.youtube.com/watch?v=deMO0wIwJis) ⭐ *start here*
2. [Django Introduction – Installation &amp; Python Virtual Environments](https://www.youtube.com/watch?v=l9mROGx4SU4)
3. [uv and Django – Managing Django projects &amp; dependencies with uv](https://www.youtube.com/watch?v=hm-rDxSMzSw)
4. [Environment-based Settings | django-environ | local/production/testing](https://www.youtube.com/watch?v=O4IIBOGFyWI) ⭐
5. [Using startproject and startapp templates](https://www.youtube.com/watch?v=_s6g6yP0ahY)
6. [cookiecutter-django – production-ready project layout](https://www.youtube.com/watch?v=aZybyNIgv0M)
7. [ruff – linting &amp; formatting (Django example)](https://www.youtube.com/watch?v=yLYaQq6KbKs)

🧠 **Know for interviews**

- **Project vs app**: the *project* is the configuration (settings, root URLconf, `wsgi.py`/`asgi.py`); an *app* is a reusable unit of functionality (models, views, urls, admin) listed in `INSTALLED_APPS`.
- What each generated file does: `manage.py`, `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`, `apps.py`, `migrations/`.
- A typical **production structure**:
  ```
  project/
  ├── config/                # the "project" package
  │   ├── settings/
  │   │   ├── base.py
  │   │   ├── local.py
  │   │   └── production.py
  │   ├── urls.py
  │   ├── asgi.py
  │   └── wsgi.py
  ├── apps/
  │   ├── users/             # custom User model lives here
  │   └── orders/
  │       ├── models.py
  │       ├── services.py    # business logic (thin views)
  │       ├── selectors.py   # read/query logic
  │       ├── api/ (serializers.py, views.py, urls.py)
  │       └── tests/
  ├── requirements / pyproject.toml
  └── manage.py
  ```
- Secrets (`SECRET_KEY`, DB passwords) come from **environment variables**, never from git. `DEBUG=False` + `ALLOWED_HOSTS` in production.

🛠 **Build:** create a project with `config/` + split settings (base/local/production) driven by `.env`.

---

## Phase 1 — Django fundamentals (views, URLs, templates, forms)

📺 **Watch — the official-tutorial playlist, in order**

1. [Views, URLs and Management Commands](https://www.youtube.com/watch?v=u3j4LCorz7Y)
2. [Models, Databases and Migrations](https://www.youtube.com/watch?v=dLoMsDlLZ1M)
3. [Models API for Querying Databases](https://www.youtube.com/watch?v=a6ow5dWM3ms)
4. [Django Admin Introduction](https://www.youtube.com/watch?v=nnIcYya4E2Y)
5. [Capturing and using URL parameters](https://www.youtube.com/watch?v=-SYcZSyiw-I)
6. [HTML Templates with Django](https://www.youtube.com/watch?v=P_XvXet_tfs)
7. [render() – a Django shortcut](https://www.youtube.com/watch?v=1uVDoW_3wfo)
8. [get_object_or_404() for cleaner views](https://www.youtube.com/watch?v=_X4mmb06xug)
9. [Detail pages &amp; the {% url %} tag](https://www.youtube.com/watch?v=cufXXrLNWHM)
10. [HTML Forms, POST requests &amp; CSRF tokens](https://www.youtube.com/watch?v=MYPHIBIzgJU) ⭐
11. [Processing POST requests &amp; saving to the DB](https://www.youtube.com/watch?v=aL19KebkRjQ)
12. [Generic &amp; Class-Based Views](https://www.youtube.com/watch?v=DDIP-icVpA8) ⭐
13. [Add context to CBVs – get_context_data()](https://www.youtube.com/watch?v=_QKfS2lBhvA)

📺 **Then these primers**

- [Django URLs – named URLs, reversing, namespaces, get_absolute_url()](https://www.youtube.com/watch?v=obRENgwHS7A)
- [Path converters – built-in &amp; custom](https://www.youtube.com/watch?v=hrfqwj7JCAc)
- [DRY templates, partials, passing context to child templates](https://www.youtube.com/watch?v=DJwytraqwoE)
- [Context processors – global template context](https://www.youtube.com/watch?v=sGU-CCz1LjE)
- [Custom template filters](https://www.youtube.com/watch?v=g2WkvFSVce8)
- [Passing backend data to JavaScript – json_script](https://www.youtube.com/watch?v=h39eMGWmEV4)
- [AJAX requests &amp; CSRF tokens](https://www.youtube.com/watch?v=lc1sOvRaFpg)
- [Model field validators / custom validators / ModelForms](https://www.youtube.com/watch?v=1x0Zdukpjrs)
- [Media files – handling user uploads](https://www.youtube.com/watch?v=lKyH_ZGtvwM)
- [Restricting uploadable file types with validators](https://www.youtube.com/watch?v=UcUm82jWeKc)
- [Whitenoise for static assets](https://www.youtube.com/watch?v=QZTk8txo6x0)
- [Admin actions – writing custom actions](https://www.youtube.com/watch?v=ilHNmOjfxfc)

🧠 **Know for interviews**

- **MVT** (Model–View–Template) vs MVC: Django's *view* plays the role of the MVC *controller*; the *template* is the MVC *view*.
- **FBV vs CBV**: FBVs are explicit and simple; CBVs give reuse through inheritance and **mixins** (`LoginRequiredMixin`, `ListView`, `CreateView`…). Know the CBV flow: `as_view()` → `dispatch()` → `get()`/`post()`.
- `render()` vs `HttpResponse` vs `redirect()`; `reverse()` vs `{% url %}`.
- **Form** vs **ModelForm**; `is_valid()` → `cleaned_data`; `clean_<field>()` and `clean()`.
- **Static vs media** files: static = your assets (CSS/JS) gathered by `collectstatic`; media = user uploads (`MEDIA_ROOT`, `FileField`). In production, neither is served by Django itself (use Whitenoise / Nginx / S3).
- **CSRF**: why POST forms need `{% csrf_token %}`, and how AJAX sends the `X-CSRFToken` header.

🛠 **Build:** a polls/blog app with list, detail, create (ModelForm), edit, and delete, first as FBVs and then rewritten as CBVs.

---

## Phase 2 — Request/response lifecycle, middleware, signals ⭐

📺 **Watch**

1. [Writing Django middleware (with tests!) | HTMX &amp; IP-blacklist middleware](https://www.youtube.com/watch?v=--ddZc39wVQ) ⭐
2. [Writing maintenance-mode middleware (with tests)](https://www.youtube.com/watch?v=TTEEr4N-lKw)
3. [Django 5.1 – LoginRequiredMiddleware &amp; {% querystring %}](https://www.youtube.com/watch?v=F_cqPmaE8vI)
4. [Django sessions – session data and cookies](https://www.youtube.com/watch?v=ethWelG8FCQ)
5. [&#34;Remember me&#34; with sessions &amp; AuthenticationForm](https://www.youtube.com/watch?v=6wRQ75awrNQ)
6. [Marking the session as &#34;modified&#34;](https://www.youtube.com/watch?v=V3hhk5QpxLQ)
7. [Django signals – introduction](https://www.youtube.com/watch?v=8p4M-7VXhAU) ⭐
8. [django-lifecycle – model hooks (signals alternative)](https://www.youtube.com/watch?v=sNdopNFOEB8)
9. [django-after-response – run code after sending the response](https://www.youtube.com/watch?v=uYF-H5TmNTk)

📖 **Docs (no dedicated BugBytes video):**
[Middleware](https://docs.djangoproject.com/en/stable/topics/http/middleware/) ·
[Request &amp; response objects](https://docs.djangoproject.com/en/stable/ref/request-response/) ·
[Signals](https://docs.djangoproject.com/en/stable/topics/signals/)

🧠 **Know for interviews: the request lifecycle (draw this on a whiteboard)**

```
Client
  │  HTTP request
  ▼
Web server (Nginx) ──► App server (Gunicorn = WSGI | Uvicorn/Daphne = ASGI)
  │
  ▼
WSGIHandler / ASGIHandler  → builds HttpRequest
  │
  ▼
Middleware (request phase, TOP → BOTTOM of MIDDLEWARE list)
  │
  ▼
URL resolver (ROOT_URLCONF → urlpatterns) → finds the view
  │
  ▼
process_view() hooks → VIEW runs (ORM → DB, templates, etc.)
  │
  ▼
Middleware (response phase, BOTTOM → TOP)
  │
  ▼
HttpResponse → back to the server → client
```

- **Middleware** = a callable wrapping `get_response`. Hooks: `__init__(get_response)` (runs once at startup), `__call__(request)`, `process_view`, `process_exception`, `process_template_response`.
- **Order matters**: e.g. `SessionMiddleware` must come before `AuthenticationMiddleware` (auth reads the session to set `request.user`). If a middleware returns a response early, the layers below it never run.
- Common built-ins: `SecurityMiddleware`, `SessionMiddleware`, `CommonMiddleware`, `CsrfViewMiddleware`, `AuthenticationMiddleware`, `MessageMiddleware`, `XFrameOptionsMiddleware`.
- **Signals** (`pre_save`, `post_save`, `pre_delete`, `m2m_changed`, `request_started`…). Pitfalls: they hide coupling, they're **synchronous** (they run inside the request), and **`bulk_create()`, `update()`, and `QuerySet.delete()` don't call `save()`**, so `pre_save`/`post_save` never fire. (Bulk delete still sends `pre_delete`/`post_delete`.) Prefer explicit service functions when you can.

🛠 **Build:** a request-timing middleware that adds an `X-Request-Duration` header, plus a test for it. Add a `post_save` signal that creates a `Profile` for each new user.

---

## Phase 3 — Models & ORM ⭐⭐ (the most-asked area)

Watch the **[ORM Deep Dive playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbTT7ri4pNEBu9VoVSAkOvd2)** in order. The groups below say what each video is for.

### 3a. Basics

1. [Intro to databases &amp; SQL](https://www.youtube.com/watch?v=EsBqIZmR2Uc)
2. [Models, migrations and admin integration](https://www.youtube.com/watch?v=t7diJPGxCGo)
3. [Querying &amp; creating records / foreign keys](https://www.youtube.com/watch?v=46au1MxtOJE)
4. [Updating &amp; deleting QuerySets / on_delete behaviour](https://www.youtube.com/watch?v=cN4zjbcM2kk) ⭐
5. [Filtering, lookups, ordering, slicing](https://www.youtube.com/watch?v=84BBAGEu064)
6. [ManyToManyField and through models](https://www.youtube.com/watch?v=MECLUHlgF2w) ⭐
7. [Model properties &amp; methods / @property / get_absolute_url()](https://www.youtube.com/watch?v=PgHaH8tGdWw)
8. [The problem with User.objects.create()](https://www.youtube.com/watch?v=c6iCXYuZ3WU) ⭐ (use `create_user()`, which hashes the password)

### 3b. Query optimization ⭐⭐⭐

9. [select_related &amp; prefetch_related / django-debug-toolbar / the N+1 problem](https://www.youtube.com/watch?v=a3dTy8RO5Ho) ⭐⭐⭐
10. [Database indexes – performance optimisation](https://www.youtube.com/watch?v=JW-EDDz5tXo) ⭐
11. [&#34;Explaining&#34; QuerySets with django-silk](https://www.youtube.com/watch?v=Rr-BSQ4AGZY)
12. [Index expressions – PostgreSQL + TruncDate](https://www.youtube.com/watch?v=Mh3MgiibqGg)
13. [in_bulk() explained](https://www.youtube.com/watch?v=ddvvty7NhsM)

### 3c. Expressions & aggregation ⭐

14. [Aggregation &amp; annotation / values() &amp; values_list()](https://www.youtube.com/watch?v=LEsmHKZLsBI) ⭐
15. [F expressions – database-level operations](https://www.youtube.com/watch?v=NDOYWw0tDgw) ⭐
16. [Q objects – OR / NOT, regex lookups](https://www.youtube.com/watch?v=Pc96-4_gqJ4) ⭐
17. [Coalesce &amp; NULL handling](https://www.youtube.com/watch?v=i5t5ONN1zY4)
18. [Conditional expressions – Case() &amp; When()](https://www.youtube.com/watch?v=beVGYjMSRRk)
19. [Subquery, OuterRef and Exists](https://www.youtube.com/watch?v=QvaScsn6S6E)
20. [Set operations on QuerySets (union/intersection/difference)](https://www.youtube.com/watch?v=tRAegLQtzIM)

### 3d. Transactions & concurrency ⭐

21. [Database transactions / atomic()](https://www.youtube.com/watch?v=L8k8Ukw1P6U) ⭐
22. [select_for_update() – locking rows](https://www.youtube.com/watch?v=xBl-qiAFrzg) ⭐

### 3e. Model design

23. [Database constraints – Unique &amp; Check](https://www.youtube.com/watch?v=lRTTLqha58I)
24. [Model inheritance – abstract &amp; multi-table](https://www.youtube.com/watch?v=KSPRODsdfo4) ⭐
25. [Proxy models](https://www.youtube.com/watch?v=KF2p-LQjZZ4) ⭐
26. [Content types framework](https://www.youtube.com/watch?v=S85MOayADz8)
27. [Generic foreign keys](https://www.youtube.com/watch?v=Wt4_7ZAE8dI)
28. [Custom on_delete functions](https://www.youtube.com/watch?v=KW-uu76708E)
29. [GeneratedField (Django 5)](https://www.youtube.com/watch?v=iTsp-QnlHAQ)
30. [Custom managers (in the Finance Tracker course)](https://www.youtube.com/watch?v=n47VFgqG-E8) ⭐
31. [Multiple databases / inspectdb / database routers](https://www.youtube.com/watch?v=GwqZozhZ1MY)
32. [Graph models – generate ER diagrams](https://www.youtube.com/watch?v=qzrE7cfc_3Q)

📖 **Docs:** [Database access optimization](https://docs.djangoproject.com/en/stable/topics/db/optimization/) ⭐ ·
[When QuerySets are evaluated](https://docs.djangoproject.com/en/stable/ref/models/querysets/#when-querysets-are-evaluated) ·
[Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/)

🧠 **Know for interviews**

- **QuerySets are lazy.** They hit the DB only when evaluated: iteration, `list()`, `len()`, `bool()`, slicing with a step, `repr()`. An evaluated QuerySet caches its results.
- **N+1 problem**: you loop over 100 books and touch `book.author.name` → 1 query for the books + 100 for the authors.
  - `select_related()` → a SQL **JOIN**, for **forward FK / OneToOne**.
  - `prefetch_related()` → a **second query**, joined in Python, for **M2M and reverse FK**. Use `Prefetch()` to filter or customise it.
- `get()` (exactly one row, otherwise `DoesNotExist` / `MultipleObjectsReturned`) vs `filter()` (a QuerySet) vs `first()`.
- `exists()` vs `count()` vs `len()`; `only()` / `defer()`; `values()` / `values_list(flat=True)`; `iterator()` for huge tables.
- `aggregate()` (returns one dict) vs `annotate()` (adds a value per row).
- **F()** for race-free updates: `Product.objects.filter(pk=1).update(stock=F("stock") - 1)`.
- **Q()** for OR / NOT: `filter(Q(a=1) | ~Q(b=2))`.
- `save()` vs `QuerySet.update()` vs `bulk_create()` / `bulk_update()`: the bulk methods skip `save()` and `pre_save`/`post_save` signals.
- **on_delete**: `CASCADE`, `PROTECT`, `RESTRICT`, `SET_NULL` (needs `null=True`), `SET_DEFAULT`, `SET()`, `DO_NOTHING`.
- `null=True` (DB column allows NULL) vs `blank=True` (form validation allows empty).
- **Inheritance**: *abstract* (no table, fields are copied into children), *multi-table* (a table per model plus an implicit OneToOne JOIN, which costs performance), *proxy* (same table, different Python behaviour or manager).
- **Manager vs QuerySet**: put reusable filters on a custom `QuerySet` and expose them with `QuerySet.as_manager()` so they're chainable.
- **Transactions**: `transaction.atomic()` (nestable through savepoints), `ATOMIC_REQUESTS`, and `transaction.on_commit()` (send emails / Celery tasks only after the commit). `select_for_update()` must run **inside** `atomic()`.
- **Migrations**: `makemigrations` / `migrate` / `showmigrations` / `sqlmigrate`, data migrations with `RunPython`, `--fake`, squashing, and resolving merge conflicts.
- **Indexes**: `db_index=True`, `Meta.indexes`, composite indexes, and when an index *doesn't* help (low-cardinality columns, write-heavy tables).

🛠 **Build:** an `Author` / `Book` / `Publisher` / `Store` schema. Seed 10k rows with a management command. Write a view that makes 100+ queries, then get it down to 2–3 with `select_related` / `prefetch_related`, proving it with debug-toolbar. Implement "buy product" with `atomic()` + `select_for_update()` + `F()`.

---

## Phase 4 — Authentication & permissions ⭐

📺 **Watch**

1. [Django permissions system – users, groups and permissions (deep dive)](https://www.youtube.com/watch?v=IF_ZpCiZKkw) ⭐
2. [django-guardian – object-level permissions](https://www.youtube.com/watch?v=uekncTEw6LI)
3. [django-allauth – intro &amp; installation](https://www.youtube.com/watch?v=nmj7ThneEnc)
4. [django-allauth – accounts app deep dive](https://www.youtube.com/watch?v=5a_I_HaKSTw)
5. [Customizing django-allauth – custom signup forms](https://www.youtube.com/watch?v=99qZ-y8Nhx0)
6. [Social auth with Google](https://www.youtube.com/watch?v=D1B_BkGHbqs) · [Login with GitHub – OAuth 2.0](https://www.youtube.com/watch?v=zu_lcO7Yueo)
7. [MFA in Django apps with django-allauth](https://www.youtube.com/watch?v=PCxNNRm4kOU)
8. [django-sesame – magic-link login](https://www.youtube.com/watch?v=g6FrzrCERqI)
9. [Django-Hijack – impersonating users via the admin](https://www.youtube.com/watch?v=S28cNW5QFtQ)

📖 **Docs (must read — no BugBytes video):** [Custom User model](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model) ⭐⭐ ·
[Security in Django](https://docs.djangoproject.com/en/stable/topics/security/) ⭐ ·
[Deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)

🧠 **Know for interviews**

- **Always start a project with a custom User model** (`AUTH_USER_MODEL = "users.User"`). Swapping it mid-project is painful.
  - `AbstractUser` = keep every default field and add your own (most common).
  - `AbstractBaseUser + PermissionsMixin` = full control (e.g. email-only login); you must write a custom `UserManager`.
  - Reference the user as `settings.AUTH_USER_MODEL` in FKs and `get_user_model()` in code, never by importing `User` directly.
- **Authentication** (who are you?) vs **authorization** (what may you do?).
- Permissions: `user.has_perm("app.change_book")`, groups, `@login_required`, `@permission_required`, `LoginRequiredMixin`, `PermissionRequiredMixin`. Model-level (built-in) vs object-level (django-guardian / custom).
- Password hashing (PBKDF2 by default, Argon2 optional). Never store raw passwords; use `set_password()` / `create_user()`.
- Session auth: the session ID lives in a cookie and the data on the server (DB, cache, or signed cookie backend).
- **Security built-ins**: CSRF middleware, template auto-escaping (XSS), parameterised ORM queries (SQL injection: never build SQL with f-strings), `X-Frame-Options` (clickjacking), `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, HSTS, and `python manage.py check --deploy`.

🛠 **Build:** a custom `User` (email login) + a `Profile`, registration/login/logout, an "editors" group with `change_article` permission, and a view that only the article's author can edit.

---

## Phase 5 — Django REST Framework ⭐⭐

Watch the **[DRF playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbSXhV8FMC1hVD32Fi6e4l2u)** in order:

### 5a. Serializers

1. [Setup and models](https://www.youtube.com/watch?v=6AEvlNgRPNc)
2. [Serializers &amp; Response objects | Browsable API](https://www.youtube.com/watch?v=BMym71Dwox0) ⭐
3. [Nested serializers, SerializerMethodField, relations](https://www.youtube.com/watch?v=KfSYadIFHgY) ⭐
4. [Serializer subclasses &amp; aggregated API data](https://www.youtube.com/watch?v=_xbI0-mjtw4)
5. [ModelSerializer fields – best practices](https://www.youtube.com/watch?v=NgUARZNOuTY)
6. [Creating nested objects – overriding create()](https://www.youtube.com/watch?v=CAq7AKAT7Q0) ⭐
7. [Updating nested objects – overriding update()](https://www.youtube.com/watch?v=QtkES6O_ed4)

### 5b. Views: APIView → Generics → ViewSets ⭐

8. [Generic views – ListAPIView &amp; RetrieveAPIView](https://www.youtube.com/watch?v=vExjSChWPWg)
9. [Dynamic filtering – overriding get_queryset()](https://www.youtube.com/watch?v=3Gi-w4Swge8)
10. [APIView class](https://www.youtube.com/watch?v=TVFCU0w65Ak) ⭐
11. [Creating data – ListCreateAPIView &amp; generic-view internals](https://www.youtube.com/watch?v=Jh85U1nhMh8) ⭐
12. [Updating &amp; deleting data](https://www.youtube.com/watch?v=08gHVFPFuBU)
13. [ViewSets &amp; routers](https://www.youtube.com/watch?v=4MrB4IvW6Ow) ⭐
14. [ViewSet actions, filtering &amp; permissions](https://www.youtube.com/watch?v=rekvVrjUMjg)

### 5c. Auth & permissions ⭐

15. [Permissions &amp; testing permissions](https://www.youtube.com/watch?v=rx5IV_4Iuog)
16. [Customising permissions in generic views](https://www.youtube.com/watch?v=mlQZ1i8rUKQ)
17. [ViewSet permissions – admin vs normal user](https://www.youtube.com/watch?v=KmYYg1qJKNQ)
18. [JWT auth with djangorestframework-simplejwt](https://www.youtube.com/watch?v=Xp0-Yy5ow5k) ⭐
19. [Refresh tokens &amp; JWT auth](https://www.youtube.com/watch?v=H3OY36wa7Cs) ⭐
20. [djoser – JWT &amp; token auth](https://www.youtube.com/watch?v=QO8UyXWNg-k)
21. [React &amp; Django auth with djoser](https://www.youtube.com/watch?v=DIvWhrVHtn4)

### 5d. Filtering, pagination, throttling, docs

22. [django-filter &amp; DRF filtering](https://www.youtube.com/watch?v=NDFgTGTI8zg)
23. [SearchFilter &amp; OrderingFilter](https://www.youtube.com/watch?v=LCYqDsl1WYI)
24. [Writing filter backends](https://www.youtube.com/watch?v=u4S71cO5QhI)
25. [Pagination – PageNumber &amp; LimitOffset](https://www.youtube.com/watch?v=sTyMe2R9mzk) ⭐
26. [API throttling](https://www.youtube.com/watch?v=95ndK3P9YLI) ⭐
27. [drf-spectacular – API documentation (OpenAPI)](https://www.youtube.com/watch?v=E3LUvsPWLwM)
28. [File uploads with DRF](https://www.youtube.com/watch?v=05YafeAFITA)

### 5e. Production concerns

29. [django-silk – profiling DRF](https://www.youtube.com/watch?v=OG8alXR4bEs)
30. [Caching with Redis](https://www.youtube.com/watch?v=5W2Yff00H8s) ⭐
31. [Vary headers &amp; caching behaviour](https://www.youtube.com/watch?v=iUn8go-XZNw)
32. [Testing APIs](https://www.youtube.com/watch?v=sRluxnmZ-H8) ⭐
33. [Celery tasks with DRF](https://www.youtube.com/watch?v=E6HPMk0bKPY) ⭐

📺 **Bonus:** [Django API overview – DRF vs django-ninja vs django-bolt vs django-modern-rest](https://www.youtube.com/watch?v=AFYNEGtsjKI) (good for "why DRF?" questions)

🧠 **Know for interviews**

- `Serializer` vs `ModelSerializer`; validation order: field validators → `validate_<field>()` → `validate()`. `to_representation()` / `to_internal_value()`. `read_only_fields`, `write_only=True`, `source=`, `SerializerMethodField`.
- **Nested writes aren't automatic.** You must override `create()` / `update()`.
- **View hierarchy:** `APIView` → `GenericAPIView` (+ mixins) → concrete generics (`ListCreateAPIView`…) → `ViewSet` / `ModelViewSet` + **routers**. Know when you'd drop down to `APIView`.
- **DRF request flow inside a view:** `initial()` → *authentication* → *permissions* → *throttling* → handler → response. Authentication is lazy: it actually runs on the first access to `request.user`.
- **Permissions:** `has_permission()` (every request) vs `has_object_permission()` (only when `get_object()` is called, so **not** on list views!).
- **Auth options:** Session (browser, same-domain), Token (DB-stored, simple), **JWT** (stateless; short-lived *access* + long-lived *refresh* token; hard to revoke, so use a blacklist or short TTLs).
- **Pagination:** PageNumber, LimitOffset, **Cursor** (stable for large or real-time feeds; no "jump to page N").
- **Throttling:** `AnonRateThrottle`, `UserRateThrottle`, `ScopedRateThrottle`; needs a shared cache (Redis) across multiple servers.
- Optimise serializers with `select_related` / `prefetch_related` **in `get_queryset()`**, because nested serializers are a classic N+1 source.
- API versioning (URL / header / namespace) and idempotency of PUT vs PATCH vs POST.

🛠 **Build:** a "Products & Orders" API with JWT auth, a `ModelViewSet` + router, filtering/search/ordering, pagination, an `IsOwnerOrReadOnly` permission, nested order-items creation, throttling, Swagger docs via drf-spectacular, and tests.

---

## Phase 6 — Performance & caching

📺 **Watch**

1. [select_related / prefetch_related / N+1 (re-watch!)](https://www.youtube.com/watch?v=a3dTy8RO5Ho)
2. [Query optimization with django-debug-toolbar (HTMX series)](https://www.youtube.com/watch?v=ndbxeRbtn7w)
3. [@cache_page() decorator for view caching](https://www.youtube.com/watch?v=725QM0BKBi8)
4. [Caching with Redis](https://www.youtube.com/watch?v=5W2Yff00H8s)
5. [Vary headers](https://www.youtube.com/watch?v=iUn8go-XZNw)
6. [Database indexes](https://www.youtube.com/watch?v=JW-EDDz5tXo)
7. [django-control-room – Celery/Redis/cache panels in admin](https://www.youtube.com/watch?v=MNYKfQUiDdE)

📖 **Docs:** [Django&#39;s cache framework](https://docs.djangoproject.com/en/stable/topics/cache/)

🧠 **Know for interviews**

- **Caching levels:** per-site (middleware), per-view (`@cache_page`), template fragment (`{% cache %}`), low-level (`cache.get` / `set` / `get_or_set`). Backends: Redis, Memcached, DB, local memory (per process, so not shared!).
- **Cache invalidation strategies:** TTL, delete on `save()` / signal, versioned keys.
- **How you'd debug a slow endpoint:** measure first (debug-toolbar / silk / APM) → count queries → fix N+1 → add indexes (`EXPLAIN`) → cache → move slow work to background tasks.
- Connection pooling / `CONN_MAX_AGE`; Django 5.1+ supports native PostgreSQL connection pooling.

---

## Phase 7 — ASGI vs WSGI, async Django, real-time & background tasks ⭐

📺 **Watch**

1. [StreamingHttpResponse – streaming responses with ASGI &amp; WSGI](https://www.youtube.com/watch?v=n0J6VoiK6VM) ⭐ *(the best ASGI vs WSGI demo on the channel)*
2. [Django &amp; HTMX with Server-Sent Events (SSE)](https://www.youtube.com/watch?v=9qwCc0FgPRg)
3. [WebSocket notifications with django-channels](https://www.youtube.com/watch?v=FcVwDEcu6K0) ⭐
4. [Celery tasks with DRF](https://www.youtube.com/watch?v=E6HPMk0bKPY) ⭐
5. [django-q2 – background tasks (Celery alternative)](https://www.youtube.com/watch?v=0hRDCrxfHug) · [django-q2 with Redis &amp; Docker](https://www.youtube.com/watch?v=wjSFMK_IZS8)
6. [Procrastinate – PostgreSQL task queue](https://www.youtube.com/watch?v=6puV9y7K0z8)
7. [Django 6 released – Tasks framework, CSP and more](https://www.youtube.com/watch?v=Ek4aweB1GlQ) ⭐
8. [django-tasks – DatabaseBackend and the new API](https://www.youtube.com/watch?v=BJVUCyh-dto)
9. [django-crontab – scheduled functions](https://www.youtube.com/watch?v=6eoS9CFOmFw)
10. [Python concurrent.futures – ThreadPool vs ProcessPool](https://www.youtube.com/watch?v=nRVT4olRbMA) (background on concurrency)

📖 **Docs (must read):** [Asynchronous support in Django](https://docs.djangoproject.com/en/stable/topics/async/) ⭐ ·
[Deploying with ASGI](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/) ·
[Deploying with WSGI](https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/) ·
[Django Channels](https://channels.readthedocs.io/) ·
[Django Tasks framework (6.0+)](https://docs.djangoproject.com/en/stable/topics/tasks/)

🧠 **Know for interviews: ASGI vs WSGI**

|            | **WSGI**                                                       | **ASGI**                                                                |
| ---------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Full name  | Web Server Gateway Interface (PEP 3333)                              | Asynchronous Server Gateway Interface                                         |
| Model      | Synchronous: one request ties up one worker/thread until it finishes | Asynchronous: one event loop can juggle many connections while waiting on I/O |
| Protocols  | HTTP request/response only                                           | HTTP, **WebSockets**, long-polling, SSE, HTTP/2                         |
| Entry file | `wsgi.py` → `application`                                       | `asgi.py` → `application`                                                |
| Servers    | Gunicorn, uWSGI, mod_wsgi                                            | Uvicorn, Daphne, Hypercorn (or Gunicorn with Uvicorn workers)                 |
| Best for   | Classic CRUD apps and APIs (still the most common)                   | Real-time features, many slow I/O calls (external APIs), streaming, chat      |

Key points interviewers like:

- Django supports **both**; every new project ships `wsgi.py` *and* `asgi.py`.
- **`async def` views work under WSGI too**, but each one runs in its own event loop, so you get **no** concurrency benefit. You need ASGI for that.
- Under ASGI, **sync views still work**: Django runs them in a thread pool (`sync_to_async`). Mixing in **sync-only middleware** forces extra context switches, which hurts performance.
- `asgiref`'s `sync_to_async()` / `async_to_sync()` bridge the two worlds.
- The **async ORM API** exists (`aget()`, `acreate()`, `acount()`, `async for obj in qs`), but the DB calls still largely run in a thread underneath, and `transaction.atomic()` isn't usable in async code. Wrap transactional logic in a sync function.
- **Django Channels** adds WebSockets via *consumers* + a *channel layer* (usually Redis) for broadcasting between processes.
- **Async ≠ background tasks.** Async helps while a request is *waiting*; anything slow that the user shouldn't wait for (emails, reports, image processing) goes to a **task queue**.

**Background tasks**

- **Celery** = producer (Django) → **broker** (Redis/RabbitMQ) → **workers**; **beat** for schedules; a **result backend** is optional.
- Best practices: pass **IDs, not model instances**; make tasks **idempotent**; set retries with backoff; enqueue inside **`transaction.on_commit()`** so the worker never reads a row that hasn't been committed yet.
- **Django 6.0** added a built-in **Tasks framework** (`@task`, `.enqueue()`) with pluggable backends. The core ships only dev/test backends, so in production you use a backend package such as `django-tasks`.

🛠 **Build:** run the same project with `gunicorn config.wsgi` and with `uvicorn config.asgi:application`. Write a view that calls 3 slow external APIs: sync (sequential) vs async (`asyncio.gather`), and time both. Add a Celery task that sends a welcome email via `on_commit` after signup.

---

## Phase 8 — Testing

📺 **Watch**

1. [Re-write Django tests with pytest | fixtures &amp; test functions](https://www.youtube.com/watch?v=pdatgYDXmSE) ⭐
2. [Django testing &amp; tagging tests](https://www.youtube.com/watch?v=9r1T26vontQ)
3. [pytest markers](https://www.youtube.com/watch?v=7mFQsv2NBG8)
4. [Custom managers | pytest &amp; factory-boy](https://www.youtube.com/watch?v=n47VFgqG-E8) ⭐
5. [Testing context with pytest](https://www.youtube.com/watch?v=3SDQ5M5xn98)
6. [Testing APIs with DRF](https://www.youtube.com/watch?v=sRluxnmZ-H8) ⭐
7. [Permissions &amp; testing permissions (DRF)](https://www.youtube.com/watch?v=rx5IV_4Iuog)
8. [Writing middleware with tests](https://www.youtube.com/watch?v=--ddZc39wVQ)
9. [End-to-end testing with Playwright &amp; pytest](https://www.youtube.com/watch?v=dlds5yN9taM)
10. [time-machine – controlling time in tests](https://www.youtube.com/watch?v=SmBk-jAh_3I)

🧠 **Know for interviews**

- `TestCase` (wraps each test in a transaction → fast) vs `TransactionTestCase` (truncates tables; needed to test `on_commit` / real transactions) vs `SimpleTestCase` (no DB). `pytest-django`'s `@pytest.mark.django_db`.
- `Client` / `APIClient`, `force_authenticate`, `RequestFactory`.
- Fixtures vs **factory-boy** factories; mocking external APIs (`unittest.mock.patch`); `assertNumQueries` to lock in query counts.
- Unit vs integration vs E2E; what you'd test first in a new codebase.

---

## Phase 9 — Architecture, settings & deployment

📺 **Watch**

1. [Service layers and &#34;thin views&#34; for business logic](https://www.youtube.com/watch?v=NvTE1Q7xouU) ⭐
2. [Environment-based settings with django-environ](https://www.youtube.com/watch?v=O4IIBOGFyWI)
3. [Deploying Django apps (Seenode)](https://www.youtube.com/watch?v=EEtbXQWK5_E)
4. [Django with AWS – S3 &amp; CloudFront for media files](https://www.youtube.com/watch?v=RsiXzwesNLQ)
5. [Django &amp; Azure Blob Storage](https://www.youtube.com/watch?v=mfYi_nnn69E)
6. [django-tenants – multi-tenancy with PostgreSQL](https://www.youtube.com/watch?v=seTUY18ge38) ⭐ (common system-design question)
7. [Multiple databases &amp; database routers](https://www.youtube.com/watch?v=GwqZozhZ1MY)
8. [django-waffle – feature flags](https://www.youtube.com/watch?v=K-Y9XHEZwU8)
9. [django-easy-audit – audit logs](https://www.youtube.com/watch?v=Kd9oyUT5DwI)
10. [Internationalization (i18n)](https://www.youtube.com/watch?v=PGMhsAcfPpI)

🧠 **Know for interviews**

- **Fat models vs services:** keep views thin; put business rules in `services.py` (writes) and `selectors.py` (reads) so they're testable and reusable from views, the API, Celery, and management commands.
- **Typical production stack:** Nginx → Gunicorn (WSGI) or Uvicorn (ASGI) → Django → PostgreSQL, plus Redis (cache/broker), Celery workers, S3 for media, and a CDN for static files.
- 12-factor config, `check --deploy`, logging, health checks, and zero-downtime migrations (add a nullable column → backfill → enforce).
- Multi-tenancy: shared schema + `tenant_id` column vs schema-per-tenant (django-tenants) vs DB-per-tenant.

---

## Phase 9.5 — Docker for Django ⭐ (used in most companies)

📺 **Watch**

1. [Docker – Django + PostgreSQL setup (with uv) from scratch](https://www.youtube.com/watch?v=37aNpE-9dD4) ⭐⭐ *main video, code along*
2. [Docker security tip – creating a dedicated user in the container](https://www.youtube.com/watch?v=D0tFRpmARGg) ⭐
3. [uv – Docker setup &amp; using uv in containers (FastAPI app, same ideas apply)](https://www.youtube.com/watch?v=DA6gywtTLL8)
4. [django-q2 with Redis &amp; Docker – background tasks](https://www.youtube.com/watch?v=wjSFMK_IZS8)
5. [cookiecutter-django – see its production Docker setup](https://www.youtube.com/watch?v=aZybyNIgv0M)

📖 **Docs:** [Docker – Python language guide](https://docs.docker.com/guides/python/) ·
[Compose file reference](https://docs.docker.com/reference/compose-file/) ·
[Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)

🧠 **Know for interviews**

- **Image vs container**: an image is the read-only template you build from a `Dockerfile`; a container is a running instance of it. **Volume** = persistent data (e.g. the Postgres data dir). **Network** = how containers find each other: in Compose, the service name *is* the hostname (`DB_HOST=db`, not `localhost`!).
- **Layer caching**: copy `requirements.txt` / `pyproject.toml` and install dependencies **before** `COPY . .`, so code changes don't reinstall everything.
- **Keep images small and safe**: a `python:3.x-slim` base, `.dockerignore` (`.git`, `.venv`, `__pycache__`, `.env`), multi-stage builds, run as a **non-root user**, no secrets baked into the image (pass them as env vars at runtime).
- `PYTHONUNBUFFERED=1` (logs show up immediately) and `PYTHONDONTWRITEBYTECODE=1`.
- **`CMD` vs `ENTRYPOINT`**; `RUN` runs at *build* time, while `CMD` runs at *container start*.
- **Migrations**: run them as a separate step/job (`docker compose run --rm web python manage.py migrate`) or in an entrypoint script, not during `docker build` (the DB isn't available at build time).
- **`depends_on` only controls start order**, not "the DB is ready". Use a `healthcheck` + `condition: service_healthy`.
- Dev vs prod: in dev, bind-mount the code and run `runserver`; in prod, use the baked image + Gunicorn/Uvicorn, `DEBUG=False`, and `collectstatic` at build time.
- Useful commands: `docker compose up -d --build`, `logs -f web`, `exec web python manage.py shell`, `down -v` (⚠ `-v` deletes volumes, i.e. your DB data).

**Reference `Dockerfile`**

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1. dependencies first → cached layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. then the code
COPY . .

# 3. static files baked into the image
RUN python manage.py collectstatic --noinput

# 4. don't run as root
RUN useradd --create-home appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
# ASGI alternative:
# CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
```

**Reference `compose.yaml`: Django + Postgres + Redis + Celery**

```yaml
services:
  web:
    build: .
    env_file: .env
    ports: ["8000:8000"]
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started

  worker:
    build: .
    command: celery -A config worker -l info
    env_file: .env
    depends_on: [db, redis]

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: app
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d app"]
      interval: 5s
      retries: 5

  redis:
    image: redis:7

volumes:
  pgdata:
```

`.env` example: `DATABASE_URL=postgres://app:app@db:5432/app`, `CELERY_BROKER_URL=redis://redis:6379/0`. Notice the hostnames are the **service names** `db` and `redis`.

🛠 **Build:** Dockerise your Phase 5 DRF project with web + Postgres + Redis + Celery. Prove that `docker compose down && docker compose up` keeps your data (the volume). Then shrink the image with a multi-stage build and compare sizes with `docker images`.

---

## Phase 10 — Modern Django (what's new; shows you're up to date)

1. [Django 5.1 – LoginRequiredMiddleware, {% querystring %}](https://www.youtube.com/watch?v=F_cqPmaE8vI)
2. [Django 5.2 – composite primary keys, shell auto-imports, new widgets](https://www.youtube.com/watch?v=ZJr7mmaEXiE)
3. [GeneratedField in Django 5](https://www.youtube.com/watch?v=iTsp-QnlHAQ)
4. [Django 6 released – Tasks, Content Security Policy and more](https://www.youtube.com/watch?v=Ek4aweB1GlQ)
5. [Django 6.1 – fetch modes, mailers and more](https://www.youtube.com/watch?v=ib9am_m2CnM)
6. [Django 6.1 – the new MAILERS setting](https://www.youtube.com/watch?v=603Mj_mtNtQ)
7. [Django Developers Survey 2026](https://www.youtube.com/watch?v=WvrajVKTwz8)

---

## Optional tracks (after the core)

- **Django Ninja** (FastAPI-style, async-friendly APIs — a DRF alternative): [Django-Ninja playlist](https://www.youtube.com/playlist?list=PL-2EBeDYMIbS7bXwkMOS_ajeTdNRnhApX)
- **Other useful backend primers:** [django-filter](https://www.youtube.com/watch?v=FTUxl5ZCMb8) · [model inheritance with django-model-utils](https://www.youtube.com/watch?v=a6JYR3aYAZE) · [django-polymorphic](https://www.youtube.com/watch?v=d8MC2FQ_nqU) · [django-unfold admin theme](https://www.youtube.com/watch?v=kkxAVubUOj8) · [django-import-export](https://www.youtube.com/watch?v=pZSYhei8yPI)

---

## Interview Question Bank

Answer these **out loud** in 30–90 seconds each. 🔥 = asked very often.

### Django basics & architecture

1. 🔥 Explain MVT. How is it different from MVC?
2. 🔥 Project vs app? What happens when you add an app to `INSTALLED_APPS`?
3. 🔥 Walk me through the life of a request in Django, from the browser to the response.
4. FBV vs CBV: when do you pick each? How does `as_view()` / `dispatch()` work?
5. What are mixins? Give 3 built-in examples.
6. Static vs media files. How are they served in production?
7. What does `collectstatic` do?
8. How do you manage settings for dev / staging / prod?
9. What are context processors? Give an example.
10. How do you write a custom management command?

### Middleware & signals

11. 🔥 What is middleware? Write a simple one. In what order does it run on request vs response?
12. Why must `SessionMiddleware` come before `AuthenticationMiddleware`?
13. What are `process_view` and `process_exception` used for?
14. 🔥 What are signals? Name 4. What are their drawbacks?
15. Does `bulk_create()` trigger `post_save`? Does `QuerySet.update()`?

### ORM ⭐

16. 🔥 What is the N+1 problem and how do you fix it?
17. 🔥 `select_related` vs `prefetch_related`: differences in SQL, and when to use each.
18. 🔥 What does "QuerySets are lazy" mean? When does a QuerySet hit the DB?
19. `get()` vs `filter()` vs `first()`.
20. 🔥 F expressions: what problem do they solve? (Race conditions on counters.)
21. Q objects: how do you write an OR query?
22. `aggregate()` vs `annotate()`.
23. `values()` vs `values_list()` vs `only()` vs `defer()`.
24. 🔥 `null=True` vs `blank=True`.
25. 🔥 Explain the `on_delete` options.
26. 🔥 Abstract vs multi-table vs proxy model inheritance.
27. What is a custom Manager? Manager vs QuerySet methods?
28. 🔥 How do transactions work in Django? `atomic()`, `ATOMIC_REQUESTS`, `on_commit()`.
29. What is `select_for_update()`? When would you use it?
30. `save()` vs `update()` vs `bulk_create()` / `bulk_update()`.
31. How do you write a data migration? How do you resolve migration conflicts?
32. When does an index help, and when doesn't it?
33. What is a GenericForeignKey / ContentType? Downsides?
34. `exists()` vs `count()` vs `len(qs)`.
35. How do you run raw SQL safely?

### Auth & security

36. 🔥 Why use a custom User model from day one? `AbstractUser` vs `AbstractBaseUser`?
37. Authentication vs authorization.
38. How does Django store passwords?
39. 🔥 How does Django protect against CSRF, XSS, SQL injection, and clickjacking?
40. Session auth vs token auth vs JWT: pros and cons.
41. Model-level vs object-level permissions.

### DRF ⭐

42. 🔥 `Serializer` vs `ModelSerializer`.
43. 🔥 What is the order of validation in a serializer?
44. 🔥 `APIView` vs `GenericAPIView` vs `ViewSet` vs `ModelViewSet`. What do routers do?
45. How do you handle nested writes?
46. 🔥 `has_permission` vs `has_object_permission`. Why doesn't the object check run on list views?
47. In what order do authentication, permissions, and throttling run?
48. 🔥 How do JWT access and refresh tokens work? How do you log out or revoke a JWT?
49. PageNumber vs LimitOffset vs Cursor pagination.
50. How do you avoid N+1 queries in nested serializers?
51. How do you version an API?
52. PUT vs PATCH vs POST: which are idempotent?

### Performance, caching, async ⭐

53. 🔥 An endpoint is slow. How do you debug it, step by step?
54. Django caching levels. Which backend for multiple servers?
55. 🔥 **ASGI vs WSGI**: differences, servers, and when to use each.
56. 🔥 Can you use `async def` views with WSGI? What happens?
57. What are `sync_to_async` / `async_to_sync`?
58. What is Django Channels? What is a channel layer?
59. 🔥 Celery architecture: broker, worker, beat, result backend.
60. 🔥 Why pass IDs (not objects) to Celery tasks? Why use `on_commit()`?
61. Async views vs background tasks: when do you use which?

### Testing & deployment

62. `TestCase` vs `TransactionTestCase`.
63. How do you test an API endpoint that needs authentication?
64. How do you mock an external API call in tests?
65. 🔥 Describe a production Django deployment (Nginx, Gunicorn/Uvicorn, DB, Redis, Celery, static files).
66. What does `python manage.py check --deploy` check?
67. How would you build a multi-tenant SaaS in Django?
68. How do you run migrations with zero downtime?

### Docker

69. 🔥 Image vs container vs volume. How do containers talk to each other in Compose?
70. 🔥 Walk me through your Django `Dockerfile`. Why copy `requirements.txt` before the code?
71. Why can't the Django container connect to `localhost:5432`?
72. `depends_on` vs healthchecks: does `depends_on` wait for Postgres to be ready?
73. Where do you run migrations and `collectstatic` in a Docker setup?
74. How do you keep secrets out of images? How do you make images smaller and more secure?
75. `CMD` vs `ENTRYPOINT` vs `RUN`.

### "Tell me about…" (prepare stories from your 2 years)

- The hardest bug you fixed in Django.
- A performance problem you solved (show numbers: queries 120 → 3, p95 2s → 200ms).
- How you structured a large Django codebase.
- A time you used transactions, caching, or Celery in production.

---

## Final checklist before interviews

- [ ] Can draw the request lifecycle + middleware order from memory
- [ ] Can explain and **demo** an N+1 fix with `select_related` / `prefetch_related`
- [ ] Can write F / Q / annotate / aggregate / Subquery queries without looking anything up
- [ ] Have built a custom User model + permissions
- [ ] Have built a full DRF API with JWT, ViewSets, filtering, pagination, permissions, tests
- [ ] Can explain ASGI vs WSGI with a table + know the async caveats
- [ ] Have used Celery (or Django Tasks) with `on_commit`
- [ ] Have a Dockerised project (web + Postgres + Redis + Celery via Compose) on GitHub with a clean README
- [ ] Can explain every line of my Dockerfile and compose.yaml
- [ ] Know what changed in Django 5.x / 6.x

Good luck! 🚀
