'''
Created on Feb 20, 2013

@author: carl
'''
from Character_System import *
from CharacterSystem.CharacterModule import Character
from ItemSystem.ItemModule import ItemSystemClass
from OperationSystem.OperationModule import OperationSystemClass
def showHP(Character):
    print("===")
    print(Character, " solid HP ", Character.health.getHP())
    print(Character," Dynamic HP ", Character.health.getDyn())
    print("===")
if __name__ == '__main__':
    XiaoMing = Character("Xiaoming", 2001, 100,
                                    100, 100, 10, 10, 1.0, 1.0)
    knife = ItemSystemClass("knife", 123, 20, 10)
    fist = ItemSystemClass("fist", 124, 10, 10)
    XiaoMing.storage.add(knife.getSN())
    showHP(XiaoMing)
    XiaoHong = Character("Xiao Hong", 2002, 
                         80, 80, 90,
                         10, 10, 1.0, 1.0)
    showHP(XiaoHong)
    OperationSystemClass.attackLowLevel(XiaoMing, XiaoHong, knife, fist)
    showHP(XiaoHong)
    OperationSystemClass.attack(2001, 2002, 123, 124)
    showHP(XiaoHong)
    pass