#!/usr/bin/python3
"""Module 1-square

Contains ''Square'' class
"""


class Square:
    """Square

    defines a square with size

    Attributes:
        size: private attribute represents a square's size
    """
    __init__(self, size):
        """init

        Initializes Square instances

        Args:
            size: size of square
        """
        self.__size = size
