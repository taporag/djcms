from django.db import models
from django.contrib.sessions.models import Session
from django.utils.translation import ugettext_lazy as _
from store.models import Product
from .managers import CartManager


class CartItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.item)


class Cart(models.Model):
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    user_ip = models.CharField(max_length=14, editable=False, unique=True)
    user_agent = models.CharField(max_length=100, blank=False, editable=False)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(decimal_places=2, max_digits=15)
    total_discount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return self.user_ip



    