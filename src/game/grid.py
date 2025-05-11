import pygame
from .tetromino import Tetromino

X_MAX = 10
Y_MAX = 22


class Grid:
    """
    The class that holds the game state and handles most of the logic.
    """

    def __init__(self):
        """
        Constructor of Grid.
        """
        # Only used for collision and row checking.
        # We make the underlying grid logic 2 squares taller than what we present to
        # account for new shapes that take up 3 squares vertically.
        # False means an empty square, True means occupied.
        self.grid = [[False for _ in range(X_MAX)] for _ in range(Y_MAX)]

        # Holds the squares that are present in the grid.
        self.squares = []

        self.active = None
        self.next = Tetromino()

        self.game_over = False

    def new_shape(self):
        """
        Takes the tetromino from the queue
        and moves it to a member that can be rendered
        and controlled. Also refills the queue.
        """
        x = 4
        y = 0

        if not self.next:
            self.next = Tetromino()

        self.active = self.next
        self.active.spawn(x, y)

        self.next = Tetromino()

    def down(self):
        """
        Moves the active piece down one step.
        If it's not possible to move down,
        gives the individual squares to Grid
        and sets active to None.
        """
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
        """
        "Fast/Hard down"; calls down() repeatedly as long as it can.
        """
        while self.active:
            self.down()

    def left(self):
        """
        Moves the active piece left one step unless movement is blocked.
        """
        if not self.active:
            return

        for square in self.active.squares:
            if square.x <= 0 or self.grid[square.y][square.x - 1]:
                return

        self.active.move_left()

    def right(self):
        """
        Moves the active piece right one step unless movement is blocked.
        """
        if not self.active:
            return

        for square in self.active.squares:
            if square.x >= X_MAX - 1 or self.grid[square.y][square.x + 1]:
                return

        self.active.move_right()

    def rotate(self):
        """
        Attempts to rotate the active piece. If the rotation
        causes a conflict with the grid boundaries or other squares,
        reverts the rotation as if nothing happened.
        """
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
        """
        Maps a keypress to an action.

        Args:
            key: A value from a pygame keypress event.
        """
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
            case pygame.K_RETURN:
                if self.game_over:
                    self.__init__()

    def refresh_grid(self):
        """
        Clears the grid used for collision/clearance checking
        and rebuilds it from existing squares.
        """
        self.grid = [[False for _ in range(X_MAX)] for _ in range(Y_MAX)]
        for square in self.squares:
            self.grid[square.y][square.x] = True

    def clear_row(self, i):
        """
        Rebuilds the list of squares omitting the row that was cleared.

        Args:
            i: The index of the row to clear
        """
        squares_new = []
        for square in self.squares:
            if square.y != i:
                squares_new.append(square)
        self.squares = squares_new

    def check_rows(self):
        """
        Check the current grid row by row and perform actions as needed.
        Clears rows that are full, moves other pieces down if rows were cleared before.
        Also checks whether the game should end.
        """
        peak = Y_MAX
        for i, row in enumerate(self.grid):
            row_sum = sum(row)
            if i <= 2 and row_sum > 0:
                self.game_over = True
                return
            if i < peak and row_sum > 0:
                peak = i
            if row_sum == X_MAX:
                self.clear_row(i)
            if i > peak and row_sum == 0:
                for square in self.squares:
                    if square.y < i:
                        square.move_down()

    def tick(self):
        """
        Happens once per second. Moves the active piece down and
        checks whether rows have been cleared.
        """
        if self.game_over:
            return

        if not self.active:
            self.new_shape()

        self.down()
        self.refresh_grid()
        self.check_rows()
        self.refresh_grid()
