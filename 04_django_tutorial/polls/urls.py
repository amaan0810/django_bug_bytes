from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path("",views.index,name="index"),
    path("xyz/<int:question_id>",views.detail,name='detail'),
    path("<int:question_id>/votes",views.vote,name='vote')
]
