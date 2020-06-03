#!/usr/bin/python3
'''Defines a script that adds all arguments to a Python list,
 and then save them to a file:'''


import sys
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file
try:
    l1 = load('add_item.json')
except:
    l1 = []
l2 = list(sys.argv[1:])
l1 = l1 + l2
save(l1, 'add_item.json')
