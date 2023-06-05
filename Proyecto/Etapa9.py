"""Etapa 9: Dinámica del juego"""
# El responsable de esta etapa es Santiago Testa.

import Etapa1   # TP1 - Interfaz de consola
import Etapa2   # TP1 - Generacion de diccionario
import Etapa3   # TP1 - Generacion aleatoria de letras y palabras
import Etapa7   # TP2 - Llamado de usuarios
import Etapa10  # TP2 - Configuracion del juego

DEBUG_MODE = True

def show_letterboard(random_letters): 
    '''
    Edit Santi - Parte 9: Esta funcion no requiere cambios

    Esta funcion recibe como parametro la lista de 10 letras seleccionadas al azar (rosco) y se encarga
    de generar el tablero que muesta las letras. Ej: [A] [B] [C] ...
    '''
    letters_list = [f'[{n.upper()}]' for n in random_letters]
    return letters_list

def print_board(letters_in_board, turns_in_board, results_in_board,success, mistake, letters_list, turns, words, words_dict, players):
    '''
    Edit Santi - Parte 9: Se agrega turnos al tablero, y se modulariza el mostrar los resultados

    Esta funcion recibe como parametros los datos que se imprimen en el tablero (letras y cuadros de aciertos/errores), enteros que representan
    la cantidad de dichos aciertos y errores, la lista de letras, el numero de turno actual, la lista de palabras y el diccionario palabras|definiciones,
    los cuales utiliza para imprimir el tablero que muestra los detalles de la partida en cada turno
    '''
    print('{}\n{}\n{}\n\n'.format(letters_in_board, turns_in_board, results_in_board))
    print_play_result(success, mistake, letters_list, turns, words, words_dict)

def print_play_result(success, mistake, letters_list, turns, words, words_dict, players):
    print('Aciertos: {}\nErrores: {}\nTurno letra {} - Palabra de {} letras\nDefinicion: {}'.format(
        success[mistake % len(players)], mistake, letters_list[turns][1], len(words[turns]), words_dict[words[turns]]))

def ask_for_word():
    '''
    Edit Santi - Parte 9: Esta funcion no requiere cambios 

    Esta funcion se encarga de solicitar el ingreso de la palabra
    a adivinar en cada turno
    '''
    word = str.lower(input('Ingrese una única palabra, compuesta solo con letras y de la longitud pedida: '))
    return word
    
def validate_lenght_and_grammar(string, lenght): 
    '''
    Edit Santi - Parte 9: Esta funcion no requiere cambios     
    
    Esta funcion recibe como parametros la palabra ingresada por el usuario y la longitud
    de la palabra correcta en dicho turno. La funcion se encarga de validar que dicha
    palabra ingresada sea puramente alfabetica y de la longitud correspondiente
    '''
    while (not string.isalpha()) or (len(string) != lenght):
        print('Error: la palabra no cumple los requisitos pedidos')
        string = ask_for_word()
    return string

def add_answer(word, actual_letter, correct_word, resultboard, turnboard, turns_description_list, turns, success, mistake): 
    '''
    Edit Santi - Parte 9:  Se debe agregar el turnboard

    Esta funcion recibe como parametros la palabra y la letra del turno actual, la palabra correcta, la lista de aciertos/errores,
    la lista de resultados de cada turno, el numero de turno actual y la cantidad de aciertos y errores hasta el momento.
    Se encarga de guardar el resultado de cada turno (acierto/error) con el fin de imprimirlos al final de la partida
    '''
    if word == correct_word:
        resultboard[turns] = '[a]'
        success += 1
        turns_description_list.append('Turno Letra {} - Palabra de {} letras - {} - acierto'.format(
            actual_letter, len(correct_word), word))
        print('Palabra correcta!\n')
    else:
        resultboard[turns] = '[e]'
        mistake += 1
        turns_description_list.append('Turno Letra {} - Palabra de {} letras - {} - error - Palabra Correcta: {}'.format(
            actual_letter, len(correct_word), word, correct_word))
        print(f'Palabra incorrecta - La respuesta correcta era: {correct_word}\n')
    return success, mistake
    
