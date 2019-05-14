#robot battle with updated moveset
#object practice

###things to do:
##balance
##Add more robots and moves
## add move status effects
#add a status check
##add tournament gameplay / game modes
## incorporate speed mechanic to determine who moves first
## add items and overall game


import random
from moveDictionary import *
from robotClass import *

#bot stats creator!
def statGen():
    ranHp = random.randint(325, 375)
    ranAtk = random.randint(12, 18)
    ranDfs = random.randint(5, 12)
    ranSpd = random.randint(3, 6)
    return ranHp, ranAtk, ranDfs#,ranSpd

def initializeRob():
    playerBot = Robot("PlayerBot", 350, 15, 8)
    ranHp, ranAtk, ranDfs = statGen()
    compBot = Robot("ButtBot", ranHp, ranAtk, ranDfs)
    return playerBot, compBot

def main():
    gameIsPlaying = "TRUE"
    while gameIsPlaying:
        playerBot, compBot = initializeRob() #build robots
        moveDic = moveDictionary() #initialize move Dictionary
        battleIntro(playerBot, compBot) #intro text
        turn = "PLAYER" # player always starts
        #turn = determineTurn() #future code spot
        #turn = "COMP" #AI TEST
        #while robots are alive, alternate turns
        while playerBot.getHp() > 0 and compBot.getHp() > 0: #while both robots alive
            if turn == "PLAYER":
                playerTurn(playerBot, compBot, moveDic)#player performs action
                turn = "COMP" #now it's comp's turn
            elif turn == "COMP":
                compTurn(playerBot, compBot, moveDic) #comp does her turn
                turn = "PLAYER" #now it's player's turn
        kill(playerBot, compBot) #game ends if...
        gameIsPlaying = restart() #will the battle continue.....?

#equations
def moveMod():
    #modify damage or heal amount
    rng = random.randint(0, 15) #dmg is modified by up to 15%
    mod = (100 - rng) / 100 #make rng a decimal
##    print("MOVE mod:", mod) # print test
    return float(mod)

def heal(atkr, move): #heal mechanic
    #accuracy check
    checkMiss = checkAccuracy(move['Acc']) #returns y or n
    #crit check
    critResult = checkCrit(move['Crit']) #returns either y or n
    criticalHeal = 1 #set constant

    print(str(atkr.getName()), str(move["Txt"]) + "!") #dialogue
    #resolve miss
    if checkMiss == 'y':
        print(atkr.getName(), "can't find any parts.")#dialogue
        print("They're wide open!!")#dialogue

    else:    
        if critResult == 'y': #critical heal!
            print(atkr.getName(), "finds a crucial system part!")#dialogue
            print(atkr.getName(), "heals for more HP!!")#dialogue
            criticalHeal = 1.5 #change value to critical
            
        #modify amount
        mod = moveMod()
        #health amount equation        
        healAmount = int((atkr.getMAXHP() * (move['Pwr']/100) *\
                          criticalHeal) * mod)
        atkr.healHP(healAmount)

        print(atkr.getName(), "successfully healed.") #dialogue
        print("Heal amount:", healAmount) #print test
        print(str(atkr.getName()) + "'s health:", atkr.getHp()) #print test
        
#damage(moveName, base power, accuracy, crit chance, attacker, defender, effect)
def damage(atkr, dfndr, move): #effect)
    #accuracy check
    checkMiss = checkAccuracy(move['Acc']) #returns either 'y' or 'n'
    #crit check
    critResult = checkCrit(move['Crit']) # this returns either 'y' or 'n'
    print(atkr.getName(), move['Txt'] + "!") #dialogue
    #resolve miss
    if checkMiss == "y": #attack missed dialogue
        dmg = 0 #move deals no damage
         #dialogug
        print("... but", dfndr.getName(), "dodged the attack!")#dialogue
    else:    #attack hits and deals damage
        print("The attack hit!")#dialogue
        mod = moveMod() #damage modifier between 85%-100%

    #resolve crit
        if critResult == 'y': # attack deals critical damage
            print(str(atkr.getName()) + "'s attack deals critical damage!")#dialogue
            critPower = 1.5 # damage will be increased X1.5
        elif critResult == 'n': #attack deals normal damage
            critPower = 1 #damage will not change
            
        #equation
