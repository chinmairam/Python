"""
    player.py
    ---------

    This module contains the Player class that represents game characters.
"""

__author__ = "Reindert-Jan Ekker"


class Player:
    """
    The Player class represents the characters in the game.

    :ivar health: The current health of the character. Starts at 100.
                  Once it reaches 0, we're dead.
    """

    def __init__(self, name, weapon):
        """
        Create a new Player.

        :param name: The name of the Player.
        :param weapon: The weapon that this Player uses to fight with
        """
        self.name = name
        self.weapon = weapon
        self.health = 100

    def take_hit(self, damage):
        """
        This method gets called when the player takes a hit from the opponent's weapon
        :param damage: The damage dealt. This will be substracted from :attr:`health`.
        :return: The new value of :attr:`health`.
        """
        self.health -= damage
        return self.health

    @property
    def is_alive(self):
        """True if :attr:`health` is larger than 0, False otherwise"""
        return self.health > 0

    def __str__(self):
        return "Player {} has {} health and brings his {} to the fight".format(self.name, self.health,
                                                                               type(self.weapon).__name__)
