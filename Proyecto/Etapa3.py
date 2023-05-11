"""Etapa 3: Rosco"""
# El responsable de esta etapa es Santiago Testa.
# El responsable de su revision es Tomas Galluccio.

from datos import obtener_lista_definiciones
from Etapa2 import return_short_words
import random

import Etapa2

def return_random_letters(letras):
    '''
    Esta funcion recibe la lista de letras y te devuelve otra lista de 10 letras elegidas aleatoriamente 
    La lista esta ordenada alfabeticamente
    '''
    
    resultado = []
    LETTER_QUANTITY = 10

    for i in range (LETTER_QUANTITY):
        elemento_encontrado = False
        elemento = ''
        while not elemento_encontrado:
            elemento = letras[random.randint(0,len(letras) - 1)]
            if not elemento in resultado:
                elemento_encontrado = True

        resultado.append(elemento)
    
    resultado.sort()
    return resultado

def generate_rosco(diccionario,letras):
    '''
    ESTA FUNCION RECIBE DICCIONARIO DE PALABRA: DEFINICION y la lista del total de letras del rosco.
    Devuelve una lista ordenada alfabeticamente con las palabras elegidas
    '''
    resultado = []

    # OBTENER PALABRAS DEL DICCIONARIO y ORDENARLAS ALFABETICAMENTE (se asume que no estan ordenadas)
    palabras_utilizables = [ key for key in diccionario if key[0] in letras or key[0] in ('á','é','í','ó','ú')]
    palabras_utilizables.sort()
    for letra in letras:
        # SI LA LETRA ES VOCAL, AGREGAR PALABRAS QUE INICIAN EN ACENTO
        palabras_letra = []
        if letra in ('a','e','i','o','u'):
            palabras_letra = ObtenerPalabrasAcentuadas(letra,palabras_utilizables)
        
        # ENCONTRAR PRIMER APARICION DE LETRA Y AGREGAR A LISTA TODAS LAS PALABRAS QUE INICIEN CON ESA LETRA
        i = 0
        while palabras_utilizables[i][0] is not letra:
            i += 1

        while palabras_utilizables[i][0] is letra:
            palabras_letra.append(palabras_utilizables[i])
            i += 1
        
        # TIRAR DADO PARA ELEGIR PALABRA PARA LA LETRA
        resultado.append(palabras_letra[random.randint(0,len(palabras_letra) - 1)])
    return resultado

def ObtenerPalabrasAcentuadas(letra,palabras):
    '''
    Si la letra es una vocal, esta funcion devuelve todas las palabras que inician con dicha vocal acentuada
    '''
    # INICIAMOS LA BUSQUEDA DESDE EL FINAL DEBIDO A QUE sort() DEJA PALABRAS CON INICIO ACENTUADO AL FINAL DE LA LISTA
    resultado = []

    i = len(palabras) - 1
    while palabras[i][0] in ('á','é','í','ó','ú'):
        if letra == 'a' and palabras[i][0] == 'á':
            resultado.append(palabras[i])
        elif letra == 'e' and palabras[i][0] == 'é':
            resultado.append(palabras[i])
        elif letra == 'i' and palabras[i][0] == 'í':
            resultado.append(palabras[i])
        elif letra == 'o' and palabras[i][0] == 'ó':
            resultado.append(palabras[i])
        elif letra == 'u' and palabras[i][0] == 'ú':
            resultado.append(palabras[i])

        i -= 1

    return resultado

def main_etapa3():
    alphabetWithAccent=Etapa2.alphabetWithAccent
    diccionario = return_short_words(obtener_lista_definiciones())
    
    # TEST DE CONSIGA
    for i in range(1,101):
        print("Intento numero:",i)
        letras = return_random_letters(alphabetWithAccent)
        rosco = generate_rosco(diccionario, letras)
        for ii in range(len(rosco)):
            print("LETRA:",letras[ii],"| PALABRA:",rosco[ii])

main_etapa3()