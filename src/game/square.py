from enum import Enum


class Color(Enum):
    """
    Taken from Wikipedia:
    https://en.wikipedia.org/wiki/Tetromino#One-sided_tetrominoes
    """

    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    LIGHTBLUE = 5
    PINK = 6
    ORANGE = 7


class Square:
    """
    Represents a single square on the grid/canvas.

    Args:
        x: The x coordinate
        y: The y coordinate
        color: The color of the square
    """

    @property
    def color(self):
        """
        Returns the color property of the square as RGB values
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Matches the Color enum given to an RGB value.
        """
        match color:
            case Color.RED:
                self._color = (255, 0, 0)
            case Color.GREEN:
                self._color = (0, 255, 0)
            case Color.BLUE:
                self._color = (0, 0, 255)
            case Color.YELLOW:
                self._color = (255, 255, 0)
            case Color.LIGHTBLUE:
                self._color = (0, 255, 255)
            case Color.PINK:
                self._color = (255, 0, 255)
            case Color.ORANGE:
                self._color = (255, 127, 0)
            case _:
                raise ValueError("Invalid color")

    def __init__(self, x: int, y: int, color: Color):
        """
        The constructor for Square.

        Args:
            x: The x coordinate
            y: The y coordinate
            color: The color of the square
        """
        self.x = x
        self.y = y
        self.color = color

    def move_down(self):
        """
        Moves the square down one step.
        """
        self.y += 1

    def move_left(self):
        """
        Moves the square left one step.
        """
        self.x -= 1

    def move_right(self):
        """
        Moves the square right one step.
        """
        self.x += 1
