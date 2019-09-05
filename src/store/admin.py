from django.contrib import admin

from .models import Collection, Product, Variant

class VariantInline(admin.StackedInline):
    model = Variant
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at']
    inlines = [
        VariantInline,
    ]
admin.site.register(Product, ProductAdmin)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'handle']

admin.site.register(Collection, CollectionAdmin)