"""Etapa 4: Integracion"""
# El responsable de esta etapa es Emilio Ontiveros.
# El responsable de su revision es Santiago Testa.

# -----------------------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------------------
import Etapa1
import Etapa2
import Etapa3

# -----------------------------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------------------------
def main_etapa4():
    play_the_game()

# -----------------------------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------------------------
def play_the_game():
    """Ejecuta una partida de juego y devuelve los resultados de la misma"""
    
    # Generación del diccionario de palabras. (Etapa2)
    word_dictionary = generate_diccionary()
    
    # Seleccion de 10 letras aleatorias (Etapa3)
    random_letters = Etapa3.return_random_letters(Etapa2.ALPHABET)

    # Seleccion de lista de palabras a adivinar (Etapa3).
    words_list = Etapa3.generate_rosco(word_dictionary,random_letters)
    
    # Creacion del tablero (Etapa1)
    results = Etapa1.run_match(word_dictionary, words_list, random_letters)
    
    return results

def generate_diccionary():
    """Genera y devuelve el diccionario a ser usado durante el juego"""
    # Obtiene una lista aleatoria de definiciones
    main_list = Etapa2.obtener_lista_definiciones()
    
    # Filtra las listas para que regrese aquellas cuyo largo es valido (Mayor a 5)
    short_word_dicc = Etapa2.return_short_words(main_list)
    return short_word_dicc

main_etapa4()