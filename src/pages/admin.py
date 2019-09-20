from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'publish_at']

admin.site.register(Page, PageAdmin)
