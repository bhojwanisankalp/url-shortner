from django.db import models

# Create your models here.
class Url(models.Model):
    """ To store and associate short url with original url """
    name = models.CharField(max_length=50,blank=True)
    original_url = models.URLField(max_length=2000, null=True)
    slug = models.CharField(max_length=15, null=True)
    created_at  = models.DateTimeField(auto_now_add = True, null = True)
    updated_at = models.DateTimeField(auto_now = True, null = True)