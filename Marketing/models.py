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
        try:
            descendant_count = target.get_descendant_count()
        except:
            descendant_count = 0
        print 'amount of children ...', descendant_count
        if descendant_count<2:
            self._tree_manager.insert_node(self, target, position, commit)
        else:
            print 'exception insert_at'
            print 'amount of children ...', descendant_count
            # exception is generated
    def binary_move_to(self, target, position='first-child'):
        try:
            descendant_count = target.get_descendant_count()
        except:
            descendant_count = 0
        print 'amount of children ...', descendant_count
        if descendant_count<2:
            self._tree_manager.move_node(self, target, position)
        else:
            print 'exception move_to'
            print 'amount of children ...', descendant_count
            # exception is generated


class LevelTree(models.Model):
    user = models.ForeignKey(User, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    def __unicode__(self):
        return self.user.username
    def level_insert_at(self, target, position='first-child', commit=False):
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

admin.site.register(MarketingRates)