"""Etapa 3: Rosco"""
# El responsable de esta etapa es Santiago Testa.
# El responsable de su revision es Tomas Galluccio.

from datos import obtener_lista_definiciones
import random

import Etapa2
import Etapa10
import Etapa8 

DEBUG_MODE = False
DEBUG_TP = 3

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
    
    added_letters = []
    for i in range(AMOUNT_OF_LETTERS):
        found_letter = False
        letter = ''
        words_that_start_with_letter = []

        # Encontrar letra valida
        while not found_letter:
            words_that_start_with_letter.clear()
            letter = letters[random.randint(MIN_RANDOM, MAX_RANDOM_LETTER)]

            # Si la letra no fue agregada antes y tiene palabras, agregala al resultado
            if not letter in added_letters:
                words_that_start_with_letter = return_words_that_start_with_letter(letter,dictionary.keys(),LENGTH)
                found_letter = ( len(words_that_start_with_letter) != 0 )

        # Agregar (letra, palabra aleatoria)
        random_index = random.randint(MIN_RANDOM, len(words_that_start_with_letter) - 1)
        result.append(words_that_start_with_letter[random_index])

        # AÑADIR A LETRAS QUE APÄRECIERON
        addedd_letters = return_correct_list_of_letters(added_letters, words_that_start_with_letter[random_index][0])
        '''
        if DEBUG_MODE:
            print(addedd_letters)
        '''
    # print(result)
    return spanish_sort(result)

def return_correct_list_of_letters(letters, letter):
    result = letters

    if letter == 'á' or letter == 'a':
        result.append('a')
        result.append('á')
    elif letter == 'é' or letter == 'e':
        result.append('e')
        result.append('é')
    elif letter == 'í' or letter == 'i':
        result.append('i')
        result.append('í')
    elif letter == 'ó' or letter == 'o':
        result.append('o')
        result.append('ó')
    elif letter == 'ú' or letter == 'u':
        result.append('u')
        result.append('ú')
    else:            
        result.append(letter)

    return result


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
    
    sorted_words = random_words
    sorted_words.sort()

    '''
    if DEBUG_MODE:
        print("Sorted words:",sorted_words)
    '''
    
    # Se iterara hasta que todas las letras especiales encuentren su posicion
    position = len(sorted_words) - 1
    while position > 0 and sorted_words[position][0] in ('ñ','á','é','í','ó','ú'):
        position -= 1

    # Separar palabras normales y especiales
    normal_words = []
    for i in range(position + 1):
        normal_words.append(sorted_words[i])
    special_words = sorted_words[position + 1::]
    special_words.sort(reverse=True)

    '''
    if DEBUG_MODE:
        print("Normal words:",normal_words)
        print("Special words:",special_words)
    '''
    # Ordenamiento
    # Las letras especiales quedan asi: á,é,í,ñ,ó,ú
    # Se insertaran los caracteres en orden, pero se encontrara su posicion desde el final
    result = normal_words
    is_ñ_present = False
    ñ_word = ''
    for word in special_words:
        limite = return_limit_for_spanish_sort(word[0])
        
        # La ñ es un caso completamente patológico (igualmente amamos nuestro idioma)
        if word[0] != 'ñ':
            i = 0
            while  i < len(result) and (result[i][0] < limite) :
                i += 1

            if i < len(result):
                result.insert(i,word)
            else:
                result.append(word)
        else:
            is_ñ_present = True
            ñ_word = word
    
    if is_ñ_present:
        result = correct_ñ_position_tp2(result,ñ_word)

    return result

def correct_ñ_position_tp2(words, ñ_word):
    i = 0
    LENGTH = len(words)
    while i < LENGTH and not is_ñ_in_correct_position(words, i):
        i += 1
    words.insert(i,ñ_word)

    '''
    if DEBUG_MODE:
        print("CHEEEEEEEEEEEEEEEE ",words)
    '''
    return words

def is_ñ_in_correct_position(words,i):
    return words[i][0] > 'n' and not words[i][0] in ('á','é','í')

def return_limit_for_spanish_sort(letter):
    result = ''
    if letter == 'á':
        result = 'a'
    elif letter == 'é':
        result = 'e'
    elif letter == 'í':
        result = 'i'
    elif letter == 'ó':
        result = 'o'
    elif letter == 'ú':
        result = 'u'

    return result

def return_first_letter_of_words(random_words):
    '''
    ASUME QUE LAS PALABRAS VIENEN ORDENADAS POR SPANISH_SORT
    '''

    result = []
    for word in random_words:
        if word[0] == 'á':
            result.append('a')
        elif word[0] == 'é':
            result.append('e')
        elif word[0] == 'í':
            result.append('i')
        elif word[0] == 'ó':
            result.append('o')
        elif word[0] == 'ú':
            result.append('u')
        else:
            result.append(word[0])
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
    if DEBUG_TP == 1:
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

    # TP N°2 
    elif DEBUG_TP == 2:

        if DEBUG_MODE:
            word_dictionary = Etapa8.return_words_and_definition()
            with open("hotfix_test","a") as hotfix:
                hotfix.write("--------------------------------------------------------------------------\n")
                hotfix.write("Nueva prueba\n")
                hotfix.write("--------------------------------------------------------------------------\n")
                AMOUNT_ITERATIONS = 100
                for i in range(0,AMOUNT_ITERATIONS):
                    hotfix.write("Intento numero:" + str(i + 1) + "\n")
                    print("Intento numero:",i + 1)
                    random_words = generate_random_letters_and_words(Etapa2.ALPHABET, word_dictionary)
                    random_letters = return_first_letter_of_words(random_words)
                    
                    output = ''
                    for letter in random_letters:
                        output += ('[' + str(letter) + ']')
                    output += '\n'    
                    hotfix.write(output)

                    for word in random_words:
                        if word[0] in ('á','é','í','ó','ú','ñ'):
                            print([word[0] for word in random_words])
                            print('PALABRA: ' + word + ' LETRA: ' + word[0])

    elif DEBUG_TP == 3:
        #spanish_sort(['útero','ímpetu', 'vaca','árbol','éxtasis','óraculo','ñandú','balde'])
        caso_3 = ['útero','ímpetu','ñandú','vaca','árbol','éxtasis','óraculo','balde']
        print("TEST 3\nSe ordenara: {}\n Ordenado:".format(caso_3))
        print(spanish_sort(caso_3))
    else:
        with open("test_palabras.txt",'a+') as end_file:
            end_file.write("\n\n\n\n\n\nNEWRUN\n\n\n\n\n\n")
            words_for_file = spanish_sort([word for word in Etapa8.return_words_and_definition().keys() if not word[0] in ('a','e','i','o','u')])
            for word in words_for_file:
                output = word + '\n'
                end_file.write(output)

#main_etapa3()