#!/usr/bin/env python3
"""Module pour démontrer l'utilisation des classes abstraites en Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite qui définit l'interface pour tous les animaux.

    Cette classe ne peut pas être instanciée directement, elle sert de
    modèle pour les classes dérivées.
    """

    @abstractmethod
    def sound(self):
        """Méthode abstraite que chaque animal doit implémenter.

        Returns:
            str: Le son produit par l'animal
        """
        pass


class Dog(Animal):
    """Classe représentant un chien."""

    def sound(self):
        """Implémentation de la méthode sound pour un chien.

        Returns:
            str: Le son produit par un chien ("Bark")
        """
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat."""

    def sound(self):
        """Implémentation de la méthode sound pour un chat.

        Returns:
            str: Le son produit par un chat ("Meow")
        """
        return "Meow"
