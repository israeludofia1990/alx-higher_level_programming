#!/usr/bin/python3
'''contains a function that creates an Object from a “JSON file'''
import json


def load_from_json_file(filename):
    '''creates an Object from a “JSON file
    args:
    filename: filename
    '''
    with open(filename, 'r') as f:
        return json.load(f)
