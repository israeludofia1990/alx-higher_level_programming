#!/usr/bin/python3
'''
contains a module that adds all arguments to a Python list,
and then save them to a file
'''
import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_file = "add_item.json"
my_list = []
argc = len(sys.argv)
if os.path.exists(my_file):
    my_list = load_from_json_file(my_file)
for i in range(1, argc):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, my_file)
