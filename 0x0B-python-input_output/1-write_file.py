#!/usr/bin/python3
'''contains a function that writes to a file'''


def write_file(filename="", text=""):
    '''writes a string to a text file (UTF8) and returns
    the number of characters written
    args:
    filename: name of file
    text: text to be written
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
