#!/usr/bin/python3

"""Square class"""


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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

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
            return

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()

    def __str__:
        """string representation of square instance"""
        if self.__size != 0:
            [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print()
        return ""
