from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from helpers.helpers import image_upload_location

class ProductAttributes(models.Model):
    title = models.CharField(max_length=100)
    handle = models.SlugField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    compare_at_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)        
    featured_image = models.ImageField(blank=True, upload_to=image_upload_location('products'))
    sku = models.CharField(max_length=30, blank=True)

    class Meta:
        abstract = True

class Collection(models.Model):
    name = models.CharField(max_length=50)
    handle = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(blank=True, upload_to=image_upload_location('collections'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Product(ProductAttributes, models.Model):
    description = models.TextField(blank=True) 
    collection = models.ManyToManyField(Collection,blank=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @staticmethod
    def pre_save(sender, instance, *args, **kwargs):
        instance.slug = slugify(instance.title)

class Variant(ProductAttributes, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)    

    def __str__(self):
        return self.title    


