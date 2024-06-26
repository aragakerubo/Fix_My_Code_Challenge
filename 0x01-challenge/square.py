#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square Class"""

    width = 0
    height = 0

    def __init__(self, width=0, height=0, *args, **kwargs):
        """Square Constructor"""
        if width != 0:
            self.width = width
        if height != 0:
            self.height = height

    def area_of_my_square(self):
        """Area of the Square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Perimeter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the Square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
