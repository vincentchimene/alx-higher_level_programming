#!/usr/bin/python3

""" a function that adds all unique
integers in a list (only once for each integer).
"""
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return(new_list)
