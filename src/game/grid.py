import pygame
from .tetromino import Tetromino
from .square import Square

SQUARE_SIZE = 30
MARGIN = 30
X_MAX = 10
Y_MAX = 22


class Grid:
    def __init__(self):
        # Only used for collision and row checking.
        # We make the underlying grid logic 2 squares taller than what we present to
        # account for new shapes that take up 3 squares vertically.
        # False means an empty square, True means occupied.
        self.grid = [[False for _ in range(Y_MAX)] for _ in range(X_MAX)]

        # Holds the squares that are present in the grid.
        self.squares = []

        self.active = None
        self.next = Tetromino()

    def new_shape(self):
        # Base spawn coordinates
        x = 4
        y = 0

        # Make sure that a new tetromino is ready to go
        if not self.next:
            self.next = Tetromino()

        # Take the next tetromino from the queue and
        # give it coordinates
        self.active = self.next
        self.active.spawn(x, y)

        # Place a new piece on the queue
        self.next = Tetromino()

    def down(self):  # TODO: Out of bounds and collision checking
        self.active.move_down()

    def tick(self):
        if not self.active:
            self.new_shape()

        self.down()

        self.grid = [[False for _ in range(Y_MAX)] for _ in range(X_MAX)]
        for square in self.squares:
            self.grid[square.x][square.y] = True

    def render(self, window):
        bounds = pygame.Rect(MARGIN, MARGIN, SQUARE_SIZE * 10, SQUARE_SIZE * 20)
        pygame.draw.rect(window, (255, 255, 255), bounds, 1)

        for square in self.squares:
            posx = SQUARE_SIZE * square.x + MARGIN
            posy = SQUARE_SIZE * (square.y - 2) + MARGIN

            drawable_square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

            pygame.draw.rect(window, square.color, drawable_square, 0)

        if self.active:
            for square in self.active.squares:
                if square.y < 2:
                    continue
                posx = SQUARE_SIZE * square.x + MARGIN
                posy = SQUARE_SIZE * (square.y - 2) + MARGIN

                drawable_square = pygame.Rect(posx, posy, SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(window, square.color, drawable_square, 0)
