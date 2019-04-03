from sqlalchemy import Column, Integer, String
from base import Base

class AbstractPlayer(Base):
    """ AbstractPlayer class """

    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    fname = Column(String(25), nullable=False)
    lname = Column(String(25), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    jersey_num = Column(Integer, nullable=False)
    date_birth = Column(String(25), nullable=False)
    year_joined = Column(Integer, nullable=False)


    def __init__(self, fname, lname, height, weight, jersey_num, date_birth, year_joined, player_type):
        """Constructor method for AbstractPlayer
        
        Args:
            fname (string): First name
            lname (string): Last name
            height (float): Height
            weight (float): Weight
            jersey_num (int): Jersey number
            date_birth (string): Date of birth
            year_joined (string): Year joined
            player_type (string): Type of player
        """

        self._id = None

        self._validate_input(fname, "fname")
        self._fname = fname

        self._validate_input(lname, "lname")
        self._lname = lname

        self._validate_input(height, "height")
        self._height = height

        self._validate_input(weight, "weight")
        self._weight = weight

        self._validate_input(jersey_num, "jersey_num")
        self._jersey_num = jersey_num

        self._validate_input(date_birth, "date_birth")
        self._date_birth = date_birth

        self._validate_input(year_joined, "year_joined")
        self._year_joined = year_joined

        self._validate_player_type(player_type)


    def get_id(self):
        """Gets id of player
        
        Returns:
            id (int): Player's id
        """
        return self._id


    def set_id(self, player_id):
        """ sets the player id
        
        Args:
            player_id (int): id of a player object
        """

        self._validate_input(player_id, "Player ID")

        self._id = player_id
        return


    def get_fname(self):
        """Gets first name of player
        
        Returns:
            fname (string): Player's first name
        """
        return self._fname

    
    def get_lname(self):
        """Gets last name of player
        
        Returns:
            lname (string): Player's last name
        """
        return self._lname


    def get_full_name(self):
        """Gets full name of player
        
        Returns:
            full_name (string): Player's full name (concat of first and last names)
        """
        full_name = "%s %s" % (self._fname, self._lname)

        return full_name


    def get_height(self):
        """Gets height of player
        
        Returns:
            height (float): Player's height
        """
        return self._height


    def get_weight(self):
        """Gets weight of player
        
        Returns:
            weight (float): Player's weight
        """
        return self._weight

    
    def get_jersey_num(self):
        """Gets jersey number of player
        
        Returns:
            jersey_num (int): Player's jersey number
        """
        return self._jersey_num

    
    def get_date_birth(self):
        """Gets birth date of player
        
        Returns:
            date_birth (string): Birth date of player
        """
        return self._date_birth


    def get_year_joined(self):
        """Gets join year of player
        
        Returns:
            year_joined (string): Join year of player
        """
        return self._year_joined


    def get_stats(self):
        """Abstract method to be implemented by subclasses
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError("Abstract method - must be implemented in subclass")


    def get_type(self):
        """Abstract method to be implemented by subclasses
        
        Raises:
            NotImplementedError
        """
        raise NotImplementedError("Abstract method - must be implemented in subclass")


    def to_dict(self):
        """Abstract method to be implemented by subclasses
        
        Raises:
            NotImplementedError
        """

        raise NotImplementedError("Abstract method - must be implemented in subclass")


    def copy(self, object):
        """ Abstract method to be implemented by subclasses

        Raises:
            NotImplementedError
        """
        raise NotImplementedError("Abstract method - must be implemented in subclass")


    @staticmethod
    def _validate_input(input, input_display):
        """Private method to validate inputs
        
        Args:
            input: Input to be validated
            input_display (string): String used in ValueError message
        
        Raises:
            ValueError: If input is undefined
            ValueError: If input is empty
        """
        if input == None:
            raise ValueError(input_display + " cannot be undefined")

        if input == "":
            raise ValueError(input_display + " cannot be empty")


    @staticmethod
    def _validate_player_type(value):
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
