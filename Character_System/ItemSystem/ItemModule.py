'''
Created on Jan 21, 2013

This file contains ItemSystem class which records serial number
of an item which is used for development of plot. Item also has 
its name, attack point and defend point.

@author: carl
'''

class ItemSystem():
    '''
    Class for items
    '''


    def __init__(self, name, SN, Atk, Def):
        '''
        Creates a new item
        @param SN: Serial number
        @param Atk: Item attack
        @param Def: Item defense
        '''
        # Initialize name
        self.name = str(name)
        # Initialize serial number
        self.SN = int(SN)
        # Initialize attack
        self.Attack = int(Atk)
        # Initialize defense
        self.Defense = int(Def)
    def __str__(self):
        '''
        Prints item name
        '''
        return self.name
    
    def getSN(self):
        '''
        Returns item SN
        '''
        return self.SN
    
    def getAttack(self):
        '''
        Returns attack
        '''
        return self.Attack
    
    def getDefense(self):
        '''
        Returns defense
        '''
        return self.Defense
    