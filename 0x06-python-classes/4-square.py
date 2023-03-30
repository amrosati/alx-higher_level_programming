#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): size of square
        """
        self.__size = size

    @property
    def size(self):
        """int: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter

        Args:
            value (int): size value that must be an int and positive
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Returns the square's area

        Area = a^2

        Returns:
            Area of square
        """
        return self.__size ** 2
