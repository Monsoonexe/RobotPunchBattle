#item module

from random import *

def itemDictionary():
    wrench = {"Name" : "Wrench", \
              "Kind" : "restore",\
              "Pwr" : 20,\
              "Price" : 250}

    blowtorch =  {"Name" : "blowtorch", \
                  "Kind" : "restore",\
                  "Pwr" : 50,\
                  "Price" : 600}

    uber_potion = {"Name" : "Uber Potion", \
                   "Kind" : "restore",\
                   "Pwr" : 150,\
                   "Price" : 2000}

    grenade = {"Name" : "Uber Potion", \
               "Kind" : "damage",\
               "Pwr" : 35,\
               "Price" : 475}

    firmware_upgrade = {"Name" : "Firmware Upgrade",\
                        "Kind" : "upgrade",\
                        "Type" : "MAXHP",\
                        "Pwr" : 1,\
                        "Price" : "1000"}

    power_upgrade = {"Name" : "Power Upgrade",\
                     "Kind" : "upgrade",\
                     "Type" : "attack",\
                     "Pwr" : 1,\
                     "Price" : "1000"}
    
    defense_upgrade = {"Name" : "Defense Upgrade",\
                       "Kind" : "upgrade",\
                       "Type" : "defense",\
                       "Pwr" : 1,\
                       "Price" : "1000"}    
    
    itemDic = {"wrench" : wrench,\
               "blowtorch" : blowtorch,\
               "uber_potion" : uber_potion,\
               "grenade" : grenade,\
               "firmware_upgrade" : firmware_upgrade,\
               "power_upgrade" : power_upgrade,\
               "defense_upgrade" : defense_upgrade}
    
    return itemDic

def activateItem(item, atkr, dfndr):
    if item["Kind"] == "restore":
        restoreItem(item, atkr)
    elif item["Kind"] == "damage":
        damageItem(item, atkr, dfndr)
    elif item["Kind"] == "upgrade":
        upgradeItem(item, atkr)

def aOrAn(name):
    name = tuple(name.lower())
    if name[0] in ("a", "e", "i", "o", "u"):
        return "an"
    else:
        return "a"

def restoreItem(item, user):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue

def damageItem(item, user, dfndr):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue

def upgradeItem(item, user):
    print(user.getName(), "used", aOrAn(item["Name"]), item["Name"]) #dialogue
    if item["Type"] == "attack":
        user.getAttack
    elif item["Type"] == "defense":
    elif item["Type"] == "MAXHP":
    
#####test functions
##itemDic = itemDictionary()
##activateItem(itemDic["grenade"])
