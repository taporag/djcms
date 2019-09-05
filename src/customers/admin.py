from django.contrib import admin

from .models import Customer, CustomerAddress

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'created_at']

admin.site.register(Customer, CustomerAdmin)

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['address1', 'full_name']

admin.site.register(CustomerAddress, CustomerAddressAdmin)
