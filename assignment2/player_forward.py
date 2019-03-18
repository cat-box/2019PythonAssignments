from abstract_player import AbstractPlayer


class PlayerForward(AbstractPlayer):
    """PlayerForward class
    """
    PLAYER_TYPE = "Forward"


    def __init__(self, fname, lname, height, weight, jersey_num, date_birth, year_joined, zone, shooting_hand, goals, assists, total_shots):
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

        super().__init__(fname, lname, height, weight, jersey_num, date_birth, year_joined)


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