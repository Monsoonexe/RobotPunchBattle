#robot battle with updated moveset
#object practice

###things to do:
##balance
##Add more robots and moves
## add move status effects
#add a status check
##add tournament gameplay / game modes
##add move dialogue
##split attacks and heal into separate move types
    #have prog test for which type and activate respectively
## toggle print tests in-game
## incorporate speed mechanic to determine who moves first
## fix computer heal mechanic

import random
from moveDictionary import *

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
        
#bot stats creator!
def statGen():
    ranHp = random.randint(250, 301)
    ranAtk = random.randint(12, 19)
    ranDfs = random.randint(5, 12)
    ranSpd = random.randint(3, 6)
    return ranHp, ranAtk, ranDfs#,ranSpd

def initializeRob():
    robot1 = Robot("PlayerBot", 275, 15, 8)
    ranHp, ranAtk, ranDfs = statGen()
    robot2 = Robot("ButtBot", ranHp, ranAtk, ranDfs)
    return robot1, robot2
        
###move stats CONSTANTS
##def initializeMoveSet(): #alphabetized list of moves and stats
##    #Var name = ["move name", base power, accuracy, crit chance]\
##    #effect, type, battle text
##    #name = name[0], basePower[1], acc[2], crit[3] 
##    ELECTRO_SHOCK = ["Electro Shock", 18, 99, 80]
##    HEAL = ["Heal", 25, 36, 5]    
##    ROBOT_PUNCH = ["Robot Punch", 45, 75, 20]
##    ROBOT_SLAP = ["Robot Slap", 32, 90, 20]
##    ROBOT_HEADBUTT = ["Robot Headbutt", 45, 50, 1]
##    
##    #moveset list
##    MOVESET = [ELECTRO_SHOCK, HEAL, ROBOT_PUNCH, ROBOT_SLAP, ROBOT_HEADBUTT]
###   print(MOVESET) #PRINT TEST
##    return MOVESET
##
##def initializeMoveSetString(): #contains string version of func(MOVESET)
##    MOVESTRING = ["electro shock", "heal", "robot punch", "robot slap",\
##                  "robot headbutt"]
###   print(MOVESTRING) # print test
##    return MOVESTRING
##    
##def findMove(MOVESTRING, move): #used to search for index of chosen move
##    index = MOVESTRING.index(move)#index is found
##    return index #returned

def main():
    playAgain = "yes"
    while playAgain == 'yes':
        robot1, robot2 = initializeRob() #build robots
        moveDic = moveDictionary() #initialize move Dictionary
##        print("main()type(moveDic): ", type(moveDic)) #print test
        #print(moveDic) #print test
        MOVESET = initializeMoveSet() #initialize function
        MOVESTRING = initializeMoveSetString() #initialize function
        input("Hit [ENTER] when ready. \n>>>")
        battleIntro(robot1, robot2) #intro text
        turn = "PLAYER" # player always starts
        #turn = determineTurn() #future code spot
        #turn = "COMP" #AI TEST
        #while robots are alive, alternate turns
        while robot1.hp > 0 and robot2.hp > 0: #while both robots alive
            if turn == "PLAYER":
                playerTurn(robot1, robot2, moveDic)#player performs action
                turn = "COMP" #now it's comp's turn
            elif turn == "COMP":
                compTurn(robot1, robot2, MOVESET, MOVESTRING) #comp does her turn
                turn = "PLAYER" #now it's player's turn
        kill(robot1, robot2) #game ends if...
        playAgain = restart() #will the battle continue.....?

#equations
def moveMod():
    #modify damage or heal amount
    rng = random.randint(0, 16) #dmg is modified by up to 15%
    mod = (100 - rng) / 100 #make rng a decimal
    print("MOVE mod:", mod) # print test
    return float(mod)

def heal(moveName, power, acc, crit, atkr): #heal mechanic
    #accuracy check
    checkMiss = checkAccuracy(acc) #returns y or n
    #crit check
    critResult = checkCrit(crit) #returns either y or n
    criticalHeal = 1 #set constant

    print(atkr.name, "is attempting to put itslef back together.") #dialogue
    #resolve miss
    if checkMiss == 'y':
        print(atkr.name, "can't find any parts.")#dialogue
        print("They're wide open!!")#dialogue

    else:    
        if critResult == 'y': #critical heal!
            print(atkr.name, "finds a crucial system part!")#dialogue
            print(atkr.name, "heals for more HP!!")#dialogue
            criticalHeal = 1.5 #change value to critical
            
        #modify amount
        mod = moveMod()
        #health amount equation        
        healAmount = int((atkr.MAXHP * (power/100) * criticalHeal) * mod)
        atkr.healHP(healAmount)


