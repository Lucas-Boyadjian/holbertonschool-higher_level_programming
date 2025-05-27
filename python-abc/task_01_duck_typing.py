#!/usr/bin/env python3
"""
Module illustrant l'utilisation des classes abstraites
et le duck typing en Python.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite définissant l'interface pour les formes géométriques.

    Cette classe ne peut pas être instanciée directement et force
    ses sous-classes à implémenter des méthodes spécifiques.
    """

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire de la forme.

        Returns:
            float: L'aire de la forme
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre de la forme.

        Returns:
            float: Le périmètre de la forme
        """
        pass


class Circle(Shape):
    """Classe représentant un cercle."""

    def __init__(self, radius):
        """Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle
        """
        self.radius = radius

    def area(self):
        """Calcule l'aire du cercle.

        Returns:
            float: L'aire du cercle (π * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcule le périmètre (circonférence) du cercle.

        Returns:
            float: Le périmètre du cercle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Classe représentant un rectangle."""

    def __init__(self, width, height):
        """Initialise un rectangle avec une largeur et une hauteur données.

        Args:
            width (float): La largeur du rectangle
            height (float): La hauteur du rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """Calcule l'aire du rectangle.

        Returns:
            float: L'aire du rectangle (largeur * hauteur)
        """
        return self.width * self.height

    def perimeter(self):
        """Calcule le périmètre du rectangle.

        Returns:
            float: Le périmètre du rectangle (2 * (largeur + hauteur))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Affiche l'aire et le périmètre d'une forme géométrique.

    Cette fonction utilise le principe du duck typing: elle fonctionne avec
    tout objet qui possède les méthodes area() et perimeter(), sans vérifier
    son type explicitement.

    Args:
        shape (Shape): Un objet qui implémente les méthodes
        area() et perimeter()
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