##        noModDamage = int(((atk.attack / dfs.defense) * pwr + 2) * critPower)#
            #print test
        dmg = int((((atkr.getAttack() / dfndr.getDefense()) * \
                    move['Pwr'] + 2) * critPower) * mod)
        print("Damage dealt: " + str(dmg)) # show damage
##        print("Unmodded Damage Dealt: " + str(noModDamage)) #print test
        dfndr.damageHP(dmg)
        
#checks
def checkAccuracy(acc): #checks to see if move hits
    rng = random.randint(1, 100) #generate random #
    if rng >= acc: #if outside accuracy rating, check fails
        checkMiss = "y" # attack missed
##        print("Miss check:", checkMiss) #print test
    else:           #if inside accuracy rating, check succeeds
        checkMiss = "n" # attack hits
##        print("Miss check:", checkMiss) #print test
##    print(rng, ":", acc, '\n') #print test
    return checkMiss #return result

def checkCrit(crit):     #checks if move is a crit
    rng = random.randint(1, 100)    #gen random number  
    if rng <= crit: #if within crit rate, check succeeds
        critical = 'y' #attack was critical, deals CRIT damage
    else: #if outsie crit rate, check fails
        critical = 'n' #normal attack deals 1X damage
##    print("Critical?:", critical) #print test
##    print(rng, ":", crit, '\n') #print test
    return critical #return check result
        
def kill(playerBot, compBot): #either robot is killed...         
    if playerBot.getHp() <= 0: #user death
        playerBot.iDie()
        compBot.iKill()
        print()
        print("You have been defeated!")
        print("I will now use your broken robot's parts to make my robot"\
              " even stronger!")
        
    if compBot.getHp() <= 0: #computer death
        compBot.iDie()
        playerBot.iKill()
        print()
        print("You have defeated me...")
        print("Now how will I impress my one true love?")
        
def restart():
    print("\nWould you like to engage in Robot Mortal Kombat again?") #dialogue
    playAgain = "" #initialize playAgain
    while playAgain != "yes" and playAgain != "no":
        print("Please enter 'yes' or 'no'.") #dialogue
        playAgain = (input(">>>")).lower() #input prompt and force to lower
    if playAgain == "yes": #if wants to play again
        print("Let's do this again!") #dialogue
        print("The staff quickly rebuilds the robots....") #dialogue
        return "TRUE"
    if playAgain == "no": # if doesn't want to keep playing
        print("Thank you for playing.  Now leave me alone.") #dialogue

def printMoveSet():# if asked, dialogue of description of moves
    print("Here are the moves you can choose from:")
    print("\t[ROBOT PUNCH] -- a hard-hitting swing with low accuracy")
    print("\t[ROBOT SLAP] -- a lighter attack with reliable results")
    print("\t[ROBOT HEADBUTT] -- surprise your opponent and maybe he'll be knocked over.")
    #print("This attack might hurt you as well!")
    print("\t[ELECTRO SHOCK] -- short circuit your opponent.\n\t\t\t  Low attack, high crit rate.")
    print("\t[HEAL] -- rebuild yourself with bits from the ground. (~25%hp)")

def getMove():# what will the user choose to do?
    print("Please input the move you wish to make.") #dialogue
    print("For a list of moves, type [MOVESET].") #dialogue
    move = input(">>>").lower() #force input into lowercase
    #print(move)#print test
    return move
        
def playerTurn(playerBot, compBot, moveDic):   #player's turn 
    attacker = playerBot #set actor roles
    defender = compBot #set actor roles
