from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustomUserChangeForm

class CustomerUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('bio', 'phone', 'locale')
        }),
    )
admin.site.register(User, CustomerUserAdmin)