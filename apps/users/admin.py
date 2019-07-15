from django.contrib import admin
from .models import User


class UserOption(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'active')


admin.site.register(User, UserOption)
