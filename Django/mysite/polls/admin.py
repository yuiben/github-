from django.contrib import admin
from .models import Choice, Post, Question
# Register your models here.

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Post)
