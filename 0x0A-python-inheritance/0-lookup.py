#!/usr/bin/python3
"""
The lookup function container that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list object
    """
    return dir(obj)
