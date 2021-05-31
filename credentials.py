import random
import string


'''
Credentials class for creating user credentials
'''

class Credential:

    '''
    class used as a blueprint to generate other instances of user credentials
    '''

    credential_list = []

    def __init__(self,account,cred_username,cred_password):
      '''
      method to define properties for the credential class object
      '''
      
      self.account = account
      self.cred_username = cred_username
      self.cred_password = cred_password

    def save_credential(self):
      '''
      method that adds a new user to the user list
      '''

      Credential.credential_list.append(self)

    def delete_credential(self):
      '''
      Method for deleting credentials
      '''
      Credential.credential_list.remove(self)  

    @classmethod
    def generate_password(cls):
      '''
      Method that generates a random password
      '''
      size = 6
      rand_password = string.ascii_uppercase + string.ascii_lowercase
      password = ''.join(random.choice(rand_password) for num in range(size))  

      return password
      print(password)


    @classmethod
    def view_credentials(cls,):  
      '''
      method that allows users to view saved credentials in credentials list
      '''
      return cls.credential_list    
  