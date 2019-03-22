import unittest
from unittest import TestCase
import inspect
from player_forward import PlayerForward


class TestPlayerForward(TestCase):
    """ Unit tests for PlayerForward class """


    def setUp(self):
        self.logPoint()
        self.test_player_forward = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.none_value = None
        self.empty_value = ""

    def test_player_forward_valid(self):
        """ 010A: Valid values for constructor """
        self.assertIsNotNone(self.test_player_forward)


    def test_player_forward_invalid_undefined(self):
        """ 010B: Invalid values for constructor """
        self.assertRaisesRegex(ValueError, "fname cannot be undefined", PlayerForward, self.none_value, "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "lname cannot be undefined", PlayerForward, "Sven", self.none_value, 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "height cannot be undefined", PlayerForward, "Sven", "Baertschi", self.none_value, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "weight cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, self.none_value, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "jersey_num cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, self.none_value, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "date_birth cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, self.none_value, "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "year_joined cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", self.none_value, "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "zone cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", self.none_value, "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "shooting_hand cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", self.none_value, 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "goals cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", self.none_value, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "assists cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, self.none_value, 40, "Forward")
        self.assertRaisesRegex(ValueError, "total_shots cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, self.none_value, "Forward")
        self.assertRaisesRegex(ValueError, "player_type cannot be undefined", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, self.none_value)


    def test_player_forward_invalid_empty(self):
        """ 010C: Empty values for constructor """
        self.assertRaisesRegex(ValueError, "fname cannot be empty", PlayerForward, self.empty_value, "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "lname cannot be empty", PlayerForward, "Sven", self.empty_value, 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "height cannot be empty", PlayerForward, "Sven", "Baertschi", self.empty_value, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "weight cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, self.empty_value, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "jersey_num cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, self.empty_value, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "date_birth cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, self.empty_value, "2011", "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "year_joined cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", self.empty_value, "LW", "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "zone cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", self.empty_value, "L", 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "shooting_hand cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", self.empty_value, 8, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "goals cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", self.empty_value, 5, 40, "Forward")
        self.assertRaisesRegex(ValueError, "assists cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, self.empty_value, 40, "Forward")
        self.assertRaisesRegex(ValueError, "total_shots cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, self.empty_value, "Forward")
        self.assertRaisesRegex(ValueError, "player_type cannot be empty", PlayerForward, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, self.empty_value)


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
