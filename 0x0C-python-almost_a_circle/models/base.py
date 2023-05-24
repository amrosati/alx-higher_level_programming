#!/usr/bin/python3

"""Defines a Base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Encodes a list of dicts object to JSON string

        Args:
            list_dictionaries (:obj:list): list of dictionaries

        Returns:
            str: JSON string representation of the list
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
