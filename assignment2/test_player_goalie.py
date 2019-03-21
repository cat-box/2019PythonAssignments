import unittest
from unittest import TestCase
import inspect
from player_goalie import PlayerGoalie


class TestPlayerGoalie(TestCase):
    """ Unit tests for PlayerGoalie class """

    
    def setUp(self):
        self.logPoint()
        self.test_player_goalie = PlayerGoalie("Roberto", "Luongo", 190.5, 215, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13, "Goalie")


    def test_player_goalie_valid(self):
        """ 000A: Valid values for constructor """
        self.assertIsNotNone(self.test_player_goalie)


    def test_player_goalie_invalid_undefined(self):
        """ 000B: Invalid values (undefined) for constructor """
        self.assertRaisesRegex(ValueError, "fname cannot be undefined", PlayerGoalie, None, "Luongo", 190.5, 215, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13, "Goalie")


    def test_get_shots_against_valid(self):
        """ 010A: Valid return for get_shots_against() """
        self.assertEqual(self.test_player_goalie.get_shots_against(), 788)


    def test_get_goals_against_valid(self):
        """ 020A: Valid return for get_goals_against() """
        self.assertEqual(self.test_player_goalie.get_goals_against(), 83)


    def test_get_goals_saved_valid(self):
        """ 030A: Valid return for get_goals_saved() """
        self.assertEqual(self.test_player_goalie.get_goals_saved(), 705)
        

    def test_get_games_played(self):
        """ 040A: Valid return for get_games_played() """
        self.assertEqual(self.test_player_goalie.get_games_played(), 30)

    
    def test_get_games_won(self):
        """ 050A: Valid return for get_games_won() """
        self.assertEqual(self.test_player_goalie.get_games_won(), 12)

    
    def test_get_games_lost(self):
        """ 060A: Valid return for get_games_lost() """
        self.assertEqual(self.test_player_goalie.get_games_lost(), 13)


    def test_get_win_loss_stats(self):
        """ 070A: Valid return for get_win_loss_stats() """
        self.assertEqual(self.test_player_goalie.get_win_loss_stats(), [12, 13, 30])
    

    def test_set_win_loss_stats(self):
        """ 080A: Valid modification of values """
        self.test_player_goalie.set_win_loss_stats(13, 15, 33)
        self.assertEqual(self.test_player_goalie.get_win_loss_stats(), [13, 15, 33])


    def test_get_stats(self):
        """ 090A: Valid return of get_stats() """
        self.assertEqual(self.test_player_goalie.get_stats(), [788, 83, 705])


    def test_get_type(self):
        """ 100A: Valid return of get_type() """
        self.assertEqual(self.test_player_goalie.get_type(), "Goalie")


    def test_to_dict_valid(self):
        """ 110A: Valid to_dict() """
        test_dict = self.test_player_goalie.to_dict()

        self.assertEquals(test_dict["fname"], "Roberto", "fname must be Roberto")
        self.assertEquals(test_dict["lname"], "Luongo", "lname must be Luongo")     
        self.assertEquals(test_dict["height"], 190.5, "height must be 190.5")
        self.assertEquals(test_dict["weight"], 215, "weight must be 215")
        self.assertEquals(test_dict["jersey_num"], 1, "jersey_num must be 1")
        self.assertEquals(test_dict["date_birth"], "Apr 4, 1979", "date_birth must be Apr 4, 1979")
        self.assertEquals(test_dict["year_joined"], 1997, "year_joined must be 1997")       
        self.assertEquals(test_dict["shots_against"], 788, "shots_against must be 788")
        self.assertEquals(test_dict["goals_against"], 83, "goals_against must be 83")
        self.assertEquals(test_dict["goals_saved"], 705, "goals saved must be 705")
        self.assertEquals(test_dict["games_played"], 30, "games_played must be 30")
        self.assertEquals(test_dict["games_won"], 12, "games_won must be 12")       
        self.assertEquals(test_dict["games_lost"], 13, "games_lost must be 13")
        self.assertEquals(test_dict["player_type"], "Goalie", "player_type must be Goalie")  


    def tearDown(self):
        self.logPoint()
    

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))