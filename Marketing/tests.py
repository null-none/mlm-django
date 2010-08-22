import unittest
import django.contrib.auth.models
from django.contrib.auth.models import User
import Marketing.models

class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('john1', 'lennon1@thebeatles.com', 'johnpassword')
        self.user2 = User.objects.create_user('john2', 'lennon2@thebeatles.com', 'johnpassword')
        self.user3 = User.objects.create_user('john3', 'lennon3@thebeatles.com', 'johnpassword')
        self.user4 = User.objects.create_user('john4', 'lennon4@thebeatles.com', 'johnpassword')

        self.user1.save()
        self.user2.save()
        self.user3.save()
        self.user4.save()

        self.tree_node1 = Marketing.models.BinaryTree(user=self.user1, parent = None)
        self.tree_node1.save()

        self.tree_node2 = Marketing.models.BinaryTree(user=self.user2, parent = None)
        self.tree_node2.save()

        self.tree_node3 = Marketing.models.BinaryTree(user=self.user3, parent = None)
        self.tree_node3.save()

        self.tree_node4 = Marketing.models.BinaryTree(user=self.user4, parent = None)
        self.tree_node4.save()

    def test_creation(self):
        print "Running test creation"
        self.assertTrue(self.tree_node1.get_children().count() == 0)
        self.assertTrue(self.tree_node1.parent == None)
        


