#!/usr/bin/python3

#  a function that removes all characters c and C from a string.
def no_c(my_string):
    new_str = ""# a new empty string
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            new_str += my_string[i]# add the character to the new empty string
    return new_str
