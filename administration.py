"""
This class contain the commands which only
the administrator is authorized to perform
"""
from retailler import Retailler

retail = Retailler()
addingIngredients = []
class Management():

    def login(self):

        loginControl = True

        while loginControl:
            usernameInput = input("username: ")
            passwordInput = input("password: ")
            for key, value in retail.ADMINACCOUNTS.items():
                if usernameInput == key and passwordInput == value:
                    print("Login successfully!")
                    self.storageManagement(usernameInput)
                    loginControl = True
                    return True
            if usernameInput == "menu":
                return False
            else:
                print("Login failed! Please login again or type MENU to go back command prompt.")

    def storageManagement(self, username):
        print("\nWelcome " + username +". What you want to do today?")
        controller = False

        while controller == False:

            print("""
                            str: to check the storage
                            add + name of ingredient: to add the missing ingredients, you can add multiple at a time split by separated space
                            ms : to check the money stray
                            dp : to deposit money to the stray
                            back: go back to the main menu
                            """)

            print("\nAdmin command: ")
            userInput = input()

            if(userInput == "str"):
                print("Retailer information: \n")

                for key, value in retail.STORAGE.items():
                    print(key + ": " + value.__str__())

            elif (userInput == "add"):
                print("Enter the name of the ingredient and quantity. Type done when you finish. ")

                addingController = False

                while addingController == False:

                    ingreInput = input("Ingredients name: ")


                    if (ingreInput == "done"):
                        print("Go back to main commands.")
                        addingController = True
                        break
                    quantity = int(input("Quantity: "))
                    retail.STORAGE[ingreInput] += quantity

            elif (userInput == "ms"):
                print("Total credit: ")
                print(retail.MONEYTRAY["credit"])

            elif (userInput == "dp"):
                print("Enter the amount you want to deposit: ")
                moneyDeposited = int(input())
                retail.MONEYTRAY["credit"] += moneyDeposited
                print ("You successfully deposited " + moneyDeposited.__str__() + "to the coffee machine credit")

            elif (userInput == "back"):
                print("Go back to the main menu \n")
                controller = True
            else:
                print("Your command is invalid, please try again.")




