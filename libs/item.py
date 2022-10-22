from thing import Thing

class Item(Thing): #inherits from the Thing parent class
    __itemPrice = 0

    def __init__(self, itemName, itemPrice:float):
        super().__init__(itemName)
        if self.isValidArgType(itemPrice, "'float'"):
            self.__itemPrice = itemPrice

    def setPrice(self, price:float):
        if self.isValidArgType(price, "'float'"):
            self.__itemPrice = round(price, 2)

    def getPrice(self):
        return self.__itemPrice

    def __str__(self):
        item = f"Name={self.getName()}, Price={self.__itemPrice}"
        return item