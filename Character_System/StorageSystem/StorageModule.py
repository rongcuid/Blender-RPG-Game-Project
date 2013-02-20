'''
Created on Feb 19, 2013

@author: carl
'''

class StorageSystemClass():
    '''
    This class stores the SN of items a character carries
    '''
    # TODO: Lock of equipped items
    # List of Items
    SNList = [None]
    def __init__(self):
        '''
        Adds a new storage system.
        '''
    def add(self, SN):
        '''
        Adds an item
        '''
        self.SNList.append(SN)
    def rm(self, SN):
        '''
        Removes an item
        '''
        self.SNList.remove(SN)
        