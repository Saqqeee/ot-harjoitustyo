import unittest
import pygame
from game.grid import Grid, Y_MAX
from game.square import Square, Color


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.grid.tick()

    def test_new_shape_is_spawned_on_first_tick(self):
        self.assertIsNotNone(self.grid.active)

    def test_dropped_shape_is_added_to_square_list(self):
        self.grid.drop()

        self.assertEqual(len(self.grid.squares), 4)

    def test_squares_appear_on_grid(self):
        for i in range(9):
            self.grid.squares.append(Square(i, 21, Color.RED))

        self.grid.tick()

        self.assertEqual(sum(self.grid.grid[21]), 9)

    def test_full_row_is_cleared(self):
        for i in range(10):
            self.grid.squares.append(Square(i, 21, Color.RED))

        self.grid.tick()

        self.assertEqual(sum(self.grid.grid[21]), 0)

    def test_line_clear_gives_points(self):
        for i in range(10):
            self.grid.squares.append(Square(i, 21, Color.RED))

        self.grid.tick()

        self.assertEqual(self.grid.score, 100)

    def test_game_over_if_stack_reaches_ceiling(self):
        self.grid.squares.append(Square(0, 0, Color.RED))

        self.grid.tick()

        self.assertTrue(self.grid.game_over)

    def test_squares_above_cleared_line_move_down(self):
        for i in range(9):
            self.grid.squares.append(Square(i, 20, Color.RED))
        for i in range(10):
            self.grid.squares.append(Square(i, 21, Color.RED))

        self.grid.tick()
        self.grid.tick()

        self.assertEqual(sum(self.grid.grid[21]), 9)

    def test_moving_left_works(self):
        squares_old = []
        for square in self.grid.active.squares:
            squares_old.append((square.x - 1, square.y))

        self.grid.move(pygame.K_LEFT)

        squares_new = []
        for square in self.grid.active.squares:
            squares_new.append((square.x, square.y))

        for square in squares_old:
            self.assertIn(square, squares_new)

    def test_moving_right_works(self):
        squares_old = []
        for square in self.grid.active.squares:
            squares_old.append((square.x + 1, square.y))

        self.grid.move(pygame.K_RIGHT)

        squares_new = []
        for square in self.grid.active.squares:
            squares_new.append((square.x, square.y))

        for square in squares_old:
            self.assertIn(square, squares_new)

    def test_moving_down_works(self):
        squares_old = []
        for square in self.grid.active.squares:
            squares_old.append((square.x, square.y + 1))

        self.grid.move(pygame.K_DOWN)

        squares_new = []
        for square in self.grid.active.squares:
            squares_new.append((square.x, square.y))

        for square in squares_old:
            self.assertIn(square, squares_new)
