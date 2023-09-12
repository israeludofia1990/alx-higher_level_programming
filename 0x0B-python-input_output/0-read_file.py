#!/usr/bin/python3
'''Contains a module that reads from a text file'''


def read_file(filename=""):
    '''function that reads a text file (UTF8) and prints it to stdout'''
    with open(filename, encoding='utf-8') as my_file:
        contents = my_file.read()
        print(contents)
