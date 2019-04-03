#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import json

from abstract_player import AbstractPlayer
from player_forward import PlayerForward
from player_goalie import PlayerGoalie

class Team:
    """Team Class """

    def __init__(self, db_filename):
        """Constructor method for Team """

        if db_filename is None or db_filename == "":
            raise ValueError("Invalid Database File")

        engine = create_engine('sqlite:///' + db_filename)

        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)


    def add(self, player_obj):
        """Adds player to database of team players if id doesn't exist in database
           Generates an id for the player on successful add, then returns that id

        Args:
            player_obj (PlayerForward or PlayerGoalie): Either a forward or goalie class
        
        Returns:
            _id (int): id that is generated on successful add
        """

        self._validate_object(player_obj)

        session = self._db_session()

        player_id = self.create_id(player_obj)

        if self._player_exists(player_id) is False:
            session.add(player_obj)
            session.close()
            return player_obj.get_id()

        session.close()
        return


    def create_id(self, player_obj):
        """ Creates an id for a player
        
        Returns:
            player_id (int): id of a player object
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
        
        Raises:
            ValueError: If player_id is not in _team_players list
        """

        self._validate_parameter(player_id, "Player ID")

        if self._player_exists(player_id) is True:
            session = self._db_session()

            existing_player = session.query(AbstractPlayer).filter(AbstractPlayer.id == player_id).first()
        
        raise ValueError("Player ID does not exist")


    def get_player(self, player_id):
        """Returns player object if player's id is in list
        
        Args:
            player_id (int): Player id of player to return
        
        Returns:
            player (PlayerForward or PlayerGoalie): Player object that is returned
        """

        self._validate_parameter(player_id, "Player ID")

        for player in self._team_players:
            if player.get_id() == int(player_id):
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

        player_of_type = [player for player in self._team_players if player.get_type().lower() == player_type.lower()]
        
        return player_of_type


    def update(self, player_obj):
        """Updates list to replace a Player object with new Player object through their id
           Then, calls _write_player_to_file() to update the file that contains the
           representations of player objects

        Args:
            player_obj (PlayerForward or PlayerGoalie): Player object to replace
        
        Raises:
            ValueError: If player_id is not in list of players
        """

        player_id = player_obj.get_id()

        if self._player_exists(player_id) is False:
            raise ValueError("Player ID does not already exist")

        for index, player in enumerate(self._team_players, 0):
            if player.get_id() == player_id:
                break

        self._team_players[index] = player_obj
        self._write_player_to_file()


    def _player_exists(self, player_id):
        """Private method to check if player exists in _team_players
        
        Args:
            player_id (int): Player's id to be checked
        
        Returns:
            (Boolean): True if id does exist in list, False otherwise
        """

        self._validate_parameter(player_id, "Player ID")

        # for player in self._team_players:
        #     if player.get_id() == player_id:
        #         return True

        # return False

        session = self._db_session()
        existing_player = session.query(AbstractPlayer).filter(AbstractPlayer.id == player_id).first()

        if existing_player is None:
            session.close()
            return False

        return True


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

        if (value.lower() == "forward") or (value.lower() == "goalie"):
            return
        else:
            raise ValueError("Player Type must be Forward or Goalie")
