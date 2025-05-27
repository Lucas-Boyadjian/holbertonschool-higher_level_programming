#!/usr/bin/env python3

class Fish:
    """
    A class representing a fish.

    This class defines the basic behaviors of a fish,
    such as swimming and its habitat.
    """

    def swim(self):
        """
        Simulate the swimming action of a fish.

        Prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Describe the habitat of a fish.

        Prints a message indicating that fish live in water.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.

    This class defines the basic behaviors of a bird,
    such as flying and its habitat.
    """

    def fly(self):
        """
        Simulate the flying action of a bird.

        Prints a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Describe the habitat of a bird.

        Prints a message indicating that birds live in the sky.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish.

    This class inherits from both Fish and Bird,
    demonstrating multiple inheritance.
    It overrides methods from both parent classes to provide
    specialized behavior.
    """

    def fly(self):
        """
        Simulate the flying action of a flying fish.

        Overrides the fly method from Bird to provide flying
        fish specific behavior.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Simulate the swimming action of a flying fish.

        Overrides the swim method from Fish to provide flying
        fish specific behavior.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Describe the habitat of a flying fish.

        Overrides the habitat method from both parent
        classes to describe the unique
        dual habitat of flying fish.
        """
        print("The flying fish lives both in water and the sky!")

    def __mro__(self):
        """
        Print the Method Resolution Order for the FlyingFish class.

        This helps visualize the inheritance hierarchy and the order in which
        Python searches for methods in the parent classes.
        """
        print(FlyingFish.__mro__)
