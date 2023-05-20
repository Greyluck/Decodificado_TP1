"""Etapa 3: Rosco"""
# Esta es la etapa3 creada por Emilio Ontivertos debido a los errores sobre etapa3 de Santiago
# El responsable de su revision es Santiago Testa

from datos import obtener_lista_definiciones
import Etapa2
import random

debug_mode = True

def return_random_letters(letters):
    '''
    Esta funcion recibe la lista de letras y devuelve una lista ordenada alfabeticamente con
    10 de ellas elegidas al azar.
    '''
    resultant_list_of_letters = []                              # Lista que sera devuelta
    REQUIRED_AMOUNT_OF_LETTERS = 10                             # Cantidad de letras que tendra la lista

    while len(resultant_list_of_letters) < REQUIRED_AMOUNT_OF_LETTERS:
        letters_quantity = len(letters)                                     # Indica la cantidad de letras totales que se revisaran
        my_random_number_for_letter = random.randint(0,letters_quantity-1)  # Numero aleatorio entre 0 y la cantidad de letras-1
        chosen_letter = letters[my_random_number_for_letter]               # Elije la letra aleatoria

        while chosen_letter not in resultant_list_of_letters:   # Solo agrega letras nuevas.
            resultant_list_of_letters.append(chosen_letter)
            
    resultant_list_of_letters.sort()
    
    # TODO: Agregar ordenamiento de ñ
    if debug_mode: print(resultant_list_of_letters)
    return resultant_list_of_letters


def generate_rosco(dictionary,participant_letters):
    '''
    Recibe un diccionario y una lista de letras, devuelve una lista ordenada con las palabras elegidas.
    '''
    result = []

    # Crea una lista ordenada usando el diccionario
    list_of_possible_words = []
    for word in dictionary:
        # Verifica que la primer letra de cada palabra sea una de las elegidas
        STARTING_LETTER = 0
        if word[STARTING_LETTER] in participant_letters:
            list_of_possible_words.append(word)      
    list_of_possible_words.sort()

    return list_of_possible_words

def main_etapa3():
    # Este es el diccionario que recibo de la etapa anterior.
    dictionary = Etapa2.return_short_words(obtener_lista_definiciones())
        
    # Esta es la lista de las letras que salieron elegidas para jugar
    selected_letters = return_random_letters(Etapa2.ALPHABET)

    generate_rosco(dictionary,selected_letters)
    

#main_etapa3()
