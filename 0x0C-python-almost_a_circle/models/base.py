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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of ``list_objs`` to file

        Args:
            list_objs (:obj:list): A list of instances
        """
        filename = cls.__name__ + ".json"
        text = []
        if list_objs:
            for obj in list_objs:
                text.append(obj.to_dictionary())

        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    @staticmethod
    def from_json_string(json_string):
        """Decodes a JSON string to a Python object

        Args:
            json_string (str): JSON string representation

        Returns:
            list: list represented by ``json_string``
        """
        if json_string:
            return json.loads(json_string)

        return []
