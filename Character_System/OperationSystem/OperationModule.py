'''
Created on Feb 19, 2013

This file includes OperationSystemClassClass class which stores some
important operations such as attack, defend, use item etc.

@author: carl
'''
from CharacterSystem.CharacterModule import Character
from WeaponSystem.WeaponModule import WeaponSystemClass
from ItemSystem.ItemModule import ItemSystemClass
class OperationSystemClass():
    '''
    This class contains several important actions.
    '''
    # TODO: operation with SN

    def __init__(self):
        '''
        Constructor
        '''
    @classmethod
    def attack(cls, srcSN, tgtSN, weaponSN, shieldSN):
        '''
        Attacks using Serial Numbers
        @param srcSN: Attacker SN
        @param tgtSN: Attacked SN
        @param weaponSN: Weapon SN
        @param shieldSN: Shield SN
        '''
        src = Character.retrieveCharacter(srcSN)
        tgt = Character.retrieveCharacter(tgtSN)
        weapon = ItemSystemClass.retrieveItem(weaponSN)
        shield = ItemSystemClass.retrieveItem(shieldSN)
        cls.attackLowLevel(src, tgt, weapon, shield)
    @classmethod
    def attackLowLevel(cls, src, tgt, weapon, shield):
        '''
        Attacks effectively.
        @param src: Attacker
        @param tgt: Attacked
        @param weapon: Weapon used
        @param shield: Item to block
        @type src: Character
        @type tgt: Character
        @type weapon: Item
        @type shield: Item
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
        hurt = WeaponSystemClass.effectiveAttackHurt(srcBaseAtk, weapon.getAttack(), 
                                         srcAtkMulti, srcActMulti, tgtDef)
        tgt.health.hurt(hurt)
        