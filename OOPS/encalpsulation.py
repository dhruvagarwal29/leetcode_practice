"""
Encapsulation is restriction access to methods and varaibles 
"""

class Computer:
    def __init__(self) -> None:
        self._maxprice = 900

    def setmaxprice(self,price):
        self._maxprice = price

obj = Computer()
