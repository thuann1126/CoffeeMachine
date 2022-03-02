#This file contain order information and functions
from retailler import Retailler

class Order():

    def annoucement(self):
        print("""   _____       __  __            __  __            _     _            
      / ____|     / _|/ _|          |  \/  |          | |   (_)           
     | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
     | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \

     | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
      \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|

                                                                          """)
        print("Please order by typing the name of the drink")
        print("you can order multi drink at a time, separated by space")

    # make order, ask input, return orders list, annoucement
    def makeOrder(self):

        menu = Retailler()

        orders = []
        orderChecker = False

        while orderChecker == False:
            userInput = input('Enter your orders: ')


            for o in userInput.split():
                if o in menu.MENU.keys():
                    orders.append(o)
                else:
                    print(f"\nyou have an invalid order: {o}")
                    continue
            print(orders)
            print("Would you like to add anything? (yes/no)")
            completedOrer = input()
            if(completedOrer == "no"):
                print("\n your order is completed")
                orderChecker = True
            if(completedOrer == "yes"):
                print("\n add to your order")
                continue
            else:
                print("\n your input is invalid please add an item")









