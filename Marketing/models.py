from django.db import models
from django.contrib import admin
import mptt
from django.contrib.auth.models import User
from mpttadmin import MpttAdmin

class BaseTree(models.Model):
    user = models.ForeignKey(User, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.user.username

mptt.register(BaseTree)

class BaseTreeAdmin(MpttAdmin):
    tree_title_field = 'name'
    tree_display = ('user',)
    #tree_editable = ('user','parent')
    class Meta:
        model = BaseTree

admin.site.register(BaseTree, BaseTreeAdmin)