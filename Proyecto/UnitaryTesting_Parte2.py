"""
Este file contiene las pruebas unitarias.
El responsable de las pruebas unitarias es Emilio Ontiveros.
"""

import Etapa7B_Backend
import doctest

def test_create_valid_password():
    """
    >>> Etapa7B_Backend.create_valid_password("Ejemplo123!")
    True

    >>> Etapa7B_Backend.create_valid_password("Ejemplo123")
    False

    >>> Etapa7B_Backend.create_valid_password("Ejemplo!")
    False

    >>> Etapa7B_Backend.create_valid_password("Ejemplo!#$")
    False
    """

def test_create_valid_user():
    """
    >>> Etapa7B_Backend.create_valid_user("Ejemplo123")
    True

    >>> Etapa7B_Backend.create_valid_user("Ej")
    False

    >>> Etapa7B_Backend.create_valid_user("°°12#!$!")
    False
    """


print (doctest.testmod())


