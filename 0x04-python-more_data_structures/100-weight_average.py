#!/usr/bin/python3

# returns the weighted average of all integers tuple 
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for n in my_list:
        average += (n[0] * n[1])
        size += (n[1])
    return (average / size)
