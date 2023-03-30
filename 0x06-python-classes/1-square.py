#!/usr/bin/python3
"""Square class module

Defines a square with a size (based on ''0-square.py'')

Contains:
    - Private instance attribute: ''size''
    - Instantiation with size (no type/value)

Why:
    Why size is private attribute?
    The size of a square is crucial for a square,
    many things depend of it (area computation, etc.),
    so you, as class builder,
    must control the type and value of this attribute.
    One way to have the control is to keep it privately.
    You will see in next tasks how to get,
    update and validate the size value.
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
