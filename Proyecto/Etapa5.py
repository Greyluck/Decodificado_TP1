"""Etapa 5: Puntaje"""
# El responsable de esta etapa es Valentino Ceniceros.
# El responsable de su revision es Emilio Ontiveros.

import Etapa4

def acumulate_points(results,SUCCESS_POINTS = 10, FAIL_POINTS = -3):
    """
    Eecibe una tupla con aciertos y errores y devuelve el puntaje total del juego como entero
    """
    SUCCESS_INDEX = 0
    FAIL_INDEX = 1
    success_point = results[SUCCESS_INDEX] * SUCCESS_POINTS
    fail_point = results[FAIL_INDEX] * FAIL_POINTS
    return success_point + fail_point

def play_match():
    """
    Le pregunta al jugador si desea seguir jugando y luego almacena y muestra el puntaje final.
    """
    points = 0
    decision = True 
    while decision:
        results = Etapa4.play_the_game()
        points += acumulate_points(results)
        print(f"Puntaje Final: {points}")
        play_again = str(input("si desea seguir jugando, escriba s, caso contrario el juego terminara "))
        if play_again != 's':
            decision = False
            
def main_etapa5():
    """ 
    ejecuta el juego
    """
    play_match()

main_etapa5()