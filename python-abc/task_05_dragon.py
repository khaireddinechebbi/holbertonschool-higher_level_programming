#!/usr/bin/python3
"""
This module demonstrates the use of mixins in Python for extending \
class functionality.
It defines three classes: SwimMixin, FlyMixin, and Dragon. \
The Dragon class inherits from both
SwimMixin and FlyMixin, and has an additional method for \
its specific behavior.
"""


class SwimMixin:
    """
    Mixin class to provide swimming capability.

    Methods:
        swim: Prints that the creature swims.
    """

    def swim(self):
        """Prints that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class to provide flying capability.

    Methods:
        fly: Prints that the creature flies.
    """

    def fly(self):
        """Prints that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying capabilities from mixins.

    Methods:
        roar: Prints that the dragon roars.
    """

    def roar(self):
        """Prints that the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
