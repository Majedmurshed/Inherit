from thing import Thing

class Store(Thing): #inherits from the Thing parent class
    __storeStock = dict()

    def __init__(self, storeName):
        super().__init__(storeName)

    def getStoreStock(self):
        return self.__storeStock

    def addToStock(self, item:object, amount:int):
        itemName = item.getName().lower()
        items = self.__storeStock.keys()
        if itemName in items:
            self.__storeStock.get(itemName).append(item)
        else:
            self.__storeStock[itemName] = [item]

    def removeFromStock(self, item:object, amount:int):
        currStockItems = set(self.__storeStock.keys())
        itemName = item.getName()
        if len(currStockItems) == 0:
            return False
        else:
            if itemName in currStockItems:
                newItemList = self.__storeStock.get(itemName)
                for i in range(amount):
                    if len(newItemList) == 0:
                        self.__storeStock.pop(itemName)
                    else:
                        newItemList = newItemList.pop()
                self.__storeStock[itemName] = newItemList
            else:
                return False

    def __str__(self):
        aString = f"{self.getName()} has:"
        if len(self.__storeStock.keys()) == 0:
            aString += " Nothing"
        else:
            for key in self.__storeStock:
                aString += f"\n\r  {key}, amount={len(self.__storeStock.get(key))}, unit price={self.__storeStock.get(key)[0].getPrice()}"

        return aString


