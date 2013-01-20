'''
Created on Jan 20, 2013

SpiritSystem class is the Spirit System. This system records the
MP of character. When MP decreases, certain types of 
operations will be affected. Also, the remaining MP when
died will affect type of spirit of character, which 
directly affects the ranking of ending.

@author: carl
'''

class SpiritSystem():
    '''
    Spirit system(MP) class
    '''


    def __init__(self, MaxMP):
        '''
        Constructor: Creates a new MP system.
        @param MaxMP: The maximum MP
        '''
        # Set maximum MP
        self.Maximum = int(MaxMP)
        # Initialize current MP
        self.currentMP = self.Maximum
    #TODO: get
    def get(self):
        '''Returns current MP'''
        return self.currentMP
    #TODO: hurt
    def hurt(self, damage):
        '''
        Decreases MP by damage, returns if still alive
        @param damage: Amount of damage
        @return: If alive, return true
        '''
        self.currentMP -= damage
        return self.currentMP > 0
    #TODO: decrease rates
    #TODO: recover
    #TODO: critical points
    