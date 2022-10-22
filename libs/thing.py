from argparse import ArgumentTypeError

class Thing:
    __name = ""

    def isValidArgType(self, userInput, destype):
        userInputType = type(userInput)
        userInputType = str(userInputType).split(" ")[1][0:-1]
        if userInputType != destype:
            raise ArgumentTypeError
        elif userInputType == "'str'" and userInput.isnumeric():
            raise ArgumentTypeError
        else:
            return True

    def __init__(self, name):
        if self.isValidArgType(name, "'str'"):
            self.__name = name
    
    def getName(self):
        return self.__name

    