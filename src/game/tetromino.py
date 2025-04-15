from enum import Enum
from random import choice
from .square import Square, Color


class Shape(Enum):
    """
    Taken from Wikipedia:
    https://en.wikipedia.org/wiki/Tetromino#One-sided_tetrominoes
    """

    I = 1
    O = 2
    T = 3
    J = 4
    L = 5
    S = 6
    Z = 7


# Helper functions for different shapes


def shape_i(x: int, y: int, color: Color):
    return [
        Square(x - 1, y, color),
        Square(x, y, color),
        Square(x + 1, y, color),
        Square(x + 2, y, color),
    ]


def shape_o(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x + 1, y, color),
        Square(x, y + 1, color),
        Square(x + 1, y + 1, color),
    ]


def shape_t(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x + 1, y, color),
        Square(x + 2, y, color),
        Square(x + 1, y + 1, color),
    ]


def shape_j(x: int, y: int, color: Color):
    return [
        Square(x + 1, y, color),
        Square(x + 1, y + 1, color),
        Square(x + 1, y + 2, color),
        Square(x, y + 2, color),
    ]


def shape_l(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x, y + 1, color),
        Square(x, y + 2, color),
        Square(x + 1, y + 2, color),
    ]


def shape_s(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x + 1, y, color),
        Square(x, y + 1, color),
        Square(x - 1, y + 1, color),
    ]


def shape_z(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x - 1, y, color),
        Square(x, y + 1, color),
        Square(x + 1, y + 1, color),
    ]


class Tetromino:
    def __init__(self, color: Color = None, shape: Shape = None):

        # If color and shape are None, decide randomly
        self.color = color or choice(list(Color))
        self.shape = shape or choice(list(Shape))

        self.squares = []

    def spawn(self, x, y):
        match self.shape:
            case Shape.I:
                self.squares = shape_i(x, y, self.color)
            case Shape.O:
                self.squares = shape_o(x, y, self.color)
            case Shape.T:
                self.squares = shape_t(x, y, self.color)
            case Shape.J:
                self.squares = shape_j(x, y, self.color)
            case Shape.L:
                self.squares = shape_l(x, y, self.color)
            case Shape.S:
                self.squares = shape_s(x, y, self.color)
            case Shape.Z:
                self.squares = shape_z(x, y, self.color)

    def move_down(self):
        for square in self.squares:
            square.move_down()

    def move_left(self):
        for square in self.squares:
            square.move_left()

    def move_right(self):
        for square in self.squares:
            square.move_right()
