"""
This class contain the commands which only
the administrator is authorized to perform
"""
from retailler import Retailler

class Management():

    def login(self):
        retail = Retailler()
        loginControl = True

        while loginControl:
            usernameInput = input("username: ")
            passwordInput = input("password: ")
            for key, value in retail.ADMINACCOUNTS.items():
                if usernameInput == key and passwordInput == value:
                    print("Login successfully!")

                    loginControl = True
                    return True
            if usernameInput == "menu":
                return False
            else:
                print("Login failed! Please login again or type MENU to go back command prompt.")

    def storageManagement(username):
        print("\nWelcome " + username +". What you want to do today?")
        print("""
                str: to check the storage \n
                add + name of ingredient: to add the missing ingredients, you can add multiple at a time split by separated space \n
                ms : to check the money stray \n
                dp : to deposit money to the stray \n
                 
                """)




