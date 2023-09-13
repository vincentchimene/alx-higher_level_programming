#!/usr/bin/python3
"""
The lookup function container
"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list of object
    """
    return dir(obj)
