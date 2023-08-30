#!/usr/bin/python3
""" Module: Sqaure_Module """


class Square:
    """A class that defines a sqaure"""

    def __init__(self, size=0):
        """
        Initializes a new square instance

        Args:
            size(int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
        int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
            value (int): The new size for the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
