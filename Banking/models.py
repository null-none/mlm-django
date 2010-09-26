from django.db import models, settings
from django.contrib import admin
from django.contrib.auth.models import User

class Transaction(models.Model):
    marketing_plan = models.CharField(max_length=50, choices=settings.TREE_TYPES)
    sender = models.ForeignKey(User, unique=False, related_name='user_sender')
    receiver = models.ForeignKey(User, unique=False, related_name='user_receiver')
    date = models.DateTimeField()
    amount = models.FloatField()
    
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('marketing_plan', 'date', 'sender', 'receiver', 'amount',)

admin.site.register(Transaction, TransactionAdmin)