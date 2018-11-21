import unittest
from app.models import User
class UserModelTest(unittest.TestCase):
    '''
    Tests to confirm password hashing
    '''

    def setUp(self):
        self.new_user = User(password = 'danmark')
        '''
        This creates an instance of the User class object and passes in a password property to be verified
        '''

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
        '''
        This test checks that the app will give an AttributeError when someone tries to access the password property
        '''

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('danmark'))
        '''
        This verifies that the password that users input is verifiable with the hashed password
        '
