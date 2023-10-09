#!/usr/bin/python3
'''contains a function that prints a sorted list'''


class MyList(list):
    '''subclass of list'''

    def print_sorted(self):
        '''prints a sorted list'''
        print(sorted(self))
