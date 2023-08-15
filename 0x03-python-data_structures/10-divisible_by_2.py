#!/usr/bin/python3

# a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    result = []
    for i in range(len(my_list)):
        result.append(my_list[i] % 2 == 0)
    return result
