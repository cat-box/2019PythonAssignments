class AbstractPlayer:
    """AbstractPlayer class
    """


    def __init__(self, id, fname, lname, height, weight, jersey_num, date_birth, year_joined):
        """Constructor method for AbstractPlayer
        
        Args:
            id (int): id
            fname (string): Full name
            lname (string): Last name
            height (float): Height
            weight (float): Weight
            jersey_num (int): Jersey number
            date_birth (string): Date of birth
            year_joined (string): Year joined
        """
        self._validate_input(id, "id")
        self._id = id

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


    def get_id(self):
        """Gets id of player
        
        Returns:
            id (int): Player's id
        """
        return self._id


    def set_id(self, id):
        """Sets id of player
        
        Args:
            id (int): Player id
        """
        self._id = id


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
            NotImplementedError: 
        """
        raise NotImplementedError("Abstract method - must be implemented in subclass")


    def get_type(self):
        """Abstract method to be implemented by subclasses
        
        Raises:
            NotImplementedError: 
        """
        raise NotImplementedError("Abstract method - must be implemented in subclass")


    @staticmethod
    def _validate_input(input, input_display):
        """Private helper to validate inputs
        
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