#!/usr/bin/python3
"""
The container of MyList class inherit from list
"""


class MyList(list):
    """MyList class that inherits from list"""
    
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
