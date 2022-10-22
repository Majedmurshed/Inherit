import os
from sys import path
path.append("libs") #adds the libs directory path to your systems PATH variable
from shoppinglist import ShoppingList #The class is in the libs directory
from store import Store #The class is in the libs directory
from item import Item #The class is in the libs directory
from csv import reader

userLists = dict()
stores = dict()

def printUserOptions():
        print("""
        \rHERE ARE YOUR OPTIONS:
        \r
        \r  FIRST THING (What operation your want to do?)
        \r  1. Store operations
        \r  2. List operations
        \r  3. prints stores available
        \r  4. prints lists available
        \r  q. To quit the program
        \r
        \r  Store operations:
        \r    1. Create a Store
        \r    2. Stock the store
        \r
        \r  List operations:
        \r    1. Create a List
        \r    2. Add to the list
        \r    3. Remove from a list
        """)

def printUserLists():
    global userLists
    aList = userLists.keys()
    count = 1
    if len(aList) != 0:
        print("These are your lists")
        for list in aList:
            print(f"{count}. ",list)
            print(userLists.get(list))
            count += 1
    else:
        print("you dont't have any list yet")

def printUserStores():
    global stores
    count = 1
    aList = stores.keys()
    if len(aList) != 0:
        print("These are your stores")
        for list in aList:
            print(f"{count}. ",list)
            print(stores.get(list))
            count += 1
    else:
        print("you dont't have any store yet")

def check_info(aList,lineNum):
    errorNum = 0
    try:
        first = str(aList[0])
    except:
        print(f"Please make sure the itemname is a string and not a number at line {lineNum}.")
    try:
        second = float(aList[1])
    except:
        print(f"Please make sure that the cost is a decimal number at line {lineNum}.")
    try:
        third = int(aList[2])
    except:
        print(f"Please make sure that the amount is a whole number at line {lineNum}.")
    if errorNum > 0:
        return False
    else:
        return True

def check_storeItems_csv_file(filename, aList):
    lineNum = 2
    try:
        with open(filename) as f:
            csv_reader = reader(f)
            next(csv_reader)
            for line in csv_reader:
                if check_info(line, lineNum):
                    aList.append(line)
                else:
                    return False
                lineNum += 1
            return True
    except:
        print("The file does not exists. Please input a valid file!")

def stockTheStore(storename, filename):
    global stores
    aList = []
    check_storeItems_csv_file(filename, aList)
    for item in aList:
        print(item)
        anItem = Item(item[0],float(item[1]))
        stores.get(storename).addToStock(anItem, int(item[2]))   

def createAStore():
    global stores
    userStoreName = input("Name your list: ")
    userStore = Store(userStoreName.lower())
    if userStore.getName() not in stores:
        stores[userStore.getName()] = userStore
        print(f"The store {userStoreName} has been created")
        dumVar = input("Press enter to continue...")
    else:
        print("There is already a store in this name")
        dumVar = input("Press enter to continue...")

def createShoppingList():
    global userLists
    userListName = input("Name your list: ")
    userList = ShoppingList(userListName)
    if userList.getName() not in userLists:
        userLists[userList.getName()] = userList
        print(f"The list {userListName} has been created")
        dumVar = input("Press enter to continue...")
    else:
        print("you already have this list")
        dumVar = input("Press enter to continue...")

def prmtUserInputAndOperation():
    global stores, userLists
    while True:
        os.system('cls')
        printUserOptions()
        firstInputSet = {'1', '2', '3', '4', 'q'}
        firstUserInput = input("What is your first input: ")
        if firstUserInput in firstInputSet and (firstUserInput == '1' or firstUserInput == '2'):
            while True:
                printUserOptions()
                if firstUserInput == '1':
                    os.system('cls')
                    printUserOptions()
                    secondUserInput = input("Please enter your operation for Store operations: ")
                    if secondUserInput == '1':
                        createAStore()
                        break
                    elif secondUserInput == '2':
                        printUserStores()
                        userStockStore = input("What store do you want to stock? ")
                        userStockFile = input("Give the .csv filename where you want to stock from: ")
                        stockTheStore(userStockStore.lower(), userStockFile)
                        break
                    else:
                        continue
                elif firstUserInput == '2':
                    os.system('cls')
                    printUserOptions()
                    secondUserInput = input("Please enter your operation for List opeartions: ")
                    if secondUserInput == '1':
                        createShoppingList()
                        break
                    elif secondUserInput == '2':
                        return
                    elif secondUserInput == '3':
                        return
                    else:
                        continue
        elif firstUserInput == '3':
            os.system('cls')
            printUserLists()
            dumUserInput = input("Please press ENTER to continue... ")
        elif firstUserInput == '4':
            os.system('cls')
            printUserStores()
            dumUserInput = input("Please press ENTER to continue... ")
        elif firstUserInput == 'q':
            os.system('cls')
            break
        else:
            os.system('cls')
            continue

def main():
    prmtUserInputAndOperation()

if __name__ == '__main__':
    main()