from django.db import models
from helpers.helpers import image_upload_location

class Page(models.Model):
    name = models.CharField(max_length=50)
    handle = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    excerpt = models.TextField(max_length=150, blank=True)
    featured_image = models.ImageField(blank=True, upload_to=image_upload_location('collections'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField(auto_now=False, blank=True)
