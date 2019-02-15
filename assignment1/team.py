class Team:

    def __init__(self):
        self._team_players = []


    def add(self, player_obj):
        self._validate_object(player_obj)

        if self._player_exists(player_obj.get_id()) is False:
            self._team_players.append(player_obj)
        
        return


    def delete(self, player_id):
        self._validate_parameter(player_id, "Player ID")

        if self._player_exists(player_id) is True:
            for player in self._team_players:
                if player.get_id() is player_id:
                    self._team_players.remove(player)
        
        return


    def get_player(self, player_id):
        self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player.get_id() is player_id:
                return player

        return None


    def get_all_players(self):
        if len(self._team_players) is 0:
            return []
        else:
            return self._team_players


    def get_all_by_type(self, player_type):   
        self._validate_parameter(player_type, "Player Type")
        self._validate_type(player_type)

        if len(self._team_players) is 0:
            return []

        player_of_type = []

        player_of_type = [player for player in self._team_players if player.get_type() is player_type]
        
        return player_of_type


    def update(self, player_obj):

        player_id = player_obj.get_id()

        if self._player_exists(player_id) is False:
            raise ValueError("Player ID does not already exist")

        for index, player in enumerate(self._team_players, 0):
            if player.get_id() is player_id:
                old_player = player
                break

        self._team_players[index] = player_obj


    def _player_exists(self, player_id):
        self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player.get_id() is player_id:
                return True
            
        return False


    @staticmethod
    def _validate_object(obj):
        if obj is None:
            raise ValueError("Player must be defined")

    
    @staticmethod
    def _validate_parameter(value, name):
        if value is None:
            raise ValueError("%s cannot be undefined" % (name))
        
        if value is "":
            raise ValueError("%s cannot be empty" % (name))

    
    @staticmethod
    def _validate_type(value):
        if (value is "Forward") or (value is "Goalie"):
            return
        else:
            raise ValueError("Player Type must be Forward or Goalie")