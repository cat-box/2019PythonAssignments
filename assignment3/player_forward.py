from abstract_player import AbstractPlayer
import json


class PlayerForward(AbstractPlayer):
    """PlayerForward class
    """
    PLAYER_TYPE = "Forward"


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
        self._zone = zone

        self._validate_input(shooting_hand, "shooting_hand")
        self._shooting_hand = shooting_hand

        self._validate_input(goals, "goals")
        self._goals = goals

        self._validate_input(assists, "assists")
        self._assists = assists
    
        self._validate_input(total_shots, "total_shots")
        self._total_shots = total_shots

        self._validate_player(player_type)
        self._player_type = self.PLAYER_TYPE

        super().__init__(fname, lname, height, weight, jersey_num, date_birth, year_joined, player_type)


    def get_zone(self):
        """Gets zone of player
        
        Returns:
            zone (string): Player's zone
        """
        return self._zone


    def get_shooting_hand(self):
        """Gets shooting hand of player
        
        Returns:
            shooting hand (string): Player's shooting hand
        """
        return self._shooting_hand

    
    def get_goals(self):
        """Gets number of goals from player
        
        Returns:
            goals (int): Player's number of goals
        """
        return self._goals
    

    def get_assists(self):
        """Gets number of assists from player
        
        Returns:
            assists (int): Player's number of assists
        """
        return self._assists


    def get_total_shots(self):
        """Gets number of total shots from player
        
        Returns:
            total_shots (int): Player's total number of shots
        """
        return self._total_shots


    def get_stats(self):
        """Gets a list of player's stats
        
        Returns:
            (list): List containing player's number of goals, assists, and total shots
        """
        return [self._goals, self._assists, self._total_shots]


    def get_type(self):
        """Gets player's type
        
        Returns:
            PLAYER_TYPE (string): Player's type ("Forward")
        """
        return self.PLAYER_TYPE

    
    def to_dict(self):
        """Returns dictionary representation of JSON object (PlayerForward)
        
        Returns:
            player_details (dictionary): Dictionary representation of Forward JSON
        """
        player_details = {}

        player_details['id'] = self._id
        player_details["fname"] = self._fname
        player_details["lname"] = self._lname    
        player_details["height"] = self._height  
        player_details["weight"] = self._weight
        player_details["jersey_num"] = self._jersey_num    
        player_details["date_birth"] = self._date_birth
        player_details["year_joined"] = self._year_joined
        player_details["zone"] = self._zone
        player_details["shooting_hand"] = self._shooting_hand
        player_details["goals"] = self._goals
        player_details["assists"] = self._assists
        player_details["total_shots"] = self._total_shots
        player_details["player_type"] = self._player_type

        return player_details


    def copy(self, object):
        """ Copies data from a PlayerForward object to this PlayerForward object """
        if isinstance(object, PlayerForward):
            self._fname = object.get_fname()
            self._lname = object.get_lname()
            self._height = object.get_height()
            self._weight = object.get_weight()
            self._jersey_num = object.get_jersey_num()
            self._date_birth = object.get_date_birth()
            self._year_joined = object.get_year_joined()
            self._zone = object.get_zone()
            self._shooting_hand = object.get_shooting_hand()
            self._goals = object.get_goals()
            self._assists = object.get_assists()
            self._total_shots = object.get_total_shots()
            self._player_type = object.get_player_type()

    
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
