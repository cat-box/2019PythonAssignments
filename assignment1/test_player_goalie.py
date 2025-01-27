import unittest
from unittest import TestCase
import inspect
from player_goalie import PlayerGoalie


class TestPlayerGoalie(TestCase):
    """ Unit tests for PlayerGoalie class """

    
    def setUp(self):
        self.logPoint()
        self.test_player_goalie = PlayerGoalie(1, "Roberto", "Luongo", 190.5, 215, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13)


    def test_get_shots_against_valid(self):
        """ 010A: Valid return for get_shots_against() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_shots_against(), 788)


    def test_get_goals_against_valid(self):
        """ 020A: Valid return for get_goals_against() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_goals_against(), 83)


    def test_get_goals_saved_valid(self):
        """ 030A: Valid return for get_goals_saved() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_goals_saved(), 705)



    def test_get_games_played(self):
        """ 040A: Valid return for get_games_played() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_games_played(), 30)

    
    def test_get_games_won(self):
        """ 050A: Valid return for get_games_won() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_games_won(), 12)

    
    def test_get_games_lost(self):
        """ 060A: Valid return for get_games_lost() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_games_lost(), 13)


    def test_get_win_loss_stats(self):
        """ 070A: Valid return for get_win_loss_stats() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_win_loss_stats(), [12, 13, 30])
    

    def test_set_win_loss_stats(self):
        """ 080A: Valid modification of values """
        self.logPoint()
        self.test_player_goalie.set_win_loss_stats(13, 15, 33)
        self.assertEqual(self.test_player_goalie.get_win_loss_stats(), [13, 15, 33])


    def test_get_stats(self):
        """ 090A: Valid return of get_stats() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_stats(), [788, 83, 705])


    def test_get_type(self):
        """ 100A: Valid return of get_type() """
        self.logPoint()
        self.assertEqual(self.test_player_goalie.get_type(), "Goalie")


    def tearDown(self):
        self.logPoint()
    

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))
        