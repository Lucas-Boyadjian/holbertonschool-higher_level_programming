#!/usr/bin/env python3

class SwimMixin:
    """
    A mixin class that provides swimming functionality.

    This mixin can be used with any class that needs to be able to swim.
    """
    def swim(self):
        """
        Simulate the swimming action.

        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.

    This mixin can be used with any class that needs to be able to fly.
    """
    def fly(self):
        """
        Simulate the flying action.

        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon.

    This class inherits from both SwimMixin and FlyMixin,
    demonstrating the use of multiple mixins to compose functionality.
    Dragons can both swim and fly, and they can also roar.
    """

    def roar(self):
        """
        Simulate the roaring action of a dragon.

        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")


draco = Dragon()
