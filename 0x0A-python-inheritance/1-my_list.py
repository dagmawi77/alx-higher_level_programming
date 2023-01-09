#!/usr/bin/python3

"""Defines class"""


class MyList(list):
    """Implements sorted built-in list class."""

    def print_sorted(self):
        """list in sorted ascending order."""
        print(sorted(self))
