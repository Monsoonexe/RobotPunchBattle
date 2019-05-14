def moveDictionary():
    electro_shock = {"Name" : "Electro Shock", \
                     "Kind" : "atk",\
                     "Pwr" : 15, \
                     "Acc" : 95, \
                     "Crit" : 80, \
                     "Txt" : "releases one thousand volts of static"}
                     #special                 
    heal =          {"Name" : "Heal", \
                     "Kind" : "heal",\
                     "Pwr" : 28, \
                     "Acc" : 36, \
                     "Crit" : 5, \
                     "Txt" : "reattaches itself"}
    robot_punch =   {"Name" : "Robot Punch", \
                     "Kind" : "atk",\
                     "Pwr" : 40, \
                     "Acc" : 70, \
                     "Crit" : 20, \
                     "Txt" : "reels back and slugs hard"}
    robot_slap =    {"Name" : "Robot Slap", \
                     "Kind" : "atk",\
                     "Pwr" : 32, \
                     "Acc" : 90, \
                     "Crit" : 20, \
                     "Txt" : "slaps a hoe"}
    robot_headbutt = {"Name" : "Robot Headbutt", \
                     "Kind" : "atk",\
                     "Pwr" : 45, \
                     "Acc" : 20, \
                     "Crit" : 80, \
                     "Txt" : "attempts a powerful attack"}
                        #special
    
    moveDic = {"electro_shock" : electro_shock,\
               "heal" : heal, \
               "robot_punch" : robot_punch,\
               "robot_slap" : robot_slap,\
               "robot_headbutt" : robot_headbutt}
    
    return moveDic

##dictionary = moveDictionary() #module testing
##print(type(dictionary)) #module print test
