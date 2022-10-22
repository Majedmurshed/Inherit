from thing import Thing

class ShoppingList(Thing): #inherits from the Thing parent class
    __listItem = []
        
    def __init__(self, listName):
        super().__init__(listName)

    def getListItem(self):
        return self.__listItem

    def addToList(self, item:object):
        self.__listItem.append(item)
    
    def removeFromList(self, itemName:str):
        for item in self.__listItem:
            if item.getName() == itemName.lower():
                self.__listItem.remove(item)

    def getTotalPrice(self):
        total = 0
        for item in self.__listItem:
            total += item.getPrice()
        total = round(total, 2)
        return total

    def __str__(self):
        items = "This is your " + self.__listItem + " list\n"
        count = 1
        for item in self.__listItem:
            items += f" {count}. {item}\n"
            count += 1
        return items