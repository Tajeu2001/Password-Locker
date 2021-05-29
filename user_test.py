import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviour.
    Args:
        unittest.TestCase
    '''
    def setUp(self):
      '''
      Set up method to run before each test case
      ''' 
      self.new_user = User("Tajeu2001" , "siantayo15")

    def test_init(self):
      '''
      test_init test case to test if the object is initialized properly 
      '''  

      self.assertEqual(self.new_user.username , "Tajeu2001")  
      self.assertEqual(self.new_user.password , "siantayo15")

if __name__ == '__main__':
    unittest.main()       