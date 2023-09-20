#!/usr/bin/python3
"""
The "class_to_json" function container
"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
