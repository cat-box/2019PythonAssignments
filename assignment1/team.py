class Team:
    """Team class
    """

    def __init__(self):
        """Constructor method for Team
        """
        self._team_players = []


    def add(self, player_obj):
        """Adds player to list of team players if id doesn't exist in list
        
        Args:
            player_obj (PlayerForward or PlayerGoalie): Either a forward or goalie class
        """

        self._validate_object(player_obj)

        if self._player_exists(player_obj.get_id()) is False:
            self._team_players.append(player_obj)
        
        return


    def delete(self, player_id):
        """Deletes player from list if id doesn't exist in list
           Iterates through list to match the given player_id, then removes it
        
        Args:
            player_id (int): Player id that is used to remove player from list
        """

        self._validate_parameter(player_id, "Player ID")

        if self._player_exists(player_id) is True:
            for player in self._team_players:
                if player.get_id() is player_id:
                    self._team_players.remove(player)
        
        return


    def get_player(self, player_id):
        """Returns player object if player's id is in list
        
        Args:
            player_id (int): Player id of player to return
        
        Returns:
            player (PlayerForward or PlayerGoalie): Player object that is returned
        """

        self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player.get_id() is player_id:
                return player

        return None


    def get_all_players(self):
        """Returns a list containing the Player objects that are stored in it
           An empty list is returned if there's nothing in _team_players
        
        Returns:
            _team_players (list): List of Player objects
        """

        if len(self._team_players) is 0:
            return []
        else:
            return self._team_players


    def get_all_by_type(self, player_type):
        """Returns a list of players of a certain type (forward or goalie)
        
        Args:
            player_type (string): Type of player (either "forward" or "goalie")
        
        Returns:
            player_of_type (list): List containing Player objects of the given player_type
        """

        self._validate_parameter(player_type, "Player Type")
        self._validate_type(player_type)

        if len(self._team_players) is 0:
            return []

        player_of_type = []

        player_of_type = [player for player in self._team_players if player.get_type() is player_type]
        
        return player_of_type


    def update(self, player_obj):
        """Updates list to replace a Player object with new Player object through their id
        
        Args:
            player_obj (PlayerForward or PlayerGoalie): Player object to replace
        
        Raises:
            ValueError: If player_id is not in list of players
        """
        player_id = player_obj.get_id()

        if self._player_exists(player_id) is False:
            raise ValueError("Player ID does not already exist")

        for index, player in enumerate(self._team_players, 0):
            if player.get_id() is player_id:
                old_player = player
                break

        self._team_players[index] = player_obj


    def _player_exists(self, player_id):
        """Private method to check if player exists in _team_players
        
        Args:
            player_id (int): Player's id to be checked
        
        Returns:
            (boolean): True if id does exist in list, False otherwise
        """
        self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player.get_id() is player_id:
                return True
            
        return False


    @staticmethod
    def _validate_object(obj):
        """Private method to help validate object inputs
        
        Args:
            obj (obj): Input to be validated
        
        Raises:
            ValueError: If obj is undefined
        """
        if obj is None:
            raise ValueError("Player must be defined")

    
    @staticmethod
    def _validate_parameter(value, name):
        """Private method to validate inputs
        
        Args:
            value: Input to be validated
            name: Name of input
        
        Raises:
            ValueError: If value is undefined
            ValueError: If value is not given
        """

        if value is None:
            raise ValueError("%s cannot be undefined" % (name))
        
        if value is "":
            raise ValueError("%s cannot be empty" % (name))

    
    @staticmethod
    def _validate_type(value):
        """Private method to validate player type
        
        Args:
            value (string): Type of player (either "Forward" or "Goalie")
        
        Raises:
            ValueError: If value is neither "Forward" or "Goalie"
        """

        if (value is "Forward") or (value is "Goalie"):
            return
        else:
            raise ValueError("Player Type must be Forward or Goalie")