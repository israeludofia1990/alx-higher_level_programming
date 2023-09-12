#!/usr/bin/python3
'''contains a module that writes to stdout'''


def write_file(filename="", text=""):
    '''
        writes a string to a text file (UTF8) and
        returns the number of characters written:
    '''
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)
