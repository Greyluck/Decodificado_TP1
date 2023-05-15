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

#-----------------------------------------------------------------------------------------------------------------------
def show_letterboard():
    """
    >>> Etapa1.show_letterboard(["a","b","c","d","e","f","g","h","i","j"])
    ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[J]']
    """

#-----------------------------------------------------------------------------------------------------------------------
letters_in_board = '[A][B][C][E][D][E][F][G][H][I]'
results_in_board = '[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]'
success = 0
mistake = 0
letters_list = ['[A]', '[B]', '[C]', '[D]', '[E]', '[F]', '[G]', '[H]', '[I]', '[J]']
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

def print_board():
    # Se agrego blank line para que coincida con la forma mostrada en el PDF. 
    # Doctest revisa las lineas vacias usando ese formato
    """
    >>> Etapa1.print_board(letters_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict)
    [A][B][C][E][D][E][F][G][H][I]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    <BLANKLINE>
    Aciertos: 0
    Errores: 0
    Turno letra A - Palabra de 5 letras
    Definicion: Descripcion generica 1
    """

#-----------------------------------------------------------------------------------------------------------------------

def validate_lenght_and_grammar():
    """
    >>> Etapa1.validate_lenght_and_grammar("Palabra", 7)
    'Palabra'
    """


#-----------------------------------------------------------------------------------------------------------------------
actual_letter = "Á"
correct_word = "Árbol"
resultboard = ["b"]
turns_description_list = ["Descripcion"]
def add_answer():
    """
    >>> Etapa1.add_answer("Árbol", actual_letter, correct_word, resultboard, turns_description_list, turns, success, mistake)
    Palabra correcta!
    <BLANKLINE>
    (1, 0)

    >>> Etapa1.add_answer("Arboles", actual_letter, correct_word, resultboard, turns_description_list, turns, success, mistake)
    Palabra incorrecta - La respuesta correcta era: Árbol
    <BLANKLINE>
    (0, 1)
    """

# TODO: Las pruebas unitarias no son completamente "Unitarias", ya que dependen del orden en el que son ejecutadas.
# Para corregir esto se requiere implementar las variables dentro de las funciones. 
# Eso sera agregado mas adelante. 

print (doctest.testmod())


# #---------------------------------------------------------
# Etapa1.show_letterboard(random_letters)                                                                               --> Verificado
# Etapa1.print_board(letters_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict)      --> Verificado
# Etapa1.ask_for_word()                                                                                                 --> Ignorado
# Etapa1.validate_lenght_and_grammar(string, lenght)                                                                    --> Verificado
# Etapa1.add_answer(word, actual_letter, correct_word, resultboard, turns_description_list, turns, success, mistake)    --> Verificado
# Etapa1.run_match(words_dict, words, random_letters)
# Etapa1.main_etapa1()
# Etapa1.run_match(words_dict, words, random_letters)
# #---------------------------------------------------------
# Etapa2.return_short_words(main_list)
# Etapa2.return_quantity(short_word_dicc)
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
