import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviour.
    Args:
        unittest.TestCase
    '''
    def setUp(self):
      '''
      Set up method to run before each test case
      ''' 
      self.new_credential = Credential("Twitter", "Tajeu2001", "siantayo15")

    def test_init(self):
#       '''
#       test_init test case to test if the object is initialized properly 
#       '''  

#       self.assertEqual(self.new_credential.account , "Twitter")  
#       self.assertEqual(self.new_credential.username , "Tajeu2001")
#       self.assertEqual(self.new_credential.password , "siantayo15")


# if __name__ == '__main__':
#     unittest.main()       