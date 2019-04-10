import unittest
from unittest import TestCase
import inspect
import os
from sqlalchemy import create_engine
from base import Base
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

        engine = create_engine("sqlite:///" + self.TEST_PLAYERS_DB)

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.team = Team(self.TEST_PLAYERS_DB)
        
        self.forward = PlayerForward("Sven", "Baertschi", 180.34, 190.0, 47, "Oct 5, 1992", 2011, "LW", "L", 8, 5, 40, "forward")
        # self.forward.id = self.forward_id
        # (self.forward).set_id(self.forward_id)
        
        self.goalie = PlayerGoalie("Roberto", "Luongo", 190.5, 215.0, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13, "goalie")
        # self.goalie.id = self.goalie_id
        # (self.goalie).set_id(self.goalie_id)
        
        self.undefined_value = None
        self.empty_value = ""

        self.logPoint()


    def test_team(self):
        """ 010A: Valid Construction """

        self.assertIsNotNone(self.team, "Team must be defined")


    def test_add(self):
        """ 020A: Valid Add Player """

        self.assertIsNotNone(self.forward, "Player must be defined")

        self.team.add(self.forward)
        self.assertEqual(len(self.team.get_all_players()), 1, "Team must have 1 player")

        self.team.add(self.goalie)
        self.assertEqual(len(self.team.get_all_players()), 2, "Team must have 2 players")


    def test_add_undefined(self):
        """ 020B: Invalid Add Player """

        undefined_player = None
        self.assertRaisesRegex(ValueError, "Player must be defined", self.team.add, undefined_player)


    def test_add_player_already_exists(self):
        """ 020C: Invalid Add Player - Player Already Exists """
    
        self.assertEqual(len(self.team.get_all_players()), 0, "Team must have no players")
    
        self.team.add(self.forward)
        self.assertEqual(len(self.team.get_all_players()), 1, "Team must have 1 player")

        self.team.add(self.forward)
        self.assertEqual(len(self.team.get_all_players()), 1, "Team must still only have 1 player")


    def test_delete(self):
        """ 030A: Valid Delete Player """

        player_id = self.team.add(self.forward)

        self.assertEqual(len(self.team.get_all_players()), 1, "Team must have 1 player")
        # self.assertEqual(player_list[0].get_id(), self.forward_id)
        
        self.team.delete(player_id)
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
        # self.assertEqual(player_list[0].get_id(), self.forward_id)
        
        test_player_id = 12345
        self.assertRaisesRegex(ValueError, "Player ID does not exist", self.team.delete, test_player_id)
        self.assertEqual(len(self.team.get_all_players()), 1, "Team must have 1 player")


    def test_get_player_forward(self):
        """ 040A: Valid Get Player for Forward """

        player_id = self.team.add(self.forward)
        
        retrieved_player = self.team.get_player(player_id)
        
        self.assertEqual(retrieved_player.fname, "Sven", "First name must be Sven")
        self.assertEqual(retrieved_player.lname, "Baertschi", "Last name must be Baertschi")
        self.assertEqual(retrieved_player.height, 180.34, "Height must be 180.34")
        self.assertEqual(retrieved_player.weight, 190, "Weight must be 190")
        self.assertEqual(retrieved_player.jersey_num, 47, "Jersey number must be 47" )
        self.assertEqual(retrieved_player.date_birth, "Oct 5, 1992", "Date of birth must be Oct 5 1992")
        self.assertEqual(retrieved_player.year_joined, 2011, "Year joined must be 2011")
        self.assertEqual(retrieved_player.zone, "LW", "Zone must be LW")
        self.assertEqual(retrieved_player.shooting_hand, "L", "Shooting hand must be L")
        self.assertEqual(retrieved_player.goals, 8, "Goals must be 8")
        self.assertEqual(retrieved_player.assists, 5, "Assists must be 5")
        self.assertEqual(retrieved_player.total_shots, 40, "Total shots must be 40")
        self.assertEqual(retrieved_player.player_type, self.PLAYER_TYPE_FORWARD, "Player type must still be forward")


    def test_get_player_goalie(self):
        """ 040A: Valid Get Player for Goalie """

        player_id = self.team.add(self.goalie)
        
        retrieved_player = self.team.get_player(player_id)
        
        self.assertEqual(retrieved_player.fname, "Roberto", "First name must be Roberto")
        self.assertEqual(retrieved_player.lname, "Luongo", "Last name must be Luongo")
        self.assertEqual(retrieved_player.height, 190.5, "Height must be 190.5")
        self.assertEqual(retrieved_player.weight, 215, "Weight must be 216")
        self.assertEqual(retrieved_player.jersey_num, 1, "Jersey number must be 1" )
        self.assertEqual(retrieved_player.date_birth, "Apr 4, 1979", "Date of birth must be Apr 4 1979")
        self.assertEqual(retrieved_player.year_joined, 1997, "Year joined must be 1997")
        self.assertEqual(retrieved_player.shots_against, 788, "Shots against must be 1768")
        self.assertEqual(retrieved_player.goals_against, 83, "Goals against must be 83")
        self.assertEqual(retrieved_player.goals_saved, 705, "Goals saved must be 705")
        self.assertEqual(retrieved_player.games_played, 30, "Games played must be 30")
        self.assertEqual(retrieved_player.games_won, 12, "Games won must be 12")
        self.assertEqual(retrieved_player.games_lost, 13, "Games lost must be 13")
        self.assertEqual(retrieved_player.player_type, self.PLAYER_TYPE_GOALIE, "Player type must still be goalie")    


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

        forward_player_id = self.team.add(self.forward)
        goalie_player_id = self.team.add(self.goalie)

        list_players = self.team.get_all_players()

        self.assertEqual(len(list_players), 2)
        self.assertEqual(list_players[0].fname, "Sven", "Player must have first name 'Sven'")
        self.assertEqual(list_players[1].id, goalie_player_id, "Player must have id %s" % goalie_player_id)


    def test_get_all_players_invalid(self):
        """ 050B: Invalid get_all_players() """
        
        # Check empty list
        self.assertEqual(len(self.team.get_all_players()), 0, "Team must have no players")

        self.team.add(self.forward)
        list_players = self.team.get_all_players()

        self.assertIsNotNone(list_players[0], "Player must be defined")


    def test_get_all_by_type(self):
        """ 060A: Valid Get all by Type """

        self.team.add(self.forward)
        self.team.add(self.goalie)

        list_players_forward = self.team.get_all_by_type(self.PLAYER_TYPE_FORWARD)
        list_players_goalie = self.team.get_all_by_type(self.PLAYER_TYPE_GOALIE)

        self.assertEqual(len(list_players_forward), 1)
        self.assertEqual(list_players_forward[0].player_type, "forward", "Player must have Player Type Forward")

        self.assertEqual(len(list_players_goalie), 1)
        self.assertEqual(list_players_goalie[0].player_type, "goalie", "Player must have Player Type Goalie")


    def test_get_all_by_type_invalid_player_type(self):
        """ 060B: Invalid Get all by Type Parameters """
        
        self.assertRaisesRegex(ValueError, "Player Type cannot be undefined", self.team.get_all_by_type, self.undefined_value)
        self.assertRaisesRegex(ValueError, "Player Type cannot be empty", self.team.get_all_by_type, self.empty_value)
        self.assertRaisesRegex(ValueError, "Player Type must be Forward or Goalie", self.team.get_all_by_type, "Defense")  


    def test_update_forward(self):
        """ 070A: Valid Update for Forward """

        player_id = self.team.add(self.forward)
        
        retrieved_player = self.team.get_player(player_id)
        retrieved_player.fname = "Yann"
        retrieved_player.lname = "Sauve"
        retrieved_player.height = 190.5
        retrieved_player.weight = 207.24
        retrieved_player.jersey_num = 47
        retrieved_player.date_birth = "Feb 18, 1990"
        retrieved_player.year_joined = 2008
        retrieved_player.zone = "RW"
        retrieved_player.shooting_hand = "L"
        retrieved_player.goals = 12
        retrieved_player.assists = 8
        retrieved_player.total_shots = 43
        retrieved_player.player_type = self.PLAYER_TYPE_FORWARD

        self.team.update(retrieved_player)

        updated_player = self.team.get_player(player_id)
        self.assertEqual(updated_player.fname, "Yann", "First name must be Yann")
        self.assertEqual(updated_player.lname, "Sauve", "Last name must be Sauve")
        self.assertEqual(updated_player.height, 190.5, "Height must be 190.5")
        self.assertEqual(updated_player.weight, 207.24, "Weight must be 207.24")
        self.assertEqual(updated_player.jersey_num, 47, "Jersey number must be 47" )
        self.assertEqual(updated_player.date_birth, "Feb 18, 1990", "Date of birth must be Feb 18 1990")
        self.assertEqual(updated_player.year_joined, 2008, "Year joined must be 2008")
        self.assertEqual(updated_player.zone, "RW", "Zone must be RW")
        self.assertEqual(updated_player.shooting_hand, "L", "Shooting hand must be L")
        self.assertEqual(updated_player.goals, 12, "Goals must be 12")
        self.assertEqual(updated_player.assists, 8, "Assists must be 8")
        self.assertEqual(updated_player.total_shots, 43, "Total shots must be 43")
        self.assertEqual(updated_player.player_type, self.PLAYER_TYPE_FORWARD, "Player type must still be forward")


    def test_update_goalie(self):
        """ 070B: Valid update for Goalie """

        player_id = self.team.add(self.goalie)
        
        retrieved_player = self.team.get_player(player_id)
        retrieved_player.fname = "Jacob"
        retrieved_player.lname = "Markstrom"
        retrieved_player.height = 201.17
        retrieved_player.weight = 206
        retrieved_player.jersey_num = 25
        retrieved_player.date_birth = "Jan 31, 1990"
        retrieved_player.year_joined = 2018
        retrieved_player.shots_against = 1768
        retrieved_player.goals_against = 153
        retrieved_player.goals_saved = 1614
        retrieved_player.games_played = 56
        retrieved_player.games_won = 27
        retrieved_player.games_lost = 20
        retrieved_player.player_type = self.PLAYER_TYPE_GOALIE

        self.team.update(retrieved_player)

        updated_player = self.team.get_player(player_id)
        self.assertEqual(updated_player.fname, "Jacob", "First name must be Jacob")
        self.assertEqual(updated_player.lname, "Markstrom", "Last name must be Markstrom")
        self.assertEqual(updated_player.height, 201.17, "Height must be 201.17")
        self.assertEqual(updated_player.weight, 206, "Weight must be 206")
        self.assertEqual(updated_player.jersey_num, 25, "Jersey number must be 25" )
        self.assertEqual(updated_player.date_birth, "Jan 31, 1990", "Date of birth must be Jan 31 1990")
        self.assertEqual(updated_player.year_joined, 2018, "Year joined must be 2018")
        self.assertEqual(updated_player.shots_against, 1768, "Shots against must be 1768")
        self.assertEqual(updated_player.goals_against, 153, "Goals against must be 153")
        self.assertEqual(updated_player.goals_saved, 1614, "Goals saved must be 1614")
        self.assertEqual(updated_player.games_played, 56, "Games played must be 56")
        self.assertEqual(updated_player.games_won, 27, "Games won must be 27")
        self.assertEqual(updated_player.games_lost, 20, "Games lost must be 20")
        self.assertEqual(updated_player.player_type, self.PLAYER_TYPE_GOALIE, "Player type must still be goalie")    


    def tearDown(self):
        os.remove(self.TEST_PLAYERS_DB)

        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))


if __name__ == "__main__":
	unittest.main()
