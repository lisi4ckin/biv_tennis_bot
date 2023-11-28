from django.contrib import admin
from .models import User, UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'user_rating')


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username',)

# Register your models here.
