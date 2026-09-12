from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King character"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a King character"""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Return the eyes color"""
        return self.__dict__["eyes"]

    def set_eyes(self, value):
        """Set eyes color of King"""
        self.__dict__["eyes"] = value

    eyes = property(get_eyes, set_eyes)

    def get_hairs(self):
        """Return de hairs color"""
        return self.__dict__["hairs"]

    def set_hairs(self, value):
        """Set the hairs color of King"""
        self.__dict__["hairs"] = value

    hairs = property(get_hairs, set_hairs)
