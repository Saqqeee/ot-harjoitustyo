import unittest
from main import Grid

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.empty = [[0 for _ in range(22)] for _ in range(10)]

    def test_square_spawns_in_correct_coordinates(self):
        self.empty[5][0] = 1
        self.empty[5][1] = 1
        self.empty[6][0] = 1
        self.empty[6][1] = 1

        self.grid.spawn_square()

        self.assertEqual(self.empty, self.grid.grid)

    def test_active_gets_correct_coordinates(self):
        testactive = [(5, 0), (6, 0), (6, 1), (5, 1)]

        self.grid.spawn_square()

        self.assertEqual(testactive, self.grid.active)

    def test_shape_moves_down_correctly(self):
        self.empty[5][1] = 1
        self.empty[5][2] = 1
        self.empty[6][1] = 1
        self.empty[6][2] = 1

        self.grid.spawn_square()
        self.grid.down()

        self.assertEqual(self.empty, self.grid.grid)

