#!/usr/bin/python3
'''module that contains base class'''


class Base:
    '''base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor
        args:
        id: public instance attribute
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
