"""
Este file contiene las pruebas unitarias para cada funcion usada en el codigo.
El responsable de las pruebas unitarias es Emilio Ontiveros.
"""
import Etapa1
import Etapa2
import Etapa3
import Etapa4
import Etapa5

import doctest

# Variables necesarias para test 1 y 2
board = {}
board['letters_in_board'] = '[A][B][C][E][D][E][F][G][H][I]'
board['results_in_board'] = '[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]'
board['success'] = 0
board['mistake'] = 0
board['letters_list'] = ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[J]']
turns = 0
words = ["Árbol","Bosque","Camping","Descanso","Entorno","Flor","Gaviota","Higo","Intemperie","Jardin"]
words_dict= {"Árbol":"Descripcion generica 1",
            "Bosque":"Descripcion generica 2",
            "Camping":"Descripcion generica 3",
            "Descanso":"Descripcion generica 4",
            "Entorno":"Descripcion generica 5",
            "Flor":"Descripcion generica 6",
            "Gaviota":"Descripcion generica 7",
            "Higo":"Descripcion generica 8",
            "Intemperie":"Descripcion generica 9",
            "Jardin":"Descripcion generica 10",}
board['turns_description_list'] = ["Descripcion"]
# Solo para test 2
actual_letter = "Á"
correct_word = "Árbol"
board['resultboard'] = ["b"]

# TEST1 -----------------------------------------------------------------------------------------------------------------------
def show_letterboard_test_1():
    """
    Verifica que al enviar una lista de 10 letras, cree y muestre el tablero

    de generar el tablero que muesta las letras. Ej: [A] [B] [C] ...
    >>> Etapa1.show_letterboard(["a","b","c","d","e","f","g","h","i","j"])
    ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[J]']

    >>> Etapa1.show_letterboard(["a","b","c","d","e","f","g","h","i","F"])
    ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[F]']

    >>> Etapa1.show_letterboard(["a","b","c","d","e","f","g","h","i","Ñ"])
    ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[Ñ]']
    """

# TEST2 -----------------------------------------------------------------------------------------------------------------------
def print_board_test_2():
    # Ejecucion del caso de prueba
    """
    >>> Etapa1.print_board(board, turns, words, words_dict)
    [A][B][C][E][D][E][F][G][H][I]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    <BLANKLINE>
    Aciertos: 1
    Errores: 1
    Turno letra A - Palabra de 5 letras
    Definicion: Descripcion generica 1
    """
 
    
# TEST3 -----------------------------------------------------------------------------------------------------------------------
def validate_lenght_and_grammar():
    """
    >>> Etapa1.validate_lenght_and_grammar("Palabra", 7)
    'Palabra'
    >>> Etapa1.validate_lenght_and_grammar("Palabras", 8)
    'Palabras'
    >>> Etapa1.validate_lenght_and_grammar("Palabrerio", 10)
    'Palabrerio'
    """
    
# TEST4 -----------------------------------------------------------------------------------------------------------------------
def add_answer():
    """
    >>> Etapa1.add_answer(board, "Árbol", actual_letter, correct_word, turns)
    Palabra correcta!
    <BLANKLINE>
    (1, 0)

    >>> Etapa1.add_answer(board, "Arboles", actual_letter, correct_word, turns)
    Palabra incorrecta - La respuesta correcta era: Árbol
    <BLANKLINE>
    (1, 1)
    """

# TEST5 -----------------------------------------------------------------------------------------------------------------------
def return_quantity_test_5():
    list = ["alegria","prisma","generico","otro"]
    list2 = ["alegria","prisma","generico","otro","adicionar"]
    """    
    >>> Etapa2.return_quantity(list)
    {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 1, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'ñ': 0, 'o': 1, 'p': 1, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}, 4
    
    >>> Etapa2.return_quantity(list2)
    {'a': 2, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 1, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'ñ': 0, 'o': 1, 'p': 1, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}, 5
    """
    
print (doctest.testmod())



# #---------------------------------------------------------
# Etapa1.show_letterboard(random_letters)                                                                               --> Verificado  TEST1
# Etapa1.print_board(letters_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict)      --> Verificado  TEST2
# Etapa1.ask_for_word()                                                                                                 
# Etapa1.validate_lenght_and_grammar(string, lenght)                                                                    --> Verificado
# Etapa1.add_answer(word, actual_letter, correct_word, resultboard, turns_description_list, turns, success, mistake)    --> Verificado
# Etapa1.run_match(words_dict, words, random_letters)
# Etapa1.main_etapa1()
# Etapa1.run_match(words_dict, words, random_letters)
# #---------------------------------------------------------
# Etapa2.return_short_words(main_list)
# Etapa2.return_quantity(short_word_dicc)                                                                               --> Verificado
# Etapa2.main_etapa2()
# #---------------------------------------------------------
# Etapa3.return_random_letters(letras)
# Etapa3.generate_rosco(diccionario,letras)
# Etapa3.obtain_words_with_accents(letra,palabras)
# Etapa3.main_etapa3()
# #---------------------------------------------------------
# Etapa4.play_the_game()
# Etapa4.generate_diccionary()
# #---------------------------------------------------------
# Etapa5.acumulate_points(results,SUCCESS_POINTS = 10, FAIL_POINTS = -3)
# Etapa5.play_match()
