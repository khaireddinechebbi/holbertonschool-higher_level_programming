"""
This module demonstrates multiple inheritance and method \
resolution order (MRO) in Python.
It defines three classes: Fish, Bird, and FlyingFish. \
The FlyingFish class inherits from both
Fish and Bird classes, and overrides methods to provide \
specific behavior for flying fish.
"""


class Fish:
    """
    Fish class representing a fish.

    Methods:
        swim: Prints that the fish is swimming.
        habitat: Prints that the fish lives in water.
    """

    def swim(self):
        """Prints that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints that the fish lives in water."""
        print("The fish lives in water")


class Bird:
    """
    Bird class representing a bird.

    Methods:
        fly: Prints that the bird is flying.
        habitat: Prints that the bird lives in the sky.
    """

    def fly(self):
        """Prints that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints that the bird lives in the sky."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird classes.

    Methods:
        fly: Prints that the flying fish is soaring.
        swim: Prints that the flying fish is swimming.
        habitat: Prints that the flying fish lives both in water and the sky.
    """

    def fly(self):
        """Prints that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints that the flying fish lives both in water and the sky."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
