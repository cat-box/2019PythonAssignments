from sqlalchemy import Column, Integer, String, Float
from base import Base


class AbstractPlayer(Base):
    """AbstractPlayer class
    """

    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    fname = Column(String(25), nullable=False)
    lname = Column(String(25), nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    jersey_num = Column(Integer, nullable=False)
    date_birth = Column(String(25), nullable=False)
    year_joined = Column(Integer, nullable=False)
    player_type = Column(String(25), nullable=False)


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
        self._validate_string(fname, "fname")
        self.fname = fname

        self._validate_input(lname, "lname")
        self._validate_string(lname, "lname")
        self.lname = lname

        self._validate_input(height, "height")
        self._validate_int(height, "height")
        self.height = height

        self._validate_input(weight, "weight")
        self._validate_int(weight, "weight'")
        self.weight = weight

        self._validate_input(jersey_num, "jersey_num")
        self._validate_int(jersey_num, "jersey_num")
        self.jersey_num = jersey_num

        self._validate_input(date_birth, "date_birth")
        self._validate_string(date_birth, "date_birth")
        self.date_birth = date_birth

        self._validate_input(year_joined, "year_joined")
        self._validate_int(year_joined, "year_joined")
        self.year_joined = year_joined

        self._validate_player_type(player_type)
        self._validate_string(player_type, "player_type")
        self.player_type = player_type.lower()
        

    def to_dict(self):
        """Abstract method to be implemented by subclasses
        
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

    
    @staticmethod
    def _validate_string(input, input_display):
        """Private method to check if input is string-type
        
        Args:
            input: Input to be checked
            input_display (string): String used in ValueError message
        
        Raises:
            ValueError: If input is not of string-type
        """

        if type(input) != str:
            raise ValueError("%s must be a string" % (input_display))
    

    @staticmethod 
    def _validate_number(input, input_display):
        """Private method to check if input is a number-type
        
        Args:
            input: Input to be checked
            input_display (string): String used in ValueError message
        
        Raises:
            ValueError: If input is not of int- or float-type
        """

        if type(input) != int or type(input) != float:
            raise ValueError("%s must be an int or float" % (input_display))
