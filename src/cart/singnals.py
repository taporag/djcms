from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cart, CartItem

@receiver(post_save, sender=Cart)
def create_cart_items(sender, instance, **kwargs):
    cart_id = instance.id
    print(cart_id)