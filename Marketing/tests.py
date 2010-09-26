import unittest
import django.contrib.auth.models
from django.contrib.auth.models import User
import Marketing.models

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('john1', 'lennon1@thebeatles.com', 'johnpassword')
        self.user2 = User.objects.create_user('john2', 'lennon2@thebeatles.com', 'johnpassword')

        self.user1.save()
        self.user2.save()

        self.tree_node1 = Marketing.models.BinaryTree(user=self.user1, parent = None)
        self.tree_node1.save()

        self.tree_node2 = Marketing.models.BinaryTree(user=self.user2, parent = None)
        self.tree_node2.save()

    def test_creation(self):
        print "Running test creation"
        self.tree_node2.insert_at(target=self.tree_node1)
        self.assertTrue(self.tree_node1.parent == None)
        print '-------=-=-=-=-=---------',self.tree_node1.get_children()