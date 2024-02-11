from abc import ABC, abstractmethod
from numbers import Number

class Geom:

    @abstractmethod
    def __init__(self, name):
        self.name = name
        """
        Method for initializing a shape
        """

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method for returning the string representation of a shape.
        """

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstract method for returning the formal string representation of a shape.
        """
        return f'Geom "{self.name}"'

    @abstractmethod
    def get_pr(self):
        raise NotImplementedError("No get_pr func")
    """
    Method for calculating perimeter
    """


class Triangle(Geom):
    def __init__(self, a: Number, b: Number, c: Number):
        if not (isinstance(a, Number)
                and not isinstance(b, Number)
                and not isinstance(c, Number)):
            raise TypeError("All sides should be numeric")

        if a < 0 or b < 0:
            raise ValueError('Sides can\'t be less 0')

        self.a = a
        self.b = b
        self.c = c
        """
        Method for initializing lengths
        """

    def __repr__(self) -> str:
        return f'Triangle "{self.a, self.b, self.c}"'

    def get_pr(self):
        return self.a + self.b + self.c
    """
    Method for calculating perimeter
    """

class Square(Geom):
    def __init__(self, a: Number):

        if not (isinstance(a, Number)):
            raise TypeError("All sides should be numeric")

        if a < 0:
            raise ValueError('Sides can\'t be less 0')

        self.a = a
        """
        Method for initializing lengths
        """

    def __repr__(self) -> str:
        return f'Square "{self.a}"'

    def get_pr(self):
        return self.a * 4
    """
    Method for calculating perimeter
    """

class Rectangle(Geom):
    def __init__(self, a: Number, b: Number):
        if not (isinstance(a, Number)
                and not isinstance(b, Number)):
            raise TypeError("All sides should be numeric")

        if a < 0 or b < 0:
            raise ValueError('Sides can\'t be less 0')

        self.a = a
        self.b = b
        """
        Method for initializing lengths
        """


    def __repr__(self) -> str:
        return f'Rectangle "{self.a, self.b}"'

    def get_pr(self):
        return 2*(self.a + self.b)
    """
    Method for calculating perimeter
    """