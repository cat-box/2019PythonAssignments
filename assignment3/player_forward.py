from sqlalchemy import Column, Integer, String
from abstract_player import AbstractPlayer
import json


class PlayerForward(AbstractPlayer):
    """PlayerForward class
    """
    
    PLAYER_TYPE = "forward"

    zone = Column(String(25))
    shooting_hand = Column(String(1))
    goals = Column(Integer)
    assists = Column(Integer)
    total_shots = Column(Integer)


    def __init__(self, fname, lname, height, weight, jersey_num, date_birth, year_joined, zone, shooting_hand, goals, assists, total_shots, player_type):
        """Constructor method for PlayerForward
        
        Args:
            zone (string): Forward's position on the ice rink
            shooting_hand (string): Player's shooting hand
            goals (int): Number of goals scored
            assists (int): Number of assists 
            total_shots (int): Total number of shots taken 
        """
        self._validate_input(zone, "zone")
        self.zone = zone

        self._validate_input(shooting_hand, "shooting_hand")
        self.shooting_hand = shooting_hand

        self._validate_input(goals, "goals")
        self.goals = goals

        self._validate_input(assists, "assists")
        self.assists = assists
    
        self._validate_input(total_shots, "total_shots")
        self.total_shots = total_shots

        self._validate_player(player_type)

        super().__init__(fname, lname, height, weight, jersey_num, date_birth, year_joined, player_type)

    
    def to_dict(self):
        """Returns dictionary representation of JSON object (PlayerForward)
        
        Returns:
            player_details (dictionary): Dictionary representation of Forward JSON
        """
        player_details = {}

        player_details['id'] = self.id
        player_details["fname"] = self.fname
        player_details["lname"] = self.lname    
        player_details["height"] = self.height  
        player_details["weight"] = self.weight
        player_details["jersey_num"] = self.jersey_num    
        player_details["date_birth"] = self.date_birth
        player_details["year_joined"] = self.year_joined
        player_details["zone"] = self.zone
        player_details["shooting_hand"] = self.shooting_hand
        player_details["goals"] = self.goals
        player_details["assists"] = self.assists
        player_details["total_shots"] = self.total_shots
        player_details["player_type"] = self.player_type

        return player_details

    def copy(self, object):
        """ Copies data from a PlayerForward object to this PlayerForward object """
        if isinstance(object, PlayerForward):
            self.fname = object.fname
            self.lname = object.lname
            self.height = object.height
            self.weight = object.weight
            self.jersey_num = object.jersey_num
            self.date_birth = object.date_birth
            self.year_joined = object.year_joined
            self.zone = object.zone
            self.shooting_hand = object.shooting_hand
            self.goals = object.goals
            self.assists = object.assists
            self.total_shots = object.total_shots
            self.player_type = object.player_type


    @staticmethod
    def _validate_player(value):
        """Private method to validate player_type
        
        Args:
            value (string): Type of player
        
        Raises:
            ValueError: If value is not "forward"
        """

        if value is None:
            raise ValueError("player_type cannot be undefined")

        if value is "":
            raise ValueError("player_type cannot be empty")

        if value.lower() != "forward":
            raise ValueError("player_type must be Forward")
