from enum import Enum
from random import choice
from math import sin, cos, pi

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
    """
    A class for representing a tetromino.
    Used for controlling the active piece on the grid
    and displaying the next piece due to spawn.
    """

    def __init__(self, shape: Shape = None):
        """
        Constructor for Tetromino.
        """
        # If shape is None, decide randomly
        self.shape = shape or choice(list(Shape))

        self.squares = []

    def spawn(self, x, y):
        """
        Populates self.squares with squares that are given
        coordinates and colors based on the shape.
        """
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
        """
        Moves all squares one step down.
        """
        for square in self.squares:
            square.move_down()

    def move_left(self):
        """
        Moves all squares one step left.
        """
        for square in self.squares:
            square.move_left()

    def move_right(self):
        """
        Moves all squares one step right.
        """
        for square in self.squares:
            square.move_right()

    def rotate(self, clockwise=True):
        """
        Rotates the tetromino around a pivot point.
        The pivot point is the first square in self.squares,
        which is why it is important that the shapes are
        correctly defined. Exits if the shape is an O (square).

        Args:
            clockwise (bool): Whether to rotate clockwise. Defaults to True.
        """
        if self.shape == Shape.O:
            return

        pivot = self.squares[0]

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
