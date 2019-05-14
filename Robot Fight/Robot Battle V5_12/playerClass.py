#bitches love players
class Player:
    def __init__(self):
        self.__name = "Player Name"
        self.__level = 1
        self.__party = []

    def getName(self):
        return self.__name
    def getLevel(self):
        return self.__level
    def getBackpack(self):
        return self.__backpack
    def getParty(self):
        return self.__party

    def setName(self, newName):
        self.__name = newName
    def setLevel(self, newLevel):
        self.__level = newLevel

    def addToParty(self, addition):
        self.__party
        
    def levelUp(self):
        self.__level += 1

