"""Etapa 4: Integracion"""
# El responsable de esta etapa es Emilio Ontiveros.
# El responsable de su revision es Santiago Testa.

import Etapa1
import Etapa2
import Etapa3
import Etapa5

debugMode=True
if debugMode: print("In debug mode")

def play_the_game():
    if debugMode: print(" - Ejecutando play_the_game")
    
    # Generación del diccionario de palabras.
    generateDiccionary()
    
    # Seleccion de letras participantes
    selectLetters()

    # Seleccion de lista de palabras a adivinar
    
        
    # Creacion del tablero

    return True

def main():
    # -----------------------------------------------------------------------------------------------
    # La funcion main_etapa1() ejecuta todos los puntos requeridos para esta etapa,
    # como fueron realizados en etapas previas, se la incluye aqui solo a modo de muestra.
    # debajo de la linea se continua con la ejecucion del programa segun lo pedido para esta etapa.
    # -----------------------------------------------------------------------------------------------

    # Start
    play_the_game()





def generateDiccionary():
    """Genera y devuelve el diccionario a ser usado durante el juego"""
    # Obtiene una lista aleatoria de definiciones
    main_list = Etapa2.obtener_lista_definiciones()
    
    # Filtra las listas para que regrese aquellas cuyo largo es valido (Mayor a 5)
    short_word_dicc = Etapa2.return_short_words(main_list)

    if debugMode: print(" - Imprimiendo diccionario de palabras cortas\n", short_word_dicc )

def selectLetters():
    """Selecciona las letras participantes"""
    # TODO Como la etapa 3 no fue entregada todavia se utilizara una lista hardocdeada a modo de placeholder hasta
    # que la etapa 3 este terminada. Esta lista contiene 10 letras (que deberian ser aleatorias)
    words = ["a","b","c","r","t", "o","h","ñ","j","k"] 
    return words

main()