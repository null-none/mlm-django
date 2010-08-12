from django.db import models
from django.contrib import admin

class NewsItem(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp', )

admin.site.register(NewsItem)