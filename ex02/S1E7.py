from S1E9 import Character


class Baratheon(Character):
    """Class representing a Baratheon character"""

    def __init__(self, first_name, is_alive=True):
        """Initialize Baratheon character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """Return a string representation of the character"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Return the official string representation of a character"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"


class Lannister(Character):
    """Class representing a Lannister character"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set is_alive to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Create a Lannister character in chained style"""
        return cls(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the character"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"

    def __repr__(self):
        """Return the official string representation of a character"""
        return f"Vector: {(self.family_name, self.eyes, self.hairs)}"
