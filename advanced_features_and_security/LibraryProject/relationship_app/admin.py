from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class UserAdmin (BaseUserAdmin):
  list_display = ["username", "date_of_birth"]
admin.site.register(CustomUser, CustomUserAdmin)