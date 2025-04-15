from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4


class Square:
    """
    Represents a single square on the grid/canvas.

    :param x: The x coordinate
    :param y: The y coordinate
    :param color: The color of the square
    """

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        match color:
            case Color.RED:
                self._color = (255, 0, 0)
            case Color.GREEN:
                self._color = (0, 255, 0)
            case Color.BLUE:
                self._color = (0, 0, 255)
            case Color.YELLOW:
                self._color = (255, 255, 0)
            case _:
                raise ValueError("Invalid color")

    def __init__(self, x: int, y: int, color: Color):
        self.x = x
        self.y = y
        self.color = color

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
