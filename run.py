from user import User
from credentials import Credential

def create_user_account(username , password):
    '''
    function to create a user account
    '''
    new_user = User(username ,password)
    return new_user

def save_users(user):
    '''
    function thats saves a created user account
    '''    
    user.save_user()
    
def create_credentials(self,account,cred_username,cred_password):
    '''
    function that creates new credential object
    '''
    new_credential = Credential(self,account, cred_username, cred_password)
    return new_credential

def save_credentials(credential):
    '''
    function to save new credentials
    '''
    Credential.save_credential(self)

def generating_password():
    '''
    function to generate a password
    '''
    password = Credential.generate_password()  
    return password  


def main():
    '''
    The method that runs the whole password locker app
    '''
    print("Welcome to password-locker!!!")
    print("Use the following options to access the service you want.")
    
    
    while True:
        print('''
        1-Create a new password locker account
        2-Login to your password account 
        ''')
        number = input()

        if number == "1":
            '''
            Creates a new password locker account 
            '''
            print("Provide username...")
            username = input()
            
            print("Provide password...")
            password = input()

            save_users(create_user_account(username ,password))
            print("Welcome to your new password locker account,your details are:" )
            print(f"Username: {username} , Password:{password}")
            print("You can now procced to log in to your account")

#         elif number == "2":
#             '''
#             Logs in the user in to their already created password locker account    
#             '''
#             print("Provide username...")
#             username = input()

#             print("Provide the password...")
#             password = input()

#             print("Use the following choices to navigate through credentials...")
            
#             while True :
#                 '''
#                 While loop to use after loggin in
#                 '''
#                 print('''options:
#                     1-Create a new credential - your own password
#                     2-Create a new credential - generated password
#                     3-Display existing account credentials
#                     ''')
#                 number = input()


#                 if number == "1":
#                     '''
#                     creating a new credential using own password
#                     '''
#                     print("Enter the name of the account:")
#                     account = input()
#                     print("Enter the username you want for the account:")
#                     cred_username = input()
#                     print("Enter the password you desire:")
#                     cred_password = input()

#                     #save_credentials( create_credentials(self,account,cred_username,cred_password))
#                     #print(f"Your {account} credentials have been successfully created!")

#                 elif number =="2" : 
#                     '''
#                     creating a new credential using generated password
#                     ''' 
#                     print("Enter the name of your account:")
#                     account = input() 
#                     print("Enter the username you want for the account:") 
#                     cred_username = input() 
#                     save_credentials(Credential(account, cred_username, (generating_password())))  
#                     print(f"Your {account} credentials have been successfully created!")


#                 elif number == "3":
#                     '''
#                     Enables viewing of existing credentials
#                     '''
#                     view_credentials()    



# if __name__ == '__main__' :
#         main()    