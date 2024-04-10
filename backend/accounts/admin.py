from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    class meta:
        model = CustomUser

        
admin.site.register(CustomUser, CustomUserAdmin)