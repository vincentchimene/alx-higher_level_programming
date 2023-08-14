#!/usr/bin/python3

#  a function that replaces an element in a list at a specific position
# without modifying the original list (like in C).
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element
    return new_list
