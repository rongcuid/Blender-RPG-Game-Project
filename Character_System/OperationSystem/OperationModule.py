'''
Created on Feb 19, 2013

This file includes OperationSystemClassClass class which stores some
important operations such as attack, defend, use item etc.

@author: carl
'''
from WeaponSystem.WeaponModule import WeaponSystemClass
class OperationSystemClass():
    '''
    This class contains several important actions.
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def attack(self, src, tgt, weapon, shield):
        '''
        Attacks effectively.
        @param src: Attacker
        @param tgt: Attacked
        @param weapon: Weapon used
        @param shield: Item to block
        '''
        srcBaseAtk = src.getBaseAttack()
        srcAtkMulti = src.getAttackMulti()
        srcActMulti = src.strength.getActionMulti()
        tgtBaseDef = tgt.getBaseDefense()
        tgtDefMulti = tgt.getDefenseMulti()
        tgtActMulti = tgt.strength.getActionMulti()
        if tgt.isDefending():
            tgtDef = WeaponSystemClass.effectiveDefense(tgtBaseDef, shield.getDefense(),
                                               tgtDefMulti, tgtActMulti)
        else:
            tgtDef = tgtBaseDef
        hurt = WeaponSystemClass.effectiveAttackHurt(srcBaseAtk, weapon.getAttack, 
                                         srcActMulti, tgtDef)
        tgt.health.hurt(hurt)
        