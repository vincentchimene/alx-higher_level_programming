#!/usr/bin/python3
"""
A module container of the function 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    To check if the object is exact  instance of the specified class
        Args:
            obj: initial object
            a_class: class to confirm with the object
            Returns: True if object is an exact instance of the class
                      False if it is not
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
