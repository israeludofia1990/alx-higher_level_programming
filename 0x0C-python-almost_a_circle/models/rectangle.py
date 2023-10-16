#!/usr/bin/python3
'''Contains Rectangle class'''

from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        class constructor
        args:
        width: width of the rectangle
        height: height of the rectangle
        x: x coordinate of the rectangle
        y: y coordinate of the rectangle
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter for width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter for x attribute'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y attribute getter and setter.
    @property
    def y(self):
        '''Get and Set the y attribute of the Rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' returns Area of rectangle'''
        return self.width * self.height

    def display(self):
        '''Prints in stdout the Rectangle instance with the character #'''
        print('\n' * self.y, end='')
        for height in range(self.height):
            print(' ' * self.x + '#' * self.width)

