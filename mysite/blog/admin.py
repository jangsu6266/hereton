from django.contrib import admin

# Register your models here.
from .models import Subject, Comment, Hashtag

admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Hashtag)
