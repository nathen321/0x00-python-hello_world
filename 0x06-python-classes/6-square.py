#!/usr/bin/python3
"""Square Class

just a square

"""


class Square:
    """ init a square

    like i said a square

    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        if self.__check_tuple(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.position = position

    """ get area of squar

    return:
        area of squar
    """
    def area(self):
        """ pls work

        """
        return self._Square__size ** 2

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    """ printin the squar"""
    def my_print(self):
        """ print a squar"""
        if self.size == 0:
            print()
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for x in range(self.size):
            for x in range(self.size):
                print("#", end="")
            print()

    def __check_tuple(self, position):
        if type(position) is tuple and type(position[0]) is int and type(position[1]) is int and position[0] >= 0 and position[1] >= 0:
            return True
        else:
            return False


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
