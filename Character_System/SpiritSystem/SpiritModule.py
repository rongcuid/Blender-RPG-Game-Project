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
# TODO: constants

    def __init__(self, MaxMP):
        '''
        Constructor: Creates a new MP system.
        @param MaxMP: The maximum MP
        '''
        # Set maximum MP
        self.Maximum = int(MaxMP)
        # Initialize current MP
        self.currentMP = self.Maximum

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
        # TODO: Constant for recovery
        # Maximum amount of recovery is 80% of total damage
        MaxAfterRecovery = (0.8 * (self.Maximum - self.currentMP) 
                            + self.currentMP)
        self.currentMP += recovery
        # If current MP larger than maximum, set to maximum.
        if self.currentMP > MaxAfterRecovery:
            self.currentMP = MaxAfterRecovery

    