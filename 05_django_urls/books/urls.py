# core/urls.py
from django.urls import path
from . import views

app_name="books"

urlpatterns = [
    path("home/", views.index,name='index'),
    path("books/", views.books,name='book-list'),
    path("books/<int:pk>/", views.book_detail,name='book-detail'),
    path("redirect/",views.redirect_me,name="redirect")
]