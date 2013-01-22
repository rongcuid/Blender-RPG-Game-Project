'''
Created on Jan 19, 2013

StrengthSystem class is for Strength System. There is a maximum strength
which decreases with solid health decreases. Strength also recovers
automatically. When pills are taken, decrease rate decreases and 
recover rate increases. Different strength gives a different act 
multiplier that will be multiplied to many attributes such as attack
and defense

@author: carl
'''

class StrengthSystem():
    '''

    '''


    def __init__(self, MaxSP):
        '''
        Constructor: Creates a new strength system.
        @param MaxSP: Maximum strength point
        '''
        # Initialize Max SP with cast
        self.Maximum = float(MaxSP)
        # Initialize current max SP
        self.currentMax = Maximum
        # Initialize current SP
        self.currentSP = Maximum
        # Initialize action multiplier
        self.actMulti = 1.0
    
    def get(self):
        '''
        Get SP
        '''
        return self.currentSP
    
    def getMax(self):
        '''
        Get current max SP
        '''
        return self.currentMax
    
    def weaken(self, damage):
        '''
        Weaken strength by damage, return if still able to move
        @return: If strength > 0, return true
        '''
        self.currentSP -= damage
        return self.currentSP > 0
    
    def recover(self, recovery):
        '''
        Recover strength by recovery, if more than current max, set to max
        '''
        self.currentSP += recovery
        if self.currentSP > self.currentMax:
            self.currentSP = self.currentMax
    
    def setMax(self, newMax):
        '''
        Set current Max to newMax.
        '''
        self.currentMax = newMax
    
    def getActMulti(self):
        '''
        Gets action multiplier. If current max > max, return 1.0
        '''
        if self.currentMax < self.Maximum:
            return self.currentMax / self.Maximum
        else:
            return 1.0