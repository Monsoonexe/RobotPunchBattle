def moveDictionary():
    electro_shock = {"moveName" : "Electro Shock", \
                     "moveKind" : "atk",\
                     "movePwr" : 15, \
                     "moveAcc" : 95, \
                     "moveCrit" : 80, \
                     "moveTxt" : "releases one thousand volts of static"}
                     #moveType
                     #special                 
    heal = {"moveName" : "Heal", \
                     "moveKind" : "heal",\
                     "movePwr" : 28, \
                     "moveAcc" : 36, \
                     "moveCrit" : 5, \
                     "moveTxt" : "reattaches itself"}
    robot_punch = {"moveName" : "Robot Punch", \
                     "moveKind" : "atk",\
                     "movePwr" : 40, \
                     "moveAcc" : 70, \
                     "moveCrit" : 20, \
                     "moveTxt" : "reels back and slugs hard"}
    robot_slap = {"moveName" : "Robot Slap", \
                     "moveKind" : "atk",\
                     "movePwr" : 32, \
                     "moveAcc" : 90, \
                     "moveCrit" : 20, \
                     "moveTxt" : "slaps a hoe"}
    robot_headbutt = {"moveName" : "Robot Headbutt", \
                     "moveKind" : "atk",\
                     "movePwr" : 45, \
                     "moveAcc" : 20, \
                     "moveCrit" : 80, \
                     "moveTxt" : "attempts a powerful attack"}
                        #special
    
    moveDic = {"electro_shock" : electro_shock,\
               "heal" : heal, \
               "robot_punch" : robot_punch,\
               "robot_slap" : robot_slap,\
               "robot_headbutt" : robot_headbutt}
    
    return moveDic

##dictionary = moveDictionary() #module testing
##print(type(dictionary)) #module print test
