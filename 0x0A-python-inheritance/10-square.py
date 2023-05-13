#!/usr/bin/python3

"""Defines ``Square`` class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square and inherits from ``Rectangle``
    """

    def __init__(self, size):
        """Instantiation method

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not int
            ValueError: if size is 0 or less
        """
        super().integer_validator("size", size)
        super(size, size)
        self.__size = size

    def area(self):
        """Area of square
        """
        return self.__size ** 2
