from enum import Enum
from random import choice
from .square import Square, Color
from math import sin, cos, pi


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
        Square(x, y, color),
        Square(x - 1, y, color),
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
        Square(x - 1, y, color),
        Square(x + 1, y, color),
        Square(x, y + 1, color),
    ]


def shape_j(x: int, y: int, color: Color):
    return [
        Square(x + 1, y, color),
        Square(x + 1, y - 1, color),
        Square(x + 1, y + 1, color),
        Square(x, y + 1, color),
    ]


def shape_l(x: int, y: int, color: Color):
    return [
        Square(x, y, color),
        Square(x, y - 1, color),
        Square(x, y + 1, color),
        Square(x + 1, y + 1, color),
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
    def __init__(self, shape: Shape = None):

        # If shape is None, decide randomly
        self.shape = shape or choice(list(Shape))

        self.squares = []

    def spawn(self, x, y):
        match self.shape:
            case Shape.I:
                self.squares = shape_i(x, y, Color.LIGHTBLUE)
            case Shape.O:
                self.squares = shape_o(x, y, Color.YELLOW)
            case Shape.T:
                self.squares = shape_t(x, y, Color.PINK)
            case Shape.J:
                self.squares = shape_j(x, y, Color.BLUE)
            case Shape.L:
                self.squares = shape_l(x, y, Color.ORANGE)
            case Shape.S:
                self.squares = shape_s(x, y, Color.GREEN)
            case Shape.Z:
                self.squares = shape_z(x, y, Color.RED)

    def move_down(self):
        for square in self.squares:
            square.move_down()

    def move_left(self):
        for square in self.squares:
            square.move_left()

    def move_right(self):
        for square in self.squares:
            square.move_right()

    def rotate(self, clockwise=True):
        # Don't even try to rotate O (square) shapes
        if self.shape == Shape.O:
            return

        # Select the first square to pivot around
        pivot = self.squares[0]

        # Move the other squares clockwise 90 degrees clockwise
        theta = pi / 2
        cosine = cos(theta)
        sine = sin(theta)
        if clockwise:
            sine = -sine

        for square in self.squares[1:]:
            x = square.x - pivot.x
            y = square.y - pivot.y

            x_new = cosine * x + -sine * y
            y_new = sine * x + cosine * y

            square.x = round(x_new + pivot.x)
            square.y = round(y_new + pivot.y)
