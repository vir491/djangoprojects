from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Image(models.Model):
    pic = models.ImageField(null=False, blank=False)
    text = models.TextField(blank=True, max_length=200)

    def get_absolute_url(self):
        return "/images/%s/" % self.id
