import unittest
from game.grid import Grid, Y_MAX


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.grid.tick()

    def test_new_shape_is_spawned_on_first_tick(self):
        self.assertIsNotNone(self.grid.active)

    def test_dropped_shape_is_added_to_square_list(self):
        self.grid.drop()

        self.assertEqual(len(self.grid.squares), 4)
