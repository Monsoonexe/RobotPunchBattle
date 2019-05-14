#bitches love robots!
class Robot:
    def __init__(self, name, hp, attack, defense):
        self.__name = name
        self.__MAXHP = hp
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        
    def iDie(self):
        print(self.__name, ": NNOOOooooOOOOoOOOOo! I am become death :(")

    def iKill(self):
        print(self.__name, ": I have bested you in Mortal Robot Combat! :D")

    def healHP(self, healAmount):
        #determine heal amount
        if(healAmount in {"full", "max", "all"})
            self.__hp = self.__MAXHP
        if self.__hp + healAmount >= self.__MAXHP: # hp can only go up to MAX HP
            self.__hp = self.__MAXHP #if more, hp = maxhp
        else: #if not
            self.__hp += healAmount #add health to hp

    def damageHP(self, damageAmount):
        self.__hp -= damageAmount #update defender's current HP
        if self.__hp <= 0:
            self.__hp = 0
       #mutators 
    def setName(self, newName):
        self.__name = newName
    def setAttack(self, amount):
        self.__attack = amount
    def setDefense(self, amount):
        self.__defense = amount
    def setMAXHP(self, amount):
        self.__MAXHP = amount
        #fetchers
    def getAttack(self):
        return int(self.__attack)
    def getDefense(self):
        return int(self.__defense)
    def getHp(self):
        return int(self.__hp)
    def getName(self):
        return str(self.__name)
    def getStats(self):
        return str(self.__name), int(self.__MAXHP),\
               int(self.__attack), int(self.__defense)
    def getMAXHP(self):
        return int(self.__MAXHP)
