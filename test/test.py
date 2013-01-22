'''
Created on Jan 22, 2013
Temp file for testing
@author: carl
'''
from CharacterModule import Character



def printData():
    print("Adam HP: ",Adam.health.getHP())
    print("MP: ", Adam.spirit.get())
    print("SP: ", Adam.strength.get())
    print("SP max: ", Adam.strength.getMax())
    print("Action multiplier: ", Adam.strength.getActMulti())
    print("Adam is alive: ", Adam.health.alive())
    
if __name__ == '__main__':
    pass
    Adam = Character("Adam", 100, 100, 100, 10, 10, 1.0, 1.0)
    printData()
    Adam.health.hurt(20)
    Adam.strength.autoSetMax(Adam.health.getHP(), Adam.health.getMax())
    Adam.strength.autoSetActMulti()
    printData()