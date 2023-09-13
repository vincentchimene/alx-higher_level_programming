#!/usr/bin/python3
"""
This is a module container of the function 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match the type of obj to.
    Returns:
        True, If obj is an inherited instance of a_class.
        False, if otherwise.
    """
if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
