import pygame
from .tetromino import Tetromino

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
        self.grid = [[False for _ in range(X_MAX)] for _ in range(Y_MAX)]

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

    def down(self):
        if not self.active:
            return

        for square in self.active.squares:
            if square.y >= Y_MAX - 1 or self.grid[square.y + 1][square.x]:
                # If it's no longer possible to go down
                self.squares += self.active.squares
                self.active = None
                return

        self.active.move_down()

    def drop(self):
        while self.active:
            self.down()

    def left(self):
        if not self.active:
            return

        for square in self.active.squares:
            if square.x <= 0 or self.grid[square.y][square.x - 1]:
                return

        self.active.move_left()

    def right(self):
        if not self.active:
            return

        for square in self.active.squares:
            if square.x >= X_MAX - 1 or self.grid[square.y][square.x + 1]:
                return

        self.active.move_right()

    def rotate(self):
        if not self.active:
            return

        self.active.rotate()

        # If the rotated tetromino contains out of bounds squares
        # or collides with anything on the grid, cancel the rotation
        for square in self.active.squares:
            if (
                square.x < 0
                or square.x >= X_MAX
                or square.y < 0
                or square.y >= Y_MAX
                or self.grid[square.y][square.x]
            ):
                self.active.rotate(clockwise=False)
                return

    def move(self, key):
        match key:
            case pygame.K_LEFT | pygame.K_a:
                self.left()
            case pygame.K_RIGHT | pygame.K_d:
                self.right()
            case pygame.K_DOWN | pygame.K_s:
                self.down()
            case pygame.K_SPACE:
                self.drop()
            case pygame.K_UP | pygame.K_w:
                self.rotate()

    def refresh_grid(self):
        self.grid = [[False for _ in range(X_MAX)] for _ in range(Y_MAX)]
        for square in self.squares:
            self.grid[square.y][square.x] = True

    def clear_row(self, i):
        squares_new = []
        for square in self.squares:
            if square.y != i:
                squares_new.append(square)
        self.squares = squares_new

    def tick(self):
        if not self.active:
            self.new_shape()

        self.down()
        self.refresh_grid()

        peak = Y_MAX
        for i, row in enumerate(self.grid):
            row_sum = sum(row)
            if i < peak and row_sum > 0:
                peak = i
            if row_sum == X_MAX:
                self.clear_row(i)
            if i > peak and row_sum == 0:
                for square in self.squares:
                    if square.y < i:
                        square.move_down()

        self.refresh_grid()

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
