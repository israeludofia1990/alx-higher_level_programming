#!/usr/bin/python3
'''contains a function that appends to a text file'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    args:
    filename: filename
    text: Text to append
    '''
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
