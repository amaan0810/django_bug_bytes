from django.contrib import admin
from .models import Question,Choice
# Register your models here.

admin.site.index_title="POlls "

admin.site.register(Question)
admin.site.register(Choice)
