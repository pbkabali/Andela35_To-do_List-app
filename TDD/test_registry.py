import unittest
from registry import User

class TestRegistry(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.user.register("Paul", "pbkabali", "kabali", 30, "engineerbpk@gmail.com", "male")
        
    def test_instance(self):
        self.assertIsInstance(self.user, User)

    def test_registerUserName_sameAsName(self):
        with self.assertRaises(ValueError):
            self.user.register("paul balitema", "paul", "kabali", 30, "engineerbpk@gmail.com", "male")

    def test_registerUserName_lessThan4chars(self):
        with self.assertRaises(ValueError):
            self.user.register("paul balitema", "pbk", "kabali", 30, "engineerbpk@gmail.com", "male")            

    def test_registerAge_characterEntered(self):
        with self.assertRaises(ValueError):
            self.user.register("paul balitema", "pbkabali", "kabali", "AA", "engineerbpk@gmail.com", "male")  

    def test_registerAge_negativeAge(self):
        with self.assertRaises(ValueError):
            self.user.register("paul balitema", "pbkabali", "kabali", -2, "engineerbpk@gmail.com", "male")                      

    def test_registerEmail_wrongFormat(self):
        with self.assertRaises(ValueError):
            self.user.register("paul balitema", "pbkabali", "kabali", 30, "engineerbpk.com", "male")                      

    def test_changeUserName_notLoggedIn(self):
        self.assertEqual(self.user.change_username("good", "kabali"), "You have to be logged in to change account details!")    

    def test_changeUserName_rightConfirmationPassword(self):
        self.user.login("pbkabali", "kabali")
        self.assertEqual(self.user.change_username("kabali", "good"), "Your username has been changed to: good")

    def test_changeUserName_wrongConfirmationPassword(self):
        self.user.login("pbkabali", "kabali")
        self.assertEqual(self.user.change_username("hkjla", "good"), "You have supplied an incorrect confirmation password!")
    