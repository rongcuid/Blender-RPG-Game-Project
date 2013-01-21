'''
Created on Jan 21, 2013

This file contains constants for SpiritModule

@author: carl
'''

# ---Start---:  MP critical points

# Critical point 1, above which MP auto recovers
MP_CRITICALPOINT_1 = 0.90
# Critical point 2, above which MP does not change, below which 
# MP auto decreases.
MP_CRITICALPOINT_2 = 0.80

# ---End---: MP critical points

# Maximum amount of recovery, usually 80% of total damage
MP_RECOVERY_RATIO = 0.8

# ---Start---: Change rates

# Automatic recover rate, points/min
MP_INCREASE_RATE = 5.0
# Automatic decrease rate, points/min
MP_DECREASE_RATE = 2.0 

# ---End---: Change rates