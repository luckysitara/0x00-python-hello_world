#!/usr/bin/python3
class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius * self.__radius * 3.14

    def circumference(self):
        return 2 * 3.14 * self.__radius
