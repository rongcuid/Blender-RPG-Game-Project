'''
Created on Jan 20, 2013

WeaponSystem class is the weapon system. Its main function is to 
attack and defend, NOT storing weapons information, which
is done by item system. It also does NOT do operations which are
done by operation system.

Attack is calculated by reading attack of item, multiply it by 
attack multiplier, add to base attack, and multiply by action 
strength multiplier.

Defense is also calculated to be used in attack function. Defense
is item defense times defense multiplier AND action multiplier, 
and add with base defense.

@author: carl
'''

class WeaponSystemClass():
    '''
    Weapon system class
    '''


    def __init__(self, atkMulti, defMulti):
        '''
        Constructor: Create a new weapon system.
        '''
    # An effective attack is an attack that hits its enemy
    def effectiveAttackHurt(self, baseAtk, itemAtk, atkMulti, actMulti, tgtDef):
        '''
        An effective attack that hurts.
        @param baseAtk: Base attack of a character.
        @param itemAtk: Base attack of an item.
        @param atkMulti: Attack multiplier of a character.
        @param actMulti: Action strength multiplier of a character.
        @param tgtDef: Target defense
        @return: Calculated hurt.
        '''
        # hurt = (((itemAtk * atkMulti) + baseAtk) * actMulti) - tgtDef
        return (((itemAtk * atkMulti) + baseAtk) * actMulti) - tgtDef
    # An effective defend is a defend that blocks an attack.
    def effectiveDefense(self, baseDef, itemDef, defMulti, actMulti):
        '''
        An effective defend that blocks
        @param baseDef: Base defense of a character.
        @param itemDef: Base defense of an item.
        @param defMulti: Defend multiplier of a character.
        @param actMulti: Action strength multiplier of a character.
        @return: Calculated defense
        '''
        # defense = ((itemDef * defMulti * actMulti) + baseDef)
        return ((itemDef * defMulti * actMulti) + baseDef)