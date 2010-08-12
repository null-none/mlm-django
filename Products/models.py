from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category, unique=False, related_name='category')

admin.site.register(Category)
admin.site.register(Product)




    
