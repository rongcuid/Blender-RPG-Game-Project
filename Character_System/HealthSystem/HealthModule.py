'''
Created on Jan 19, 2013

HealthSystem class is the health point calculation system. It includes
maximum health for each character, the solid and dynamic HP(Solid
HP does not change if it is higher than critical point 2 and lower than 
critical point 1, but 
dynamic health drops regardless the total point is). Operation to
hurt and recover, the function to get health. Critical points(CP) marks
different behaviour of health: above CP1 solid health recovers automatically
, between CP1 and 2 health remains same; between 2 and 3 health drops
at rate 1; below 3 health drops at rate 2.

@author: carl
'''

from HPSystemConstants import *

class HealthSystem:
    '''Health System main class'''
    

    def __init__(self, MaxHP):
        '''
        Constructor: Creates a new health system
        @param MaxHP: The maximum HP
        '''
        # Initialize maximum HP
        self.Maximum = int(MaxHP)
        # Initialize current HP, with type cast
        self.currentHP = float(MaxHP)
        # Initialize dynamic HP, float type
        self.currentDynHP = 0.0
        
    def getHP(self):
        '''
        Returns current solid HP
        '''
        return self.currentHP
    
    def getDyn(self):
        '''
        Returns current dynamic HP
        '''
        return self.currentDynHP
    
    def getMax(self):
        '''
        Returns max HP
        '''
        return self.Maximum
    
    def hurt(self, damage):
        '''
        Decreases total HP by damage which is pre-calculated.
        @return: Return true if character is still alive.
        '''
        self.currentDynHP -= damage
        if self.currentDynHP < 0:
            # Subtract the excess damage on dynamic HP from solid HP
            self.currentHP += self.currentDynHP
            self.currentDynHP = 0
        # Return true if still alive
        return self.currentHP > 0
    
    def recover(self, recovery):
        '''
        Increase dynamic HP by recovery which is pre-calculated.
        ''' 
        # Maximum HP after recovery, which is
        # current solid HP + 80% of total solid HP damage
        MaxAfterRecovery = (self.currentHP + 
                            (self.Maximum - self.currentHP) * HP_RECOVERY_RATIO)
        self.currentDynHP += recovery
        # If recovery is more than allowed, dynamic HP is set to
        # the difference between MaxAfterRecovery - current solid HP
        if self.currentDynHP > MaxAfterRecovery:
            self.currentDynHP = MaxAfterRecovery - self.currentHP
    
    def alive(self):
        '''
        If alive, return true
        '''
        return self.currentHP > 0
        
        
