#bitches love robots!
class Robot:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.MAXHP = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        
    def iDie(self):
        print(self.name, ": NNOOOooooOOOOoOOOOo! I am become death :(")

    def iKill(self):
        print(self.name, ": I have bested you in Mortal Robot Combat! :D")

    def healHP(self, healAmount):
        #determine heal amount
        if self.hp + healAmount >= self.MAXHP: # hp can only go up to MAX HP
            self.hp = self.MAXHP #if more, hp = maxhp
        elif self.hp + healAmount < self.MAXHP: #if not
            self.hp += healAmount #add health to hp
        print(self.name, "successfully healed.")
        print("Heal amount:", healAmount) #print test
        print(str(self.name) + "'s health:", self.hp) #print test

    def damageHP(self, damageAmount):
        self.hp -= damageAmount #update defender's current HP
        if self.hp <= 0:
            self.hp = 0
        print(str(self.name) + "'s current HP:", self.hp) #show defender's current HP
        
    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def getStats(self):
        return self.name, self.MAXHP, self.attack, self.defense

    def getCurrentHP(self):
        return self.hp

    def getMAXHP(self):
        return self.MAXHP
