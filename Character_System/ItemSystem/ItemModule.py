'''
Created on Jan 21, 2013

This file contains ItemSystemClass class which records serial number
of an item which is used for development of plot. Item also has 
its name, attack point and defend point.

@author: carl
'''
class ItemSystemClass():
    '''
    Class for items
    '''
    # Store SN with name as key
    SNList = {None:None}
    # Store items with SN as key
    ItemList = {None:None}
    # Lock for each object, SN as key, boolean as value
    AvailabilityList = {None:None}
    # TODO: Retrieve object with SN
    def __init__(self, name, SN, Atk, Def):
        '''
        Creates a new item
        @param name: Item name
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
        # Initialize SN list
        ItemSystemClass.SNList.update({self.name:self.SN})
        # Initialize Item list
        ItemSystemClass.ItemList.update({self.SN:self})
        # Initialize Availability list, default: true
        ItemSystemClass.AvailabilityList.update({self.SN:True})
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
    @classmethod
    def retrieveItem(cls, SN):
        '''
        Returns item with SN
        @param SN: Serial number
        @return: The item with SN
        '''
        return cls.ItemList[SN]
    