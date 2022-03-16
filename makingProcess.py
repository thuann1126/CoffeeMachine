# This class is used for making orders and calculating retailing information
from retailler import Retailler

retail = Retailler()
class MakingProcess:
    def __init__(self, orders):
        self.order = orders

    def processOrder(self):
        for o in self.order:
            for key, value in retail.MENU[o.__str__()]["ingredients"].items():
                retail.STORAGE[key] -= value
                if retail.STORAGE[key] < 0:
                    print("Out of " + key.__str__() + " to make you order")
                    retail.STORAGE[key] += value
                    return False
        return True


