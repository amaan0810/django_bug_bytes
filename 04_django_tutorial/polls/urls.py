from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("xyz/<int:pk>",views.DetailView.as_view(),name='detail'),
    path("<int:question_id>/votes",views.vote,name='vote'),
    path("<int:question_id>/results",views.ResultView.as_view(),name='results')
]
