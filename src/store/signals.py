from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Product, Collection

@receiver(pre_save, sender=Product)
def product_generate_handle(sender, instance,**kwargs):
    handle = slugify(instance.title)
    handleCount = Product.objects.filter(handle=handle).count()
    if handleCount > 0:
        handle = f'{handle}-{handleCount+1}'
    instance.handle = handle    

@receiver(pre_save, sender=Collection)
def collection_generate_handle(sender, instance,**kwargs):
    handle = slugify(instance.name)
    handleCount = Collection.objects.filter(handle=handle).count()
    if handleCount > 0:
        handle = f'{handle}-{handleCount+1}'
    instance.handle = handle    