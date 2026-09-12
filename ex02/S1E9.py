from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a abstract character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method implemented in subclasses."""


class Stark(Character):
    """Class representing a Stark character"""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Set is_alive of character to False"""
        self.is_alive = False
