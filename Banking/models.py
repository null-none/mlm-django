from django.db import models, settings
from django.contrib import admin
from django.contrib.auth.models import User

class Transaction(models.model):
    marketing_plan = models.CharField(max_length=50, choices=settings.TREE_TYPES)
    sender = models.ForeignKey(User, unique=False, related_name='profile')
    receiver = models.ForeignKey(User, unique=False, related_name='profile')
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    
