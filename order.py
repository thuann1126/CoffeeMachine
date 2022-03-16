#This file contain order and purchase information and functions

from retailler import Retailler
from makingProcess import MakingProcess

menu = Retailler()
orders = []
mkprocess = MakingProcess(orders)

class Order():

    #pay for the order
    def purchase(self, orders):
        total = 0
        credit  = 0.00
        purchaseChecker = False

        for o in orders:
            total += menu.MENU[o]["cost"]

        print(f"your total purchase is: {total}")

        while purchaseChecker ==False:
            try:
                userPayment = float(input("Enter your paying amount: "))
                credit += userPayment
            except Exception:
                print("Please enter floating number only...")
                continue
            if(credit < total):
                print("Your payment is not enough please insert more money")
                continue
            else:
                print("Your purchase is successfully")
                menu.MONEYTRAY["credit"] += total
                print(f"Your exchange is: {credit - total}")
                print("Thank you for buying at the coffee machine")
                purchaseChecker = True

    # make order, ask input, return orders list, annoucement
    def makeOrder(self):


        orderChecker = False

        #Checking the order
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

                if mkprocess.processOrder() == True:
                    print("\n your order is completed")
                    self.purchase(orders)
                else:
                    print("Your order is canceled because the machine is out of stock.")
                    orders.clear()

                orderChecker = True

            elif(completedOrer == "yes"):
                print("\n add to your order")
                continue

            elif(completedOrer == "back"):
                print("Go back to the main menu.")
                break
            else:
                print("\nYour input is invalid please add an item")









