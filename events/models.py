# Create your models here.
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title