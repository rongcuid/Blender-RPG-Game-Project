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

from HealthSystem.HealthModule import HealthSystemClass
from StrengthSystem.StrengthModule import StrengthSystemClass
from SpiritSystem.SpiritModule import SpiritSystemClass
from ItemSystem.ItemModule import ItemSystemClass

class Character:
    '''
    The meta class for character managing
    '''
    # List of characters using SN
    CharacterList = None
    # List of character SNs using Name
    SNList = None

    def __init__(self, name, SN, HP, SP, MP, baseAtk, 
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
        # TODO: Register to Character list
        # Convert type
        HP = int(HP)
        SP = float(SP)
        MP = int(MP)
        baseAtk = int(baseAtk)
        baseDef = int(baseDef)
        # Set name
        self.name = name
        # Initialize health system
        self.health = HealthSystemClass(HP)
        # Initialize spirit system
        self.spirit = SpiritSystemClass(MP)
        # Initialize strength system
        self.strength = StrengthSystemClass(SP)
        # TODO: Storage system for item storage
        # Initialize base attack
        self.baseAttack = baseAtk
        # Initialize base defense
        self.baseDefense = baseDef
        # Initialize attack multiplier
        self.attackMulti = atkMulti
        # Initialize defense multiplier
        self.defenseMulti = defMulti
        
        # Initialize status flags
        ## Alive status
        self.alive = True
        ## Defending status
        self.defending = False
    # TODO: Character refresh module. Use timestamp + loop to auto decrease/increase
    def getBaseAttack(self):
        '''
        Returns base attack
        '''
        return self.baseAttack
    def getbaseDefense(self):
        '''
        Returns base defense
        '''
        return self.baseDefense
    def getAttackMulti(self):
        '''
        Returns attack multiplier.
        '''
        return self.attackMulti
    def getDefenseMulti(self):
        '''
        Returns defense multiplier
        '''
        return self.defenseMulti
    def isDefending(self):
        '''
        If defending, return true
        '''
        return self.defending
