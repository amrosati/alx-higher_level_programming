#!/usr/bin/python3

"""Defines Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width (int): width
            height (int): height
            x (int): x point
            y (int): y point
            id (int): instance id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        """
        self.validate_value('width', width)
        self.__width = width

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        """
        self.validate_value('height', height)
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """
        self.validate_value('x', x)
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """
        self.validate_value('y', y)
        self.__y = y

    def validate_value(self, name, value):
        """Integers validation

        Args:
            name (str): Name of the variable
            value (:obj:Any): The variable's value

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 1, except x and y
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value < 1:
            if value < 0 and name in ['x', 'y']:
                raise ValueError(f'{name} must be >= 0')

            raise ValueError(f'{name} must be > 0')
