from sqlalchemy import Column, Integer, String
from abstract_player import AbstractPlayer
import json

class PlayerGoalie(AbstractPlayer):
    """PlayerGoalie class
    """

    PLAYER_TYPE = "goalie"

    shots_against = Column(Integer)
    goals_against = Column(Integer)
    goals_saved = Column(Integer)
    games_played = Column(Integer)
    games_won = Column(Integer)
    games_lost = Column(Integer)


    def __init__(self, fname, lname, height, weight, jersey_num, date_birth, year_joined, shots_against, goals_against, goals_saved, games_played, games_won, games_lost, player_type):
        """Constructor method for PlayerGoalie
        
        Args:
            shots_against (int): Number of shots taken against
            goals_against (int): Number of goals scored against
            goals_saved (int): Number of goals saved
            games_played (int): Number of games played
            games_won (int): Number of games won
            games_lost (int): Number of games lost
        """
        self._validate_input(shots_against, "shots_against")
        self.shots_against = shots_against

        self._validate_input(goals_against, "goals_against")
        self.goals_against = goals_against

        self._validate_input(goals_saved, "goals_saved")
        self.goals_saved = goals_saved
    
        self._validate_input(games_played, "games_played")
        self.games_played = games_played

        self._validate_input(games_won, "games_won")
        self.games_won = games_won

        self._validate_input(games_lost, "games_lost")
        self.games_lost = games_lost

        self._validate_player(player_type)

        super().__init__(fname, lname, height, weight, jersey_num, date_birth, year_joined, player_type)

    
    def set_win_loss_stats(self, wins, losses, games_played):
        """Sets win/loss stats of player
        
        Args:
            wins (int): Value for player's number of wins
            losses (int): Value for player's number of losses
            games_played (int): Value for player's number of total games played
        """
        self._validate_input(wins, "wins")
        self._games_won = wins

        self._validate_input(losses, "losses")
        self._games_lost = losses

        self._validate_input(games_played, "games_played")
        self._games_played = games_played


    def get_type(self):
        """Gets player's type
        
        Returns:
            PLAYER_TYPE (string): Player's type ("Goalie")
        """
        return self.PLAYER_TYPE


    def to_dict(self):
        """ Returns a Python dictionary representation of data held in player_goalie
        
        Returns:
            player_details (dictionary): Player details in dictionary format
        """

        player_details = {}

        player_details['id'] = self.id
        player_details['fname'] = self.fname
        player_details['lname'] = self.lname
        player_details['height'] = self.height
        player_details['weight'] = self.weight
        player_details['jersey_num']  = self.jersey_num
        player_details['date_birth'] = self.date_birth
        player_details['year_joined'] = self.year_joined
        player_details['shots_against'] = self.shots_against
        player_details['goals_against'] = self.goals_against
        player_details['goals_saved'] = self.goals_saved
        player_details['games_played'] = self.games_played
        player_details['games_won'] = self.games_won
        player_details['games_lost'] = self.games_lost
        player_details["player_type"] = self.player_type

        return player_details


    def copy(self, object):
        """ Copies data from a PlayerForward object to this PlayerForward object """
        if isinstance(object, PlayerGoalie):
            self.fname = object.fname
            self.lname = object.lname
            self.height = object.height
            self.weight = object.weight
            self.jersey_num = object.jersey_num
            self.date_birth = object.date_birth
            self.year_joined = object.year_joined
            self.shots_against = object.shots_against
            self.goals_against = object.goals_against
            self.goals_saved = object.goals_saved
            self.games_played = object.games_played
            self.games_won = object.games_won
            self.games_lost = object.games_lost
            self.player_type = object.player_type


    @staticmethod
    def _validate_player(value):
        """Private method to validate player_type
        
        Args:
            value (string): Type of player 
        
        Raises:
            ValueError: If value is not "goalie"
        """

        if value is None:
            raise ValueError("player_type cannot be undefined")

        if value is "":
            raise ValueError("player_type cannot be empty")

        if value.lower() != "goalie":
            raise ValueError("player_type must be Goalie")
