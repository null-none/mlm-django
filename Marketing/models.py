from django.db import models, settings
from django.contrib import admin
import mptt
from django.contrib.auth.models import User
from mpttadmin import MpttAdmin

class BaseTree(models.Model):
    user = models.ForeignKey(User, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.user.username

class BinaryTree(models.Model):
    user = models.ForeignKey(User, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.user.username
    def binary_insert_at(self, target, position='first-child', commit=False):
        print '|--> mptt models.py binary_insert_at'
        try:
            children_count = target.get_chilren.count()
        except:
            children_count = 0
        if children_count<2:
            print position
            self._tree_manager.insert_node(self, target, position, commit)
        else:
            print 'exception insert_at'
            # exception is generated
    def binary_move_to(self, target, position='first-child'):
        print '|--> mptt models.py binary_move_to'
        try:
            children_count = target.get_chilren.count()
        except:
            children_count = 0
        if children_count < 2:
            self._tree_manager.move_node(self, target, position)
        else:
            self._tree_manager.move_node(self, None, position)
            print 'exception move_to'
            # exception is generated

class LevelTree(models.Model):
    user = models.ForeignKey(User, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.user.username
    def level_insert_at(self, target, position='first-child', commit=False):
        print '|--> mptt models.py level_insert_at'
        print 'good owerride'
        self._tree_manager.insert_node(self, target, position, commit)

mptt.register(BaseTree)
mptt.register(BinaryTree)
mptt.register(LevelTree)
setattr(BinaryTree, 'insert_at', BinaryTree.binary_insert_at)
setattr(BinaryTree, 'move_to', BinaryTree.binary_move_to)
setattr(LevelTree, 'insert_at', LevelTree.level_insert_at)

class BaseTreeAdmin(MpttAdmin):
    tree_title_field = 'name'
    tree_display = ('user',)
    class Meta:
        model = BaseTree

class BinaryTreeAdmin(MpttAdmin):
    tree_title_field = 'name'
    tree_display = ('user',)
    class Meta:
        model = BinaryTree

class LevelTreeAdmin(MpttAdmin):
    tree_title_field = 'name'
    tree_display = ('user',)
    class Meta:
        model = LevelTree

admin.site.register(BaseTree, BaseTreeAdmin)
admin.site.register(BinaryTree, BinaryTreeAdmin)
admin.site.register(LevelTree, LevelTreeAdmin)


class MarketingRates(models.Model):
    marketing_tree = models.CharField(max_length=50, choices=settings.TREE_TYPES)
    generation = models.IntegerField()
    commission = models.FloatField()
    def __unicode__(self):
        return self.marketing_tree
    class Meta:
        ordering = ('marketing_tree', )

class MarketingRatesAdmin(admin.ModelAdmin):
    list_display = ('marketing_tree', 'generation', 'commission',)

admin.site.register(MarketingRates, MarketingRatesAdmin)