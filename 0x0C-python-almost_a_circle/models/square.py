#!/usr/bin/python3

"""Defines Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String Description of the instance

        Returns:
            str: Description of instance
        """
        form = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return form.format(self.id, self.x, self.y, self.width)
