#!/usr/bin/python3
'''contains base class'''


class Base:
    '''base class to manage id attribute in all
    future class
    Attributes:
        __nb_objects (int): the number of created Base objects.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes the default attributes of the Base object.

        Args:
            id (int): the identifier of the Base object.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
