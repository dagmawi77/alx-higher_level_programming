#!/usr/bin/python3

"""Defines class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary."""
        return self.__dict__
