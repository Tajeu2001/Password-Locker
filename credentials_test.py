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
      '''
      test_init test case to test if the object is initialized properly 
      '''  

      self.assertEqual(self.new_credential.account , "Twitter")  
      self.assertEqual(self.new_credential.cred_username , "Tajeu2001")
      self.assertEqual(self.new_credential.cred_password , "siantayo15")


    def test_delete_credential(self):
      '''
      test if credentials can be deleted
      '''
      self.new_credential.save_credential()
      test_credential = Credential("Instagram", "Tajeu2001", "siantayo15") 
      test_credential.save_credential()
      self.new_credential.delete_credential()
      self.assertEqual(len(Credential.credential_list), 1) 


    def test_generate_password(self):
      '''
      Test to see if a random password can be generated
      '''
      password = self.new_credential.generate_password()
      self.assertEqual(len(password), 6)

    def test_view_credentials(self):
      '''
      test if credentials can be viewed
      '''
      self.assertEqual(Credential.view_credentials(),Credential.credential_list)  


if __name__ == '__main__':
    unittest.main()       