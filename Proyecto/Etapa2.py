"""Etapa 2: Diccionario"""
# El responsable de esta etapa es es Tomas Galluccio.
# El responsable de su revision es Lucas Aldonate.

from datos import obtener_lista_definiciones
import doctest

ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
ALPHABET_WITH_ACCENT = ["a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","ñ","o","ó","p","q","r","s","t","u","ú","v","w","x","y","z"]

def return_short_words(main_list):
    """
    Recibe la lista principal y devuleve un diccionario con palabras de un largo determinado
    """
    out_dicc={}     # Diccionario de salida
    MIN_LETERS=5    # Largo minimo de letras por palabra
    
    INDEX_WORD=0        # Ubicacion de las palabras en la lista principal
    INDEX_DEFINITION=1  # Ubicacion de las definiciones de palabras en la lista principal   

    for word in main_list:
        if len(word[INDEX_WORD])>=MIN_LETERS:
            out_dicc[word[INDEX_WORD]]=word[INDEX_DEFINITION]
    return out_dicc

def return_quantity(short_word_dicc):
    """
    Devuleve la cantidad de palabras que inician con una letra en especifico y la cantidad total de 
    palabras en el diccioanrio
    """

    out_dicc_just_letter={}     # Diccionario de salida. Solo letras
    words_list=[]               # Lista de palabras

    INDEX_FIRST_LETTER_IN_WORD=0                # Es la primer letra de cada palabra
    for word in short_word_dicc:
        words_list.append(word[INDEX_FIRST_LETTER_IN_WORD])
    
    total_words_in_dicc=0

    for letter in ALPHABET:
        # Asigna la letra como key y le asigna la ocurrencia como value
        out_dicc_just_letter[letter] = words_list.count(letter) 

        # TODO: Agregar vocales acentuadas.

        if letter=="a":
            out_dicc_just_letter["a"]+=words_list.count("á")

        elif letter=="i":
            out_dicc_just_letter["i"]+=words_list.count("í")            
        
        elif letter=="o":
            out_dicc_just_letter["o"]+=words_list.count("ó")    

        elif letter=="u":
            out_dicc_just_letter["u"]+=words_list.count("ú")

        # Acumula el total de palabras

        total_words_in_dicc += out_dicc_just_letter[letter] 
        
    return out_dicc_just_letter, total_words_in_dicc

def main_etapa2():
    """
    Recibe una lista que contiene las palabras candidatas
    y sus definiciones, las analiza y retorna un out_dicc con palabras especificas. Para, posteriormente
    haberiguar cuantas palabras inician.
    """
    main_list= obtener_lista_definiciones()
    short_word_dicc= return_short_words(main_list)
    quantity, total= return_quantity(short_word_dicc) #return_quantity devuelve cantidad y total
    print("Los numeros de palabras por letra son: ", quantity, "y el total es: ", total)
    
main_etapa2()

#TODO:
# Este es el codigo que imprime
# "Los numeros de palabras por letra son:  {'a': 47, 'b': 26, 'c': 45, 'd': 43, 'e': 91, 'f': 77, 'g': 62, 'h': 74, 'i': 78, 'j': 49, 'k': 24, 'l': 69, 'm': 66, 'n': 64, 'ñ': 1, 'o': 57, 'p': 70, 'q': 23, 'r': 73, 's': 80, 't': 68, 'u': 60, 'v': 72, 'w': 5, 'x': 7, 'y': 41, 'z': 14} y el total es:  1386"
# El total deberia tener 8 palabras mas (1394)



