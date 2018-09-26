import unittest
from registry import *

class TestRegistry(unittest.TestCase):

    def setUp(self):
        self.user = User("Mike")

    def test_instance(self):
        self.assertIsInstance(self.user, User)

    def test_userInstantiation(self):
        self.assertEqual(self.user.name, "Mike")

    def test_creationOfUsername(self):
        self.assertEqual(self.user.create_username("pbks"), {"Mike":"pbks"})