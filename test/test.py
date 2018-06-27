import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from dictionaryball import game_dict, num_points_scored, shoe_size, team_colors, team_names, player_numbers, player_stats

class TestDictionaryBall(unittest.TestCase):

    def test_game_dict(self):
        pass

    def test_num_points_scored(self):
        self.assertEqual(type(num_points_scored('Mason Plumlee')), type(26), "Return value must be an integer")
        self.assertEqual(num_points_scored('Mason Plumlee'), 26)

    def test_shoe_size(self):
        pass

    def test_team_colors(self):
        pass

    def test_team_names(self):
        pass

    def test_player_numbers(self):
        pass

    def test_player_stats(self):
        pass
