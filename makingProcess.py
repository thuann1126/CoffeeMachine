# This class is used for making orders and calculating retailing information
from retailler import Retailler

class MakingProcess:
    def __init__(self, order):
        self.orders = order


    def storageCalculation(self):
        re = Retailler()
        for orde in self.orders.items:
            for instore in re.STORAGE