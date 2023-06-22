"""Etapa 3: Rosco"""
# El responsable de esta etapa es Santiago Testa.
# El responsable de su revision es Tomas Galluccio.

from datos import obtener_lista_definiciones
import random

import Etapa2
import Etapa10

DEBUG_MODE = True

def generate_random_letters_and_words(letters, dictionary):
    '''
    Argumentos: Todas las letras y el diccionario de palabras
    Funcionalidad: Misma que anteriores de esta etapa, solo que ademas compara si la letra tiene palabras que superen el largo minimo.
    Y como para hacer esto debe iterar las palabras        
    Return: letras elegidas aleatoriamente, palabras que inician con esa letra
    Nota: Función refactorizada para parte 2 del trabajo practico debido a que, al existir una longitud minima para las palabras, era posible
    que no haya palabras para alguna letra (lo cual rompia el programa)
    '''

    result = [] 
    words_that_start_with_letter = []

    AMOUNT_OF_LETTERS = Etapa10.game_config['LETTERS_ROSCO_QUANTITY'][Etapa10.VALUE]
    LENGTH = Etapa10.game_config['MIN_WORD_LENGHT'][Etapa10.VALUE]
    MIN_RANDOM = 0
    MAX_RANDOM_LETTER = len(letters) - 1
    
    for i in range(AMOUNT_OF_LETTERS):
        found_letter = False
        letter = ''
        words_that_start_with_letter = []

        # Encontrar letra valida
        while not found_letter:
            letter = letters[random.randint(MIN_RANDOM, MAX_RANDOM_LETTER)]

            # Si la letra no fue agregada antes y tiene palabras, agregala al resultado
            if not letter in [ word[0] for word in result ]:
                words_that_start_with_letter = return_words_that_start_with_letter(letter,dictionary.keys(),LENGTH)
                found_letter = ( len(words_that_start_with_letter) != 0 )

        # Agregar (letra, palabra aleatoria)
        random_index = random.randint(MIN_RANDOM, len(words_that_start_with_letter) - 1)
        result.append(words_that_start_with_letter[random_index])

    # print(result)
    return spanish_sort(result)

def return_words_that_start_with_letter(letter, words, length):
    return [ word for word in words if is_this_word_correct(letter,word,length)]

def is_this_word_correct(letter,word, length):
    '''
    Argumentos: Letra y palabra
    Return: True si la palabra empieza con la letra y cumple con el largo, false en caso contrario
    '''
    result = False
    if len(word) >= length:
        if letter == word[0]:
            result = True
        elif letter == 'a' and word[0] == 'á':
            result = True
        elif letter == 'e' and word[0] == 'é':
            result = True
        elif letter == 'i' and word[0] == 'í':
            result = True
        elif letter == 'o' and word[0] == 'ó':
            result = True
        elif letter == 'u' and word[0] == 'ú':
            result = True

    return result

def spanish_sort(random_words):
    '''
    Argumentos: Lista de palabras
    Funcionalidad: Inicia por el final, si la ñ no esta devuelve todo igual, si esta compara con el elemento
    a su izquierda y de ser menor, se intercambian entre si
    Return: Misma lista pero con la posicion de la ñ corregida
    Nota: Funcion refactorizada en TP N°2 - Etapa6
    '''
    result = random_words
    result.sort()
    #print(result)
    LENGTH = len(result)
    
    # MIENTRAS HAYA LETRAS DESORDENADAS POR SER CARACTERE
    index = LENGTH - 1
    while index > 0 and result[index][0] in ('ñ','á','é','í','ó','ú'):
        if result[index][0] == 'ñ':
            # Encontrar posicion de ñ
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'n':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        elif result[index][0] == 'á':
            # Encontrar posicion de ñ
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'a':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        elif result[index][0] == 'é':
            # Encontrar posicion de ►
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'e':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        elif result[index][0] == 'í':
            # Encontrar posicion de í
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'i':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        elif result[index][0] == 'ó':
            # Encontrar posicion de ó
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'o':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        elif result[index][0] == 'ú':
            # Encontrar posicion de ú
            position = LENGTH - 2
            while position > 0 and result[position][0] > 'u':
                position -= 1

            # Corregir posicion
            result.insert(position, result.pop(index))
        
    return result


