#!/usr/bin/python3

"""Defines a Base class
"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor

        Args:
            id (int): Instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
