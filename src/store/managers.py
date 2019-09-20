from django.db import models

class ProductQuerySet(models.QuerySet):
    def url(self):
        return self.only('handle')
    def images(self):
        return self.only('featured_image')

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def url(self):
        return self.get_queryset().url()
    
    def images(self):
        return self.get_queryset().images()