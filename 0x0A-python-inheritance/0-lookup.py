#!/usr/bin/python3
'''contains a function that returns
the list of available attributes and methods of an object
'''


def lookup(obj):
    '''the list of available attributes and methods of an object'''
    return dir(obj)
