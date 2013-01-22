'''
Created on Jan 20, 2013

SpiritSystem class is the Spirit System. This system records the
MP of character. When MP decreases, certain types of 
operations will be affected. Also, the remaining MP when
died will affect type of spirit of character, which 
directly affects the ranking of ending.

@author: carl
'''

# Import constants
from MPSystemConstants import *

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
        # Initialize current MP, also add type cast
        self.currentMP = float(self.Maximum)

    def get(self):
        '''Returns current MP'''
        return self.currentMP

    def hurt(self, damage):
        '''
        Decreases MP by damage, returns if still alive
        @param damage: Amount of damage
        @return: If alive, return true
        '''
        self.currentMP -= damage
        return self.currentMP > 0
    
    def recover(self, recovery):
        '''
        Increase MP by recovery up to a certain limit.
        @param recovery: Amount of recovery
        '''
        # Maximum amount of recovery
        MaxAfterRecovery = (MP_RECOVERY_RATIO * 
                            (self.Maximum - self.currentMP) 
                            + self.currentMP)
        self.currentMP += recovery
        # If current MP larger than maximum, set to maximum.
        if self.currentMP > MaxAfterRecovery:
            self.currentMP = MaxAfterRecovery

    
