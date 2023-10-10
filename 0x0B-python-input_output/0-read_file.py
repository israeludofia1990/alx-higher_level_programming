#!/usr/bin/python3
'''contains a function that reads from file'''


def read_file(filename=""):
    '''Reads from a file and Prints it to stdout
    args:
    filename: name of file
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
