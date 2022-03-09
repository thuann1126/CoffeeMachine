"""
Project: Coffee Machine
Author: Thuan Nguyen
Skill sets: OOP,
Last modified: March 1, 2022
"""
from order import Order
from administration import Management
from retailler import Retailler

retail = Retailler()

def annoucement():
    print("""   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \

 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|

                                                                      """)
    print("TODAY MEMU")
    for i in retail.MENU:
        print (i +": $" +str(retail.MENU[i]["cost"]))

    print("\nPlease order by TYPING THE NAME of the drink")
    print("you can order multi drink at a time, separated by space")
    print("If you are the administrator, you can login to me to check my status.")
    print("\nCommand:")
    print("order: to make an order")
    print("login: to login to the system")
    print("cancel: to cancel to order and leave\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = Order()
    admin = Management()
    controller = False

    annoucement()

    while controller == False:
        userInput = input("Enter your command: ")
        if userInput == "order":
            order.makeOrder()

        elif userInput == "login":
            admin.login()

        elif userInput == "cancel":
            print("Thank you! See you soon!")
            controller = True

        else:
            print("Your command is invalid, please try again")
            continue


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
