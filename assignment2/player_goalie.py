from abstract_player import AbstractPlayer


class PlayerGoalie(AbstractPlayer):
    """PlayerGoalie class
    """
    PLAYER_TYPE = "Goalie"


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
        self._shots_against = shots_against

        self._validate_input(goals_against, "goals_against")
        self._goals_against = goals_against

        self._validate_input(goals_saved, "goals_saved")
        self._goals_saved = goals_saved
    
        self._validate_input(games_played, "games_played")
        self._games_played = games_played

        self._validate_input(games_won, "games_won")
        self._games_won = games_won

        self._validate_input(games_lost, "games_lost")
        self._games_lost = games_lost

        self._validate_player(player_type)
        self._player_type = self.PLAYER_TYPE

        super().__init__(fname, lname, height, weight, jersey_num, date_birth, year_joined, player_type)


    def get_shots_against(self):
        """Gets number of shots taken against player
        
        Returns:
            shots_against (int): Player's number of shots against
        """
        return self._shots_against


    def get_goals_against(self):
        """Gets number of goals scored against player
        
        Returns:
            goals_against (int): Player's number of goals against
        """
        return self._goals_against


    def get_goals_saved(self):
        """Gets number of goals saved by player
        
        Returns:
            goals_saved (int): Player's number of goals saved
        """
        return self._goals_saved


    def get_games_played(self):
        """Gets number of games played by player
        
        Returns:
            games_played (int): Player's number of games played
        """
        return self._games_played


    def get_games_won(self):
        """Gets number of games won by player
        
        Returns:
            games_won (int): Player's number of games won
        """
        return self._games_won


    def get_games_lost(self):
        """Gets number of games lost
        
        Returns:
            games_lost (int): Player's number of games lost
        """
        return self._games_lost


    def get_win_loss_stats(self):
        """Gets win/loss stats of player
        
        Returns:
            (list): List containing player's number of games won, lost, and total played
        """
        return [self._games_won, self._games_lost, self._games_played]

    
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

    
    def get_stats(self):
        """Gets goal stats of player
        
        Returns:
            (list): List containing number of shots and goals against player, and goals saved
        """
        return [self._shots_against, self._goals_against, self._goals_saved]
    

    def get_type(self):
        """Gets player's type
        
        Returns:
            PLAYER_TYPE (string): Player's type ("Goalie")
        """
        return self.PLAYER_TYPE


    def to_dict(self):
        """ Returns a Python dictionary representation of data held in player_goalie
        
        Returns:
            dict: player details in dictionary format
        """

        player_details = {self._id: {}}

        player_details[self._id]['fname'] = self._fname
        player_details[self._id]['lname'] = self._lname
        player_details[self._id]['height'] = self._height
        player_details[self._id]['weight'] = self._weight
        player_details[self._id]['jersey_num']  = self._jersey_num
        player_details[self._id]['date_birth'] = self._date_birth
        player_details[self._id]['year_joined'] = self._year_joined
        player_details[self._id]['shots_against'] = self._shots_against
        player_details[self._id]['goals_against'] = self._goals_against
        player_details[self._id]['goals_saved'] = self._goals_saved
        player_details[self._id]['games_played'] = self._games_played
        player_details[self._id]['games_won'] = self._games_won
        player_details[self._id]['games_lost'] = self._games_lost
        player_details[self._id]["player_type"] = self._player_type

        return player_details

    @staticmethod
    def _validate_player(value):
        if value.lower() != "goalie":
            raise ValueError("Player type must be Goalie")
