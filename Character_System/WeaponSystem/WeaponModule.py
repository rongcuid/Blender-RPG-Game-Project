'''
Created on Jan 20, 2013

WeaponSystem class is the weapon system. Its main function is to 
attack and defend, NOT storing weapons information, which
is done by item system. It also does NOT do operations which are
done by operation system.

Attack is calculated by reading attack of item, multiply it by 
attack multiplier, add to base attack, and multiply by action 
strength multiplier.

Defending is different: read defense of item, multiply it
by defense multiplier AND action strength multiplier, and
add to base defense.

@author: carl
'''

class WeaponSystem():
    '''
    Weapon system class
    '''


    def __init__(self, atkMulti, defMulti):
        '''
        Constructor: Create a new weapon system.
        '''
    # An effective attack is an attack that hits its enemy
    def effectiveAttack(self, baseAtk, itemAtk, atkMulti, actMulti, tgtDef):
        '''
        An effective attack that hurts.
        @param baseAtk: Base attack of a character.
        @param itemAtk: Base attack of an item.
        @param atkMulti: Attack multiplier of a character.
        @param actMulti: Action strength multiplier of a character.
        @param tgrDef: Target defense
        @return: Calculated hurt.
        '''
        # hurt = (((itemAtk * atkMulti) + baseAtk) * actMulti) - tgtDef
        return (((itemAtk * atkMulti) + baseAtk) * actMulti) - tgtDef
    # An effective defend is a defend that blocks an attack.
    def effectiveDefend(self, baseDef, itemDef, defMulti, actMulti, srcAtk):
        '''
        An effective defend that blocks
        @param baseDef: Base defense of a character.
        @param itemDef: Base defense of an item.
        @param defMulti: Defend multiplier of a character.
        @param actMulti: Action strength multiplier of a character.
        @param srcAtk: Attack value of the attacker.
        @return: Calculated hurt
        '''
        # hurt = srcAtk - ((itemDef * defMulti * actMulti) + baseDef)
        return srcAtk - ((itemDef * defMulti * actMulti) + baseDef)