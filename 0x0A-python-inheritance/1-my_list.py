#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
