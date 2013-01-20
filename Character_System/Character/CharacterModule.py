'''
Character class is for characters a rpg game will use. It 
includes an elaborate system of health point(HP), strength
point(SP), spiritual point(MP), and weapon system (WP). The
tyoes included are game points, eg. health point; multiplication
points, eg. attack multiplication point; status, eg. death flag;
operation, eg. attack. This class links to other classes
including Health Point Module, Strenth Point Module, Weapons 
Module, and Spiritual Point Module.
@author: carl
'''
from HealthModule import HealthSystem
from StrengthModule import StrengthSystem
from SpiritModule import SpiritSystem
from WeaponModule import WeaponSystem

class Character:
    '''
    The meta class for character managing
    '''


    def __init__(self, name, HP, SP, MP, baseAtk, 
                 baseDef, atkMulti, defMulti):
        '''
        Constructor, creates a character.
        @param name: The name of a character
        @param HP: Maximum health point.
        @param SP: Maximum strength point.
        @param MP: Maximum spiritual point.
        @param baseAtk: Basic attack with fist.
        @param baseDef: Basic defense without defending. 
        @param atkMulti: Multiplication of attack of a particular weapon.
        @param defMulti: Multiplication of defense of a particular
        weapon.
        ''' 
        # TODO: Add operation object and list
        # Convert type
        HP = int(HP)
        SP = float(SP)
        MP = int(MP)
        # Set name
        self.name = name
        # Initialize health system
        self.health = HealthSystem(HP)
        # Initialize weapon system
        self.weapons = WeaponSystem(atkMulti, defMulti)
        # Initialize spirit system
        self.spirit = SpiritSystem(MP)
        # Initialize strength system
        self.strength = StrengthSystem(SP)
        # Initialize status flags
        ## Alive status
        self.alive = True
        ## Defending status
        self.defending = True
# TODO: Character refresh module. Use timestamp + loop to auto decrease/increase