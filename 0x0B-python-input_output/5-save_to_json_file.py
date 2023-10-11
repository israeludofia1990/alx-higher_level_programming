#!/usr/bin/python3
''' contains a function that writes an Object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file, using a JSON representation
    args:
    my_obj: data variable to save
    filename: filename
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
