#!/usr/bin/python3
"""
The container of MyList class inherit from list
"""


class MyList(list):
    """MyList class that inherits from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
