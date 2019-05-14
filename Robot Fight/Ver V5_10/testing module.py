#testing module
from robotClass import *
from itemmodule import *
from robot_battle_test import *
playerBot, compBot = initializeRob() #build robots
moveDic = moveDictionary() #build move dictionary
itemDic = itemDictionary() #build item dictionary

activateItem(itemDic["grenade"], playerBot, compBot)
