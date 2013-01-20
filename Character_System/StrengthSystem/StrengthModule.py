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
        self.Maximum = MaxSP
    
    #TODO: weaken
    #TODO: recover
    #TODO: ChangeMaximum
    #TODO: actMulti