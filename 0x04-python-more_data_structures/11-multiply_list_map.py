#!/usr/bin/python3

# returns a list with all values times a number noloops.
def mutiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
