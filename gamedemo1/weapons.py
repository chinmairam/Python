"""
    weapons.py
    ----------

    This module contains classes for Weapons.
"""

__author__ = "Reindert-Jan Ekker"

from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    """This abstract class defines the method :meth:`attack` that should be implemented
    by subclasses.
    """

    @abstractmethod
    def attack(self, other):
        """This method should return a tuple (damage, text): how much damage was dealt
        and what text to output. Text is a format string with placeholders for attacker
        and defender.
        """


class Sword(Weapon):
    """A primitive close-range weapon. It deals either 5 or 10 damage with a 50/50 chance.
    """

    def attack(self):
        return (
            random.choice([10, 15]),
            random.choice(["Bam!", "Whack!", "Pow!"])
        )


class FireBreath(Weapon):
    """FireBreath is a weapon only wielded by dragons or wizards. It can deal a lot of damage,
    but it also has its drawbacks. There is a 30% chance that the attack will not work, and after
    a successful attack you will need to wait a while before you will be able to breath fire again.
    """

    def __init__(self):
        # The number of attacks we will have to wait until we can fire again
        self._cooldown = 0

    def attack(self):
        if self._cooldown <= 0:
            dmg, sound = random.choice(
                [(0, "There's lots of smoke but no fire.")] * 5 +
                [(40, "Boom! Dragon Fire!")] * 5
            )
            if dmg == 40:
                self._cooldown = 2
            return dmg, sound
        else:
            self._cooldown -= 1
            return (0, "There's lots of smoke but no fire.")

# Use mypy gamedemo1/ in terminal
