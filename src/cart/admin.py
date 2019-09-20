from django.contrib import admin
from .models import Cart, CartItem
from django.utils.safestring import mark_safe

# class CartItemInline(admin.StackedInline):
#     model = CartItem
#     extra = 0

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'user_ip', 'total_price', 'total_discount', 'created_at', 'updated_at'
    ]
    readonly_fields = [
        'user_ip', 'user_agent', 'cart_items'
    ]
    
    def cart_items(self, obj=None):
        # items = ''
        print(obj.items.all())
        return mark_safe(f'<p>items</p>')
        
        # for item in obj.items:
        #     items += f'<li>{item.title} - ${item.price}</li>'
        # return make_safe(items)
    cart_items.short_description = 'Cart Items'

admin.site.register(Cart, CartAdmin)


