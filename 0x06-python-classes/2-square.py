#!/usr/bin/python3
class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """
        Define private instance attribute: size
        Raise TypeError & ValueError if not int or <0 resp.
        """

        if not isinstance(size ,int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        
    def area(self):
        """Area of this aquare


        returns:
        the size square"""

        return self.__size ** 2
        

