"""Etapa 3: Rosco"""
# El responsable de esta etapa es Santiago Testa.
# El responsable de su revision es Tomas Galluccio.

from datos import obtener_lista_definiciones
from Etapa2 import return_short_words
import random

import Etapa2

def return_random_letters(letters):
    '''
    Esta funcion recibe la lista de letras y te devuelve otra lista de 10 letras elegidas pseudo-aleatoriamente (ignorar el pseudo en la 
    expresion anterior) 
    La lista esta ordenada alfabeticamente
    '''
    
    result = []
    AMOUNT_OF_LETTERS = 10

    for i in range (AMOUNT_OF_LETTERS):
        found_letter = False
        letter = ''
        while not found_letter:
            letter = letters[random.randint(0,len(letters) - 1)]
            if not letter in result:
                found_letter = True

        result.append(letter)
    
    result.sort()

    
    # Ultimo edit, para que la letra ñ no quede al final
    aux = []
    position_found = False
    if 'ñ' in result:
        # Iteramos hasta en anteúltimo elemento, debido a que el método sort ubica a la ñ en la última posición
        for i in range (len(result) - 1):
            if result[i] > 'n' and not position_found:
                aux.append('ñ')
                position_found = True
            aux.append(result[i])

        result = aux
                
    return result

def generate_rosco(dictionary,letters):
    '''
    ESTA FUNCION RECIBE DICCIONARIO DE PALABRA: DEFINICION y la lista del total de letras del rosco.
    Devuelve una lista ordenada alfabeticamente con las palabras elegidas
    '''
    result = []

    # OBTENER PALABRAS DEL DICCIONARIO y ORDENARLAS ALFABETICAMENTE (se asume que no estan ordenadas)
    words_for_use = [ key for key in dictionary if key[0] in letters or key[0] in ('á','é','í','ó','ú')]
    words_for_use.sort()

    for letter in letters:
        # SI LA LETRA ES VOCAL, AGREGAR PALABRAS QUE INICIAN EN ACENTO
        words_that_start_with_letter = []
        if letter in ('a','e','i','o','u'):
            words_that_start_with_letter = obtain_words_with_accents(letter,words_for_use)
        
        # ENCONTRAR PRIMER APARICION DE LETRA Y AGREGAR A LISTA TODAS LAS PALABRAS QUE INICIEN CON ESA LETRA
        i = 0
        while not words_for_use[i][0] is letter:
            i += 1

        while words_for_use[i][0] is letter:
            words_that_start_with_letter.append(words_for_use[i])
            i += 1

        # ----------------------------------------------------------------------------------------------------
        # TODO: En esta seccion hay un error que aparece solo en una de las pcs donde se ejecuta (PC de Emilio)
        # Se debe revisar este error para entender como manejarlo.
        # print("ACA!")
        # print(palabras_letra)
        # print(0,len(palabras_letra) - 1)
        # print(random.randint(0,len(palabras_letra) - 1))
        # print(palabras_letra[random.randint(0,len(palabras_letra) - 1)])
        # print(resultado.append(palabras_letra[random.randint(0,len(palabras_letra) - 1)]))
        # ----------------------------------------------------------------------------------------------------

        # TIRAR DADO PARA ELEGIR PALABRA PARA LA LETRA
        result.append(words_that_start_with_letter[random.randint(0,len(words_that_start_with_letter) - 1)])
    return result

def obtain_words_with_accents(letter,words):
    '''
    Si la letra es una vocal, esta funcion devuelve todas las palabras que inician con dicha vocal acentuada
    '''
    # INICIAMOS LA BUSQUEDA DESDE EL FINAL DEBIDO A QUE sort() DEJA PALABRAS CON INICIO ACENTUADO AL FINAL DE LA LISTA
    result = []

    i = len(words) - 1
    while words[i][0] in ('á','é','í','ó','ú'):
        if letter == 'a' and words[i][0] == 'á':
            result.append(words[i])
        elif letter == 'e' and words[i][0] == 'é':
            result.append(words[i])
        elif letter == 'i' and words[i][0] == 'í':
            result.append(words[i])
        elif letter == 'o' and words[i][0] == 'ó':
            result.append(words[i])
        elif letter == 'u' and words[i][0] == 'ú':
            result.append(words[i])

        i -= 1

    return result

def main_etapa3():
    dictionary = return_short_words(obtener_lista_definiciones())
    
    # TEST DE CONSIGA
    AMOUNT_ITERATIONS = 100
    for i in range(0,AMOUNT_ITERATIONS):
        print("Intento numero:",i + 1)
        letters = return_random_letters(Etapa2.ALPHABET)
        rosco = generate_rosco(dictionary, letters)
        for ii in range(len(rosco)):
            print("LETRA:",letters[ii],"| PALABRA:",rosco[ii])

main_etapa3()
