# main module
#imports
from itemmodule import *
from moveDictionary import *
from robotClass import *


def main():
    initializeGame()
    gameIntro()

def gameIntro():
    print("Hello there!  Welcome to the exciting world",
          "of ROBOT BATTLE 5000!!!")
    print("Your job is to build a robot and murder other people's robots!")
    print("Robots don't have feelings, so murder is okay in this case.")
    print("Here, why don't I give you a start-up Robot?")
    print(PLAYER.getName(), "recieved [STARTER ROBOT]")
    print("Eh?", PLAYER.getName(), "?  What's up with that?  Oh right!")
    print("I forgot to ask you for your name.")
    print("Whenever you see three 'greater than' symbols, it means you",\
          "need to enter something.")
    
    

def initializeGame():

main()
