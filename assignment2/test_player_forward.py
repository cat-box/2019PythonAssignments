import unittest
from unittest import TestCase
import inspect
from player_forward import PlayerForward


class TestPlayerForward(TestCase):
    """ Unit tests for PlayerForward class """


    def setUp(self):
        self.logPoint()
        self.test_player_forward = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        

    def test_player_forward_valid(self):
        """ 010A: Valid values for constructor """
        self.assertIsNotNone(self.test_player_forward)


    def test_player_forward_invalid_undefined(self):
        """ 010B: Invalid values (undefined) for constructor """
        self.assertRaisesRegex(ValueError, "fname cannot be undefined", PlayerForward, None, "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")

    def test_get_zone(self):
        """ 020A: Valid return for get_zone() """
        self.assertEqual(self.test_player_forward.get_zone(), "LW")


    def test_get_shooting_hand(self):
        """ 030A: Valid return of get_shooting_hand() """
        self.assertEqual(self.test_player_forward.get_shooting_hand(), "L")
    

    def test_get_goals(self):
        """ 040A: Valid return of get_goals() """
        self.assertEqual(self.test_player_forward.get_goals(), 8)

    
    def test_get_assists(self):
        """ 050A: Valid return of get_assists() """
        self.assertEqual(self.test_player_forward.get_assists(), 5)
    

    def test_get_total_shots(self):
        """ 060A: Valid return of get_total_shots() """
        self.assertEqual(self.test_player_forward.get_total_shots(), 40)


    def test_get_stats(self):
        """ 070A: Valid return of get_stats() """
        self.assertEqual(self.test_player_forward.get_stats(), [8, 5, 40])
    

    def test_get_type(self):
        """ 080A: Valid return of get_type() """
        self.assertEqual(self.test_player_forward.get_type(), "Forward")


    def test_to_dict_valid(self):
        """ 090A: Valid to_dict() """
        test_dict = self.test_player_forward.to_dict()

        self.assertEquals(test_dict["fname"], "Sven", "fname must be Sven")
        self.assertEquals(test_dict["lname"], "Baertschi", "lname must be Baertschi")     
        self.assertEquals(test_dict["height"], 180.34, "height must be 180.34")
        self.assertEquals(test_dict["weight"], 190, "weight must be 190")
        self.assertEquals(test_dict["jersey_num"], 47, "jersey_num must be 47")
        self.assertEquals(test_dict["date_birth"], "Oct 5, 1992", "date_birth must be Oct 5, 1992")
        self.assertEquals(test_dict["year_joined"], "2011", "year_joined must be 2011")       
        self.assertEquals(test_dict["zone"], "LW", "zone must be LW")
        self.assertEquals(test_dict["shooting_hand"], "L", "shooting_hand must be L")
        self.assertEquals(test_dict["goals"], 8, "goals must be 8")
        self.assertEquals(test_dict["assists"], 5, "assists must be 5")
        self.assertEquals(test_dict["total_shots"], 40, "total_shots must be 40")       
        self.assertEquals(test_dict["player_type"], "Forward", "player_type must be Forward")  


    def tearDown(self):
        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))