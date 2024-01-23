#!/usr/bin/python3
"""class Square."""


class Square:
    """quare iner class"""
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    """calulate the area"""
    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        val = []
        if self.__size == 0:
            return ("")
        [val.append("\n") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [val.append(" ") for i in range(0, self.__position[0])]
            for j in range(self.__size):
                val.append("#")
            val.append("\n") if i is not self.__size - 1 else ""
        return ("".join(val))