def return_random_letters(letters):
    '''
    TP N°1
    Esta funcion recibe la lista de letras y te devuelve otra lista de 10 letras elegidas pseudo-aleatoriamente (ignorar el pseudo en la 
    expresion anterior) 
    La lista esta ordenada alfabeticamente
    '''
    
    result = []
    AMOUNT_OF_LETTERS = Etapa10.game_config['LETTERS_ROSCO_QUANTITY'][Etapa10.VALUE]

    for i in range(AMOUNT_OF_LETTERS):
        found_letter = False
        letter = ''
        while not found_letter:
            letter = letters[random.randint(0,len(letters) - 1)]
            if not letter in result:
                found_letter = True

        result.append(letter)
    
    result.sort()

    # Ultimo edit, para que la letra ñ no quede al final
    if 'ñ' in result:
        result = correct_ñ_position(result)    
                
    return result

def generate_rosco(dictionary,letters):
    '''
    TP N°1
    ESTA FUNCION RECIBE DICCIONARIO DE PALABRA: DEFINICION y la lista del total de letras del rosco.
    Devuelve una lista ordenada alfabeticamente con las palabras elegidas
    '''
    result = []

    # OBTENER PALABRAS DEL DICCIONARIO y ORDENARLAS ALFABETICAMENTE (se asume que no estan ordenadas)
    words_for_use = []
    for key in dictionary.keys():
            if key[0] in letters or key[0] in ('á','é','í','ó','ú'):
                words_for_use.append(key)
    words_for_use.sort()
    for letter in letters:
        # SI LA LETRA ES VOCAL, AGREGAR PALABRAS QUE INICIAN EN ACENTO
        words_that_start_with_letter = []
        if letter in ('a','e','i','o','u'):
            words_that_start_with_letter = obtain_words_with_accents(letter,words_for_use)
        
        # ENCONTRAR PRIMER APARICION DE LETRA Y AGREGAR A LISTA TODAS LAS PALABRAS QUE INICIEN CON ESA LETRA
        i = 0
        while (i < len(words_for_use)) and (words_for_use[i][0] != letter):
            i += 1

        while (i < len(words_for_use)) and (words_for_use[i][0] == letter):
            words_that_start_with_letter.append(words_for_use[i])
            i += 1

        # DEBUG HEISENBUG print("LETRA: {} PALABRAS: {}".format(letter, words_that_start_with_letter))
        random_index = random.randint(0,len(words_that_start_with_letter) - 1)
        result.append(words_that_start_with_letter[random_index])

    return result

def obtain_words_with_accents(letter,words):
    '''
    TP N°1
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

def correct_ñ_position(letters):
    '''
    TP N°1
    Explicación:
    Recibe una lista de letras ordenada por sort() y devuelve la misma lista pero con la ñ en la posición correcta para nuestro idioma.
    Procedimiento:
    Copia los elementos en una nueva lista hasta llegar a n o mayor, incluye la ñ y copia los elementos restantes sin incluir nuevamente la ñ.
    '''
    
    result = []
    position_found = False
    if 'ñ' in letters:
        # Iteramos hasta en anteúltimo elemento (la ñ es el último)
        for i in range (len(letters) - 1):
            if letters[i] > 'n' and not position_found:
                result.append('ñ')
                position_found = True
            result.append(letters[i])

    return result


def main_etapa3():
    # TP N°1
    dictionary = Etapa2.return_short_words(obtener_lista_definiciones())
    
    # TEST DE CONSIGA
    if DEBUG_MODE:
        AMOUNT_ITERATIONS = 100
        for i in range(0,AMOUNT_ITERATIONS):
            print("Intento numero:",i + 1)
            letters = return_random_letters(Etapa2.ALPHABET)
            rosco = generate_rosco(dictionary, letters)
            for ii in range(len(rosco)):
                print("LETRA:",letters[ii],"| PALABRA:",rosco[ii])

#main_etapa3()