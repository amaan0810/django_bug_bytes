from django.shortcuts import get_object_or_404, render,redirect
from .models import Book
from django.urls import reverse

def index(request):
    return render(request, "index.html")

def books(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book_detail.html", {"book": book})


def redirect_me(request):
    # return redirect(reverse("book-list"))
    return redirect(reverse("books:book-detail", kwargs={"pk": 1}))
