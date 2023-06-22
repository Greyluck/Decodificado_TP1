"""
Este file contiene las pruebas unitarias.
El responsable de las pruebas unitarias es Emilio Ontiveros.
"""

import Etapa7B_Backend
import Etapa10
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

def test_print_game_config():
    """
    >>> Etapa10.print_game_config(Etapa10.game_config)
    La configuracion de esta partida es:
    MIN_WORD_LENGHT = 5 -> obtenida por configuracion
    LETTERS_ROSCO_QUANTITY = 12 -> obtenida por configuracion
    MAX_GAMES = 3 -> obtenida por configuracion
    SUCCESS_POINT = 10 -> obtenida por configuracion
    FAIL_POINT = 3 -> obtenida por configuracion
    """

def test_check_config_file():
    """
    >>> Etapa10.check_config_file('configuracion.csv')
    <_io.TextIOWrapper name='configuracion.csv' mode='r' encoding='cp1252'>

    >>> Etapa10.check_config_file('configuracio.csv') # Como el output es None (el archivo esta mal escrito, no existe) en este caso, no se espera nada

    """



print (doctest.testmod())


