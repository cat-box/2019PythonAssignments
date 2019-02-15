import unittest
from unittest import TestCase
import inspect
from player_forward import PlayerForward


class TestPlayerForward(TestCase):
    """ Unit tests for PlayerForward clas """


    def setUp(self):
        self.logPoint()
        self.test_player_forward = PlayerForward(47, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40)
    

    def test_player_forward_valid(self):
        """ 010A: Valid values for constructor """
        self.logPoint()
        self.assertIsNotNone(self.test_player_forward)


    def test_get_zone(self):
        """ 020A: Valid return for get_zone() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_zone(), "LW")


    def test_get_shooting_hand(self):
        """ 030A: Valid return of get_shooting_hand() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_shooting_hand(), "L")
    

    def test_get_goals(self):
        """ 040A: Valid return of get_goals() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_goals(), 8)

    
    def test_get_assists(self):
        """ 050A: Valid return of get_assists() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_assists(), 5)
    

    def test_get_total_shots(self):
        """ 060A: Valid return of get_total_shots() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_total_shots(), 40)


    def test_get_stats(self):
        """ 070A: Valid return of get_stats() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_stats(), [8, 5, 40])
    

    def test_get_type(self):
        """ 080A: Valid return of get_type() """
        self.logPoint()
        self.assertEqual(self.test_player_forward.get_type(), "Forward")


    def tearDown(self):
        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))
    