#damage(moveName, base power, accuracy, crit chance, attacker, defender, effect)
def damage(atkr, dfndr, move): #effect)
    #accuracy check
    checkMiss = checkAccuracy(move['moveAcc']) #returns either 'y' or 'n'
    #crit check
    critResult = checkCrit(move['moveCrit']) # this returns either 'y' or 'n'
    
    #resolve miss
    if checkMiss == "y": #attack missed dialogue
        dmg = 0 #move deals no damage
        print(atkr.name, "used" + move['moveName'] + "!") #dialogue
        print("... but", dfndr.name, "dodged the attack!")#dialogue
    else:    #attack hits and deals damage
        print(atkr.name, "used", move['moveName'] + "!")#dialogue
        print("The attack hit!")#dialogue
        mod = moveMod() #damage modifier between 85%-100%

    #resolve crit
        if critResult == 'y': # attack deals critical damage
            print(str(atkr.name) + "'s attack deals critical damage!")#dialogue
            critPower = 1.5 # damage will be increased X1.5
        elif critResult == 'n': #attack deals normal damage
            critPower = 1 #damage will not change
            
        #equation
##        noModDamage = int(((atk.attack / dfs.defense) * pwr + 2) * critPower)#
            #print test
        dmg = int((((atkr.attack / dfndr.defense) * pwr + 2) * critPower) * mod)
        print("Modded Damage dealt: " + str(dmg)) # show damage
##        print("Unmodded Damage Dealt: " + str(noModDamage)) #print test
        dfndr.damageHP(dmg)
        
        
#checks
def checkAccuracy(acc): #checks to see if move hits
    rng = random.randint(1, 10) #generate random #
    if rng >= acc: #if outside accuracy rating, check fails
        checkMiss = "y" # attack missed
        print("Miss check:", checkMiss) #print test
    else:           #if inside accuracy rating, check succeeds
        checkMiss = "n" # attack hits
        print("Miss check:", checkMiss) #print test
    print(rng, ":", acc, '\n') #print test
    return checkMiss #return result

def checkCrit(crit):     #checks if move is a crit
    rng = random.randint(1, 10)    #gen random number  
    if rng <= crit: #if within crit rate, check succeeds
        critical = 'y' #attack was critical, deals CRIT damage
    else: #if outsie crit rate, check fails
        critical = 'n' #normal attack deals 1X damage
    print("Critical?:", critical) #print test
    print(rng, ":", crit, '\n') #print test
    return critical #return check result
        
def kill(robot1, robot2): #either robot is killed...         
    if robot1.hp <= 0: #user death
        robot1.iDie()
        robot2.iKill()
        print()
        print("You have been defeated!")
        print("I will now use your broken robot's parts to make my robot"\
              "even stronger!")
        
    if robot2.hp <= 0: #computer death
        robot2.iDie()
        robot1.iKill()
        print()
        print("You have defeated me...")
        print("Now how will I impress my one true love?")
        
def restart():
    print("\nWould you like to engage in Robot Mortal Kombat again?")
    print("Please enter 'yes' or 'no'")
    playAgain = input(">>>")
    playAgain = playAgain.lower()
    while playAgain != "yes" and playAgain != "no":
        print("Please input only 'yes' or 'no'.")
        playAgain = input(">>>")
        playAgain = playAgain.lower()

    if playAgain == "yes":
        print("Let's do this again!") #dialogue
        print("The staff quickly rebuilds the robots....") #dialogue
        return playAgain
    if playAgain == "no":
        print("Thank you for playing.  Now leave me alone.")

def printMoveSet():# if asked, dialogue of description of moves
    print("Here are the moves you can choose from:")
    print("\t[ROBOT PUNCH] -- a hard-hitting swing with low accuracy")
    print("\t[ROBOT SLAP] -- a lighter attack with reliable results")
    print("\t[ROBOT HEADBUTT] -- surprise your opponent and maybe he'll be knocked over.")
    #print("This attack might hurt you as well!")
    print("\t[ELECTRO SHOCK] -- short circuit your.  Low attack, high crit rate.")
    print("\t[HEAL] -- rebuild yourself with bits from the ground. (~25%hp)")

