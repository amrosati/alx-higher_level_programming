#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: size of square"""
        return self.__size

    @property
    def position(self):
        """tuple: squre coordinates"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Position setter

        Must be a 2 positive integers tuple

        Args:
            value (typle): Coordinates of a square
        """
        error = TypeError("position must be a tuple of 2 positive integers")

        if type(value) is not tuple:
            raise error
        if len(value) != 2:
            raise error
        for i in value:
            if i < 0:
                raise error

        self.__position = value

    def area(self):
        """Returns the square's area

        Area = a^2

        Returns:
            Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