##    print("playerTurn()type(moveDic): ", type(moveDic)) #print test
    print() #spacer
    print(str(playerBot.getName()) + "'s current HP: "\
          + str(playerBot.getHp()) + " / "\
          + str(playerBot.getMAXHP())) #print test
    print(str(compBot.getName()) + "'s current HP: "\
      + str(compBot.getHp()) + " / "\
      + str(compBot.getMAXHP())) #print test
    healthReport(playerBot, compBot) #how are the robs doing?
    inputInvalid = "TRUE" # initialize while variable
    move = getMove() #what will the player do
##    print("playerTurn/move: ", move) #print test
    while inputInvalid == "TRUE": #while user has not input viable move choice
##        print("move:", move) #print test
        if move == "moveset": # if user requests move set
            printMoveSet()  #show user library of moves to choose from
            move = getMove() #request move from user
        elif move in moveDic: #check to see if move exists
            activateAttack(attacker, defender, moveDic[move]) #activate related equation
            inputInvalid = "FALSE" #stop loop
        else: #move not found
            print("ERROR: please input a valid move from [MOVESET]")  #dialogue
            move = getMove() #prompt again for move
            
def compTurn(playerBot, compBot, moveDic): #AI TURN
    atkr = compBot #set actor roles
    dfndr = playerBot #set actor roles
    print("\n***It's the enemy's turn!***\n")#dialogue
    choice = compChooseAttack(compBot) #what will comp do?
    activateAttack(atkr, dfndr, moveDic[choice]) #activate
    
def compChooseAttack(comp):#what will AI do?
    if comp.getHp() >= .9 * comp.getMAXHP():  #if comp is high health
        choice = 'robot slap' #ROBOT SLAP
    elif comp.getHp() >= .7 * comp.getMAXHP(): # if comp medium high health
        choiceList = ('robot punch', 'robot slap', 'electro shock')
        choice = random.choice(choiceList)
    elif comp.getHp() >= .5 * comp.getMAXHP():#if comp is medium health
        choiceList = ('robot punch', 'robot slap', 'electro shock', 'heal')
        choice = random.choice(choiceList) #any move
    elif comp.getHp() >= .1 * comp.getMAXHP(): # if near death
        choiceList = ('robot punch', 'heal')
        choice = random.choice(choiceList) # go out swinging or heal
    elif comp.getHp() > 0:
        choice = 'robot punch' # go out swinging
    return choice

def healthReport(rob1, rob2):
    if rob2.getHp() > .85 * rob2.getMAXHP():
        print("Your opponent looks healthy.\n") #dialogue
    elif rob2.getHp() > .50 * rob2.getMAXHP():
        print("Your oppenent looks like it has suffered some damage.")#dialogue
        print("But She's still ready to fight!\n")#dialogue
    elif rob2.getHp() > .25 * rob2.getMAXHP():
        print("Your opponent looks unsteady. She may be dead soon!\n") #dialogue
    else:
        print("Your oppenent is quite wounded.\n")#dialogue
        print("Finish her!")#dialogue
    print("-----------------------------------------------")
    print("What will you do?")    #dialogue

def getPlayerBotName(playerBot):
    likesName = 'n' #initialize while loop
    while likesName == "n": #while the player likes the name
        print("What would you like to name your robot?")
        newName = input(">>>")
        playerBot.setName(newName)
        print("Your robot's new name is", playerBot.getName())
        print("Do you like this name?  [y] or [n]")
        likesName = (input(">>>")).lower()
        #print(likesName) #print test
                
def battleIntro(playerBot, compBot):
    print("Welcome to Robot Battle 5000!")
    print("If you would like to edit your robot, type [EDITBOT]")
    print("Or press [ENTER] to continue")
    choice = (input(">>>")).lower()
    if choice == "editbot":
        getPlayerBotName(playerBot)
    print("Enemy robot's stats are:", compBot.getStats())
    print("Your robot's stats are:", playerBot.getStats())   
    print("\nAnnouncer: Let the Battle BEGINNNNNN!\n") #dialogue

#do the thing        
main() #main(playerBot, compBot) alt
