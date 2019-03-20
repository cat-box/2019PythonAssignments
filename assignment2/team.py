import json

class Team:
    """Team Class
    """

    def __init__(self, filepath):
        """Constructor method for Team
        """
        self._validate_parameter(filepath, "filepath")
        self._filepath = filepath

        self._team_players = []

        self._read_player_from_file()


    def add(self, player_obj):
        """Adds player to list of team players if id doesn't exist in list
        
        Args:
            player_obj (PlayerForward or PlayerGoalie): Either a forward or goalie class
        """

        self._validate_object(player_obj)

        player_id = self.create_id(player_obj)

        #if self._player_exists(player_id) is False:
        #    self._team_players.append({"test":"abc"})
        #    self._team_players.append(player_obj)
        #    return player_obj.get_id()

        print(self._team_players)

        return

    def create_id(self, player_obj):
        """ Creates an id for a player
        
        Returns:
            int: id of a player object
        """
        self._validate_object(player_obj)

        player_id = id(player_obj)
        player_obj.set_id(player_id)

        return player_id


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
        
        raise Exception("Player ID does not exist")


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
                break

        self._team_players[index] = player_obj


    def _player_exists(self, player_id):
        """Private method to check if player exists in _team_players
        
        Args:
            player_id (int): Player's id to be checked
        
        Returns:
            (boolean): True if id does exist in list, False otherwise
        """
        # self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player is player_id:
                return True

        return False


    def _read_player_from_file(self):
        # TODO: When you EntityManager is constructed (i.e., __init__), this method will load the JSON Entity records from the file at _filepath into your list of entities (i.e., _entities instance variable).
        #       Make sure it creates the correct type of Entity (SpecificEntity1 or SpecificEntity2).

        with open(self._filepath) as player_file:
            players_obj = json.load(player_file)

            for key, value in players_obj.items():
                self._team_players.append({key: value})

            print(len(self._team_players))

        return


    def _write_player_to_file(self):
        # TODO: In any method that modifies an Entity object in your list of entities (i.e., _entities instance variable), this method is called.
        #       The first thing this method will do is open the file at _filepath for writing (such that the existing data will be overwritten).
        #       For each Entity record in _entities:
        #           o It will call the to_dict() method to get the Python dictionary will all the attributes for the SpecificEntity
        #           o It will serialize the Python dictionary to a JSON representation
        #           o The JSON representation is written as a string to a single line in the file
        pass


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

        if (value.lower() is "forward") or (value.lower() is "goalie"):
            return
        else:
            raise ValueError("Player Type must be Forward or Goalie")
