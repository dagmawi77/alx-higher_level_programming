#!/usr/bin/python3

"""Defines function."""


def number_of_lines(filename=""):
    """Return the number of lines in file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
