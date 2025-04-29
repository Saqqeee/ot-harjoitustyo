import unittest
from game.tetromino import Tetromino, Shape


class TestTetromino(unittest.TestCase):
    def setUp(self):
        self.tetromino = Tetromino(Shape.O)
        self.tetromino.spawn(0, 0)

    def test_correct_shape_is_formed(self):
        coords = [(0, 0), (0, 1), (1, 1), (1, 0)]

        for square in self.tetromino.squares:
            coord = (square.x, square.y)
            self.assertIn(coord, coords)

    def test_squares_share_parent_color(self):
        for square in self.tetromino.squares:
            self.assertEqual(square.color, (255, 255, 0))

    def test_moving_left_works(self):
        coords = [(-1, 0), (-1, 1), (0, 1), (0, 0)]

        self.tetromino.move_left()

        for square in self.tetromino.squares:
            coord = (square.x, square.y)
            self.assertIn(coord, coords)

    def test_moving_right_works(self):
        coords = [(1, 0), (1, 1), (2, 1), (2, 0)]

        self.tetromino.move_right()

        for square in self.tetromino.squares:
            coord = (square.x, square.y)
            self.assertIn(coord, coords)

    def test_moving_down_works(self):
        coords = [(0, 1), (0, 2), (1, 2), (1, 1)]
        self.tetromino.move_down()

        for square in self.tetromino.squares:
            coord = (square.x, square.y)
            self.assertIn(coord, coords)