def run_match(words_dict, words, random_letters, players):
    '''
    Edit Santi - Parte 9: Se 

    Esta funcion recibe como parametros el diccionario de palabras|definiciones,
    la lista de palabras a usar y las letras aleatorias.
    Se encarga de generar el desarrollo de la partida, dando uso a la funciones antes definidas.
    Retorna la tupla results que contiene la cantidad de aciertos y errores que posteriormente es
    utilizada en la Etapa 5 para calcular los puntajes.
    (Es la funcion principal de la Etapa 1)
    ''' 
    letters_list = Etapa1.show_letterboard(random_letters) # TABLERO DE LETRAS ELEGIDAS AL AZAR
    turns_per_match = len(letters_list) 
    resultboard = ['[ ]' for n in range(turns_per_match)] # CREA EL TABLERO DE RESULTADOS
    turnboard = resultboard
    
    # turns = 0 (comentado porque el for ya lo inicializa) # ITERADOR TANTO DE LAS LETRAS COMO DE LA PALABRA EN EL TURNO ACTUAL
    success = [0 for player in players] # LISTA DE CONTADORES DE ACIERTOS POR JUGADOR
    mistake = 0 # CONTADOR DE ERRORES (general de todos, no es necesario distinguirlos)
    turns_description_list = []
    for turns in range(turns_per_match): # Tambien se podria utilizar while turns < turns_per_match:
        letters_in_board = ''.join(letters_list)
        results_in_board = ''.join(resultboard)
        turns_in_board = ''.join(turnboard)
        print_board(letters_in_board, turns_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict)

        # Solicitar palabra y agregar resultado
        word = Etapa1.validate_lenght_and_grammar(Etapa1.ask_for_word(), len(words[turns])) # VERIFICA LA PALABRA DEPENDIENDO DEL LARGO DE LA PALABRA EN EL TURNO ACTUAL
        success, mistake = add_answer(word, letters_list[turns][1], words[turns], resultboard, turns_description_list, turns, success, mistake)
    
    letters_in_board = ''.join(letters_list)
    results_in_board = ''.join(resultboard)


    # Resultado final
    print(f'{letters_in_board}\n{results_in_board}\n\nAciertos: {success}\nErrores: {mistake}') # IMPRIME EL FINAL DE LA PARTIDA ACTUAL
    for answer in turns_description_list: # IMPRIME EL RESULTADO DE CADA TURNO, CON SUS ACIERTOS Y ERRORES CORRESPONDIENTES
        print(answer)
    results = (success, mistake)
    return results

def run_full_game(players):
    '''
    Esta funcion itera creando nuevas partidas hasta llegar al maximo o hasta que los usuarios no quieran seguir jugando
    '''
    games_played = 0
    play_game = True

    while play_game:
        if DEBUG_MODE:
            random_letters = ['a','b','c','e','f','g','h','i','t','z']
            random_words = ['a','b','c','e','f','g','h','i','t','z']
            word_dictionary = {n:f'{n} definicion' for n in random_letters}
        else:
            word_dictionary = Etapa2.return_short_words()
            random_letters = Etapa3.return_random_letters()
            random_words = Etapa3.generate_rosco()

        run_match(word_dictionary, random_words, random_letters, players)
        games_played += 1
        play_game = check_and_ask_for_another_game(games_played)

def ask_for_another_game(games_played):
    remaining_games = Etapa10.game_config['MAX_GAMES'] - games_played

    # Mensaje de partidas restantes a usuario/s (No se utiliza if condensado debido a que seria muy largo)
    if remaining_games > 1:
        print("Quedan {} partidas ¿Jugamos otra?".format(remaining_games))
    else:
        print("Queda 1 partida ¿Jugamos la última?")

    # Loop de solicitud al usuario
    input_user = 'Algo random para que empiece a iterar, Victoria Alonso es la última patriota viva'
    while input_user != 's' and input_user != 'n':
        input_user = input("Si [s] / No [n]:").lower()

    return (input_user == 's')


def check_and_ask_for_another_game(games_played):
    '''
    Esta funcion recibe la cantidad de partidas jugadas y calcula las partidas restantes disponibles para jugar
    Solo consulta al usuario si quedan partidas disponibles. Caso contrario devuelve False

    Notacion utilizada: If condensado según PEP 75.40.2.1
    '''
    remaining_games = Etapa10.game_config['MAX_GAMES'] - games_played
    return False if remaining_games == 0 else ask_for_another_game(games_played)

def play_new_rosco():
    Etapa10.set_game_config()
    # players = Etapa7.   Traer Jugadores
    # run_full_game(players)

def main_etapa9(): 
    '''
    Main de la etapa. Para probar la funcion, DEBUG MODE debe ser True
    '''
    play_new_rosco()

#main_etapa9()


