'''
Created on Jan 20, 2013

This module is used to store constants for HP System

@author: carl
'''

# ---Start---: HP System Critical Points

# HP System Critical Point 1, above which solid HP automatically
# recovers.
HP_CRITICALPOINT_1 = 0.95
# HP System Critical Point 2. Between 1 and 2 solid HP does not 
# change.
HP_CRITICALPOINT_2 = 0.90
# HP System Critical Point 3. Between 2 and 3 solid HP decreases
# at constant rate.
HP_CRITICALPOINT_3 = 0.10

# ---End---: HP System Critical Points

# ---Start---: Change rates

# HP increase rate when solid HP above CP 1, points/min
HP_INCREASE_RATE = 5.0
# HP decrease rate when solid HP below CP 2, points/min
HP_DECREASE_RATE = 2.0
# HP decrease rate when solid HP below CP 3, points/min
HP_DECREASE_RATE_2 = 20.0

# ---End---: Change rates

# Max ratio of HP recover
HP_RECOVERY_RATIO = 0.8