def getMove():# what will the user choose to do?
    print("Please input the move you wish to make.") #dialogue
    print("For a list of moves, type [MOVESET].") #dialogue
    move = input(">>>") #user prompt
    move = move.lower() #force input into lowercase
    #print(move)#print test
    return move

def moveValidation(moveDic, moveName): #is the user retarded?
##    print(moveName) #print test
##    print("moveValidation type(moveDic check: ", type(moveDic)) #print test
    if moveName in moveDic:
        found = 'y'
        playerAction = moveName
    else:
        found = 'n'
        playerAction = 'n'
##    for key in range(len(moveDic)): #how many items in list?
##        print(moveDic[key]) #print test
##        if moveDic[key] == moveName:  #search for move in moveDictionary
##            found = 'y'
    return found, moveName
        
def activateAttack(atkr, dfndr, move): # finds the move and calls damage
    if move["moveKind"] == 'atk':
        damage()
    if move["moveKind"] == 'heal':
        heal()
    
def playerTurn(robot1, robot2, moveDic):   #player's turn 
    attacker = robot1 #set actor roles
    defender = robot2 #set actor roles
##    print("playerTurn()type(moveDic): ", type(moveDic)) #print test
    print("Your robot's current HP: " + str(robot1.hp) + " / " + str(robot1.MAXHP))
    healthReport(robot1, robot2)
    inputInvalid = "TRUE" # initialize while variable
    move = getMove() #what will the player do
    print("playerTurn/move: ", move) #print test
    while inputInvalid == "TRUE": #while user has not input viable move choice
        while move == "moveset": # if user requests move set
            printMoveSet()  #show user library of moves to choose from
            move = getMove() #request move from user
            if move in moveDic[move['moveIndex']]:
                activateAttack(attacker, defender, moveDic[move])
            
##        validMove, playerAction = moveValidation(moveDic, move) #check if move is valid
##        print("validMove = ", validMove) #print test
##        if validMove == 'y':#input validation
##            action = moveDic[playerAction]['moveIndex']                       
##            activateAttack(action, attacker, defender) #activate              
##            inputInvalid = "FALSE" #clear invalid loop
##        if validMove == 'n':#input validation
##            print("[ERROR]: Please enter only name of the [MOVE].")#dialogue
##            move = getMove()  #ask user for input again

def compTurn(robot1, robot2, MOVESET, MOVESTRING): #AI TURN
    atkr = robot2 #set actor roles
    dfndr = robot1#set actor roles
    print("\nIt's the enemy's turn!\n")#dialogue
    choice = compChooseAttack(MOVESET, robot2) #what will comp do?
    activateAttack(MOVESET, MOVESET[choice], atkr, dfndr) #activate
    
def compChooseAttack(MOVESET, comp):#what will AI do?    
    if comp.hp >= .9 * comp.MAXHP:  #if comp is high health
        choice = 3 #ROBOT SLAP
    elif comp.hp >= .7 * comp.MAXHP: # if comp medium high health
        option = random.randint(0, 4)
        choice = option
    elif comp.hp >= .5 * comp.MAXHP:#if comp is medium health
        choice = random.randint(0, 4) #any move
    elif comp.hp >= .1 * comp.MAXHP: # if near death
        choice = random.randint(0, 2) # robot punch
    elif comp.hp > 0:
        choice = 2
    return choice

def healthReport(rob1, rob2):
    if rob2.hp > .85 * rob2.MAXHP:
        print("Your opponent looks healthy.\n") #dialogue
    elif rob2.hp > .50 * rob2.MAXHP:
        print("Your oppenent looks like it has suffered some damage.")#dialogue
        print("But She's still ready to fight!\n")#dialogue
    elif rob2.hp > .25 * rob2.MAXHP:
        print("Your opponent looks unsteady. She may be dead soon!\n") #dialogue
    else:
        print("Your oppenent is quite wounded.\n")#dialogue
        print("Finish her!")#dialogue
    print("What will you do?")    #dialogue

def battleIntro(robot1, robot2):
    print("Enemy robot's stats are:", robot2.name, robot2.hp, robot2.attack,\
          robot2.defense)
    print("Your robot's stats are:", robot1.name, robot1.hp, robot1.attack,\
          robot1.defense)   
    print("\nAnnouncer: Let the Battle BEGINNNNNN!\n") #dialogue
        
main() #do the thing that you do
