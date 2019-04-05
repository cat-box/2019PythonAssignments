import unittest
from unittest import TestCase
import inspect
import os
from team import Team
from player_forward import PlayerForward
from player_goalie import PlayerGoalie


class TestTeam(TestCase):
    """ Unit Tests for the Team Class """

    TEST_PLAYERS_DB = "test_players.sqlite"
    PLAYER_TYPE_FORWARD = "forward"
    PLAYER_TYPE_GOALIE = "goalie"


    def setUp(self):
        """ Creates test fixture """
        self.logPoint()

        self.team = Team(self.TEST_PLAYERS_DB)
        
        self.forward = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "forward")
        self.forward_id = id(self.forward)
        (self.forward).set_id(self.forward_id)
        
        self.goalie = PlayerGoalie("Roberto", "Luongo", 190.5, 215, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13, "goalie")
        self.goalie_id = id(self.goalie)
        (self.goalie).set_id(self.goalie_id)
        
        self.undefined_value = None
        self.empty_value = ""


    def test_team(self):
        """ 010A: Valid Construction """

        self.assertIsNotNone(self.team, "Team must be defined")


    def test_add(self):
        """ 020A: Valid Add Player """

        self.assertIsNotNone(self.forward, "Player must be defined")

        self.team.add(self.forward)
        num_players = len(self.team.get_all_players())
        self.assertEqual(num_players, 1, "Team must have 1 player")

        self.team.add(self.goalie)
        num_players = len(self.team.get_all_players())
        self.assertEqual(num_players, 2, "Team must have 2 players")


    def test_add_undefined(self):
        """ 020B: Invalid Add Player """

        undefined_player = None
        self.assertRaisesRegex(ValueError, "Player must be defined", self.team.add, undefined_player)


    def test_add_player_already_exists(self):
        """ 020C: Invalid Add Player - Player Already Exists """

        num_players = len(self.team.get_all_players())
        self.assertEqual(num_players, 0, "Team must have no players")

        self.team.add(self.forward)
        num_players = len(self.team.get_all_players())
        self.assertEqual(num_players, 1, "Team must have 1 player")

        self.team.add(self.forward)
        num_players = len(self.team.get_all_players())
        self.assertEqual(num_players, 1, "Team must still only have 1 player")


    def test_delete(self):
        """ 030A: Valid Delete Player """

        self.team.add(self.forward)

        player_list = self.team.get_all_players()

        self.assertEqual(len(player_list), 1, "Team must have 1 player")
        self.assertEqual(player_list[0].get_id(), self.forward_id)

        self.team.delete(self.forward_id)
        self.assertEqual(len(self.team.get_all_players()), 0, "Team must have no players")


    def test_delete_invalid_player_id(self):
        """ 030B: Invalid Delete Player Parameters """

        self.assertRaisesRegex(ValueError, "Player ID cannot be undefined", self.team.delete, self.undefined_value)
        self.assertRaisesRegex(ValueError, "Player ID cannot be empty", self.team.delete, self.empty_value)


    def test_delete_non_existent_player(self):
        """ 030C: Invalid Delete Player - Player is Non-Existent """

        self.team.add(self.forward)

        player_list = self.team.get_all_players()

        self.assertEqual(len(player_list), 1, "Team must have 1 player")
        self.assertEqual(player_list[0].get_id(), self.forward_id)

        self.assertRaisesRegex(ValueError, "Player ID does not exist", self.team.delete, self.goalie_id)
        self.assertEqual(len(self.team.get_all_players()), 1, "Team must have 1 player")


    def test_get_player(self):
        """ 040A: Valid Get Player """

        self.team.add(self.forward)
        
        retrieved_player = self.team.get_player(self.forward_id)
        self.assertEqual(retrieved_player.get_id(), self.forward_id, "Player must have player ID %s" % (self.forward_id))
        self.assertEqual(retrieved_player.get_zone(), "LW", "Player must have zone LW")
        self.assertEqual(retrieved_player.get_stats(), [8, 5, 40], "Player must have stats [8, 5, 40]")


    def test_get_player_invalid_player_id(self):
        """ 040B: Invalid Get Player Parameters """

        self.assertRaisesRegex(ValueError, "Player ID cannot be undefined", self.team.get_player, self.undefined_value)
        self.assertRaisesRegex(ValueError, "Player ID cannot be empty", self.team.get_player, self.empty_value)


    def test_get_player_non_existent(self):
        """ 040C: Invalid Get Player - Player is Non-Existent"""

        self.team.add(self.forward)
        self.team.add(self.goalie)

        self.assertIsNone(self.team.get_player(99), "No player should exist for 99")


    def test_get_all_players(self):
        """ 050A: Valid get_all_players() """

        self.team.add(self.forward)
        self.team.add(self.goalie)

        list_players = self.team.get_all_players()

        self.assertEqual(len(list_players), 2)
        self.assertEqual(list_players[0].get_fname(), "Sven", "Player must have first name 'Sven'")
        self.assertEqual(list_players[1].get_id(), self.goalie_id, "Player must have id %s" % self.goalie_id)


    def test_get_all_players_invalid(self):
        """ 050B: Invalid get_all_players() """
 
        list_players = self.team.get_all_players()
        
        # Check empty list
        self.assertEqual(len(list_players), 0, "Team must have no players")

        self.team.add(self.forward)
        list_players = self.team.get_all_players()

        self.assertIsNotNone(list_players[0], "Player must be defined")


    def test_get_all_by_type(self):
        """ 060A: Valid Get all by Type """

        self.team.add(self.forward)
        self.team.add(self.goalie)

        list_players_forward = self.team.get_all_by_type("Forward")
        list_players_goalie = self.team.get_all_by_type("Goalie")

        self.assertEqual(len(list_players_forward), 1)
        self.assertEqual(list_players_forward[0].get_type(), "Forward", "Player must have Player Type Forward")

        self.assertEqual(len(list_players_goalie), 1)
        self.assertEqual(list_players_goalie[0].get_type(), "Goalie", "Player must have Player Type Goalie")


    def test_get_all_by_type_invalid_player_type(self):
        """ 060B: Invalid Get all by Type Parameters """
        
        self.assertRaisesRegex(ValueError, "Player Type cannot be undefined", self.team.get_all_by_type, self.undefined_value)
        self.assertRaisesRegex(ValueError, "Player Type cannot be empty", self.team.get_all_by_type, self.empty_value)
        self.assertRaisesRegex(ValueError, "Player Type must be Forward or Goalie", self.team.get_all_by_type, "Defense")  


    def test_update(self):
        """ 070A: Valid Update """

        self.team.add(self.forward)
        self.team.add(self.goalie)

        new_forward = PlayerForward("Yann", "Sauve", 190.5, 207.24, 47, "Feb 18, 1990", "2008", "RW", "L", 12, 8, 43, "forward")
        new_forward.set_id(self.forward_id)

        self.team.update(new_forward)

        self.assertEqual(self.team.get_player(self.forward_id).get_full_name(), "Yann Sauve")

    
    def tearDown(self):
        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == "__main__":
	unittest.main()
