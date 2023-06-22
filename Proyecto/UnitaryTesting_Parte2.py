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

# PARA PRUEBAS DE Etapa10.set_game_config

config_file_1 = Etapa10.check_config_file('configuracion.csv')
config_file_2 = Etapa10.check_config_file('configuracio.csv')

def test_set_game_config():
    """
    >>> Etapa10.set_game_config(config_file_1)
    {'MIN_WORD_LENGHT': [5, 'configuracion'], 'LETTERS_ROSCO_QUANTITY': [12, 'configuracion'], 'MAX_GAMES': [3, 'configuracion'], 'SUCCESS_POINT': [10, 'configuracion'], 'FAIL_POINT': [3, 'configuracion']}

    >>> Etapa10.set_game_config(config_file_2)
    {'MIN_WORD_LENGHT': [4, 'omision'], 'LETTERS_ROSCO_QUANTITY': [10, 'omision'], 'MAX_GAMES': [5, 'omision'], 'SUCCESS_POINT': [10, 'omision'], 'FAIL_POINT': [3, 'omision']}
    """

def test_check_config_file():
    """
    >>> Etapa10.check_config_file('configuracion.csv')
    <_io.TextIOWrapper name='configuracion.csv' mode='r' encoding='cp1252'>

    >>> Etapa10.check_config_file('configuracio.csv') # Como el output es None (el archivo esta mal escrito, no existe) en este caso, no se espera nada

    """



print (doctest.testmod())


