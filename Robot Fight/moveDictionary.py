def moveDictionary():
    electro_shock = {"moveName" : "Electro Shock", \
                     "moveKind" : "atk",\
                     "movePwr" : 15, \
                     "moveAcc" : 95, \
                     "moveCrit" : 80, \
                     "moveTxt" : "releases one thousand volts of static", \
                     "moveIndex" : "electro_shock"}
                     #moveType
                     #special                 
    heal = {"moveName" : "Heal", \
                     "moveKind" : "heal",\
                     "movePwr" : 25, \
                     "moveAcc" : 36, \
                     "moveCrit" : 5, \
                     "moveTxt" : "reattaches itself", \
                    "moveIndex" : "heal"}
    robot_punch = {"moveName" : "Robot Punch", \
                     "moveKind" : "atk",\
                     "movePwr" : 45, \
                     "moveAcc" : 75, \
                     "moveCrit" : 20, \
                     "moveTxt" : "reels back and slugs hard", \
                   "moveIndex" : "robot_punch"}
    robot_slap = {"moveName" : "Robot Slap", \
                     "moveKind" : "atk",\
                     "movePwr" : 32, \
                     "moveAcc" : 90, \
                     "moveCrit" : 20, \
                     "moveTxt" : "slaps a hoe", \
                      "moveIndex" : "robot_slap"}
    robot_headbutt = {"moveName" : "Robot Headbutt", \
                     "moveKind" : "atk",\
                     "movePwr" : 45, \
                     "moveAcc" : 20, \
                     "moveCrit" : 90, \
                     "moveTxt" : "attempts a powerful attack",\
                      "moveIndex" : "robot_headbutt"}
                        #special
    
    moveDic = {"electro_shock" : electro_shock,\
               "heal" : heal, \
               "robot_punch" : robot_punch,\
               "robot_slap" : robot_slap,\
               "robot_slap" : robot_headbutt}
    
    return moveDic

##dictionary = moveDictionary() #module testing
##print(type(dictionary)) #module print test
