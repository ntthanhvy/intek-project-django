from django.contrib import admin
from .models import Actor, Movie, Category, Comment


# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Comment)