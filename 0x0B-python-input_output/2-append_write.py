#!/usr/bin/python3
'''contains a module that appends a text file'''


def append_write(filename="", text=""):
    '''Appends to a text file'''
    with open(filename, 'a', encoding='utf-8') as my_file:
        return my_file.write(text)
