from django.db import models
from store.models import Product

class CartQueryset(models.QuerySet):
    pass

class CartManager(models.Manager):
    pass