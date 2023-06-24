"""Etapa 9: Dinámica del juego"""
# El responsable de esta etapa es Santiago Testa.

import Etapa1   # TP1 - Interfaz de consola
import Etapa2   # TP1 - Generacion de diccionario
import Etapa3   # TP1 - Generacion aleatoria de letras y palabras
'''
import Etapa7   # TP2 - Llamado de usuarios
'''
import Etapa8
import Etapa10  # TP2 - Configuracion del juego

import random
import os

from datos import obtener_lista_definiciones

DEBUG_MODE = False


def print_board(board, words, words_dict, players):
    '''
    Edit Santi - Parte 9: Se modularizo esta funcion debido a que es mas complejo que la Etapa1

    Argumentos: Diccionario de tablero (letras, aciertos, etc), palabras, diccionario de palabras y jugadores
    Funcionalidad: Imprime tablero, resultados del juego (aciertos y turnos) y jugada
    Return: Funcion void
    Nota: Se modularizo esta función (la original corresponde a la etapa1)
    '''

    print('{}\n{}\n{}\n\nJugadores:'.format(''.join(board['letter_board']), ''.join(board['result_board']), ''.join(board['turn_board'])))
    print_players_result(board,players)
    print_play(board, words, words_dict, players)
    
def print_players_result(board,players):
    '''
    Argumentos: lista de aciertos, la cantidad de errores y los jugadores. 
    Funcionalidad: Itera mostrando aciertos y errores de cada jugador
    Return = Funcion void. 

    Nota: Como errores es un entero, y los errores se suman incrementalmente por jugador, entonces los 
    errores para cada jugador seran el resultado de la division, y el resto se dividira un punto por jugador
    hasta quedarnos sin puntos
    Ejemplo Nota: 10 errores, 4 jugadores. 
    9/4 = 2 -> Todos los jugadores cometieron dos errores
    9%4 = 2 -> Primer y segundo jugador se equivocaron (se suma 1 si tu indice es menor que 2). 
    Resultado final = 3 3 2 2 errores
    '''
    success = board['success']
    mistake = board['mistake']

    AMOUNT_OF_PLAYERS = len(players)
    player_mistakes = 0

    # Iteracion por los jugadores, calculando errores por jugador y mostrando resultados
    for player_number in range(AMOUNT_OF_PLAYERS):
        # Calcular errores
        player_mistakes = mistake // AMOUNT_OF_PLAYERS
        if player_number < mistake % AMOUNT_OF_PLAYERS:
            player_mistakes += 1

        # Mostrar el resultado del jugador
        print("{}. {} - Aciertos: {} - Errores: {}".format(
            player_number + 1, players[player_number],success[player_number], player_mistakes))

    print('\n') 

def print_play(board, words, words_dict, players):
    '''
    Argumentos: Aciertos/errores, lista de letras, palabras, diccionario y jugadores
    Funcionalidad: Mostrar mensaje de Jugador que debe responder, letra palabra y definicion
    Return: Funcion void

    Nota: La idea de que calcule el turno es minimizar la cantidad de datos guardados por la funcion
    '''
 
    mistake = board['mistake']
    success = board['success']
    letters_list = board['letter_board']

    # Calculo de turnos jugados, sumando aciertos y errores (minimizar cant. de variables)
    turns = mistake
    for success in success:
        turns += success

    # Mostrar jugada
    AMOUNT_OF_PLAYERS = len(players)
    number_player_inplay = mistake%AMOUNT_OF_PLAYERS
    print('Turno Jugador {} {} - letra {} - Palabra de {} letras\nDefinicion: {}'.format(
        number_player_inplay + 1, players[number_player_inplay], letters_list[turns][1], len(words[turns]), words_dict[words[turns]]))

def print_points(points,players,games_played):
    '''
    Argumentos: Lista de puntos (total o parcial), lista de jugadores y partidas jugadas hasta el momento
    Funcionalidad: Imprime puntaje parcial si games_played es -1, caso contrario imprime puntaje final del rosco
    Return: Funcion void
    '''
    if games_played == -1:
        print('Puntaje parcial:')
    else:
        print('---------------------------------------------------------------')
        print('Reporte final:\nPartidas jugadas: {}\n\nPuntaje final:'.format(games_played))

    points_sorted = sorted(points.items(), key=lambda x:x[1], reverse=True)
    for player in range(len(players)):
        print('{}. {} - {} puntos'.format(player + 1, points_sorted[player][0],points_sorted[player][1]))

def calculate_points(success, mistake):
    '''
    Argumentos: Lista de aciertos y cantidad de errores
    Funcionalidad: Calcula los puntos de cada jugador segun la configuracion y los aciertos/errores
    Return: Puntos de cada jugador
    '''
    AMOUNT_OF_PLAYERS = len(success)
    
    result = [ success * Etapa10.game_config['SUCCESS_POINT'][Etapa10.VALUE] for success in success]
    for player_num in range(AMOUNT_OF_PLAYERS):
        result[player_num] -= mistake//AMOUNT_OF_PLAYERS * Etapa10.game_config['FAIL_POINT'][Etapa10.VALUE]
        if player_num < mistake%AMOUNT_OF_PLAYERS:
            result[player_num] -= Etapa10.game_config['FAIL_POINT'][Etapa10.VALUE]
    return result

def add_answer(board, word, words, turns, players): 
    '''
    Argumentos: palabra y la letra del turno actual, la palabra correcta, la lista de aciertos/errores, lista de resultados de cada turno, el numero de turno actual y la cantidad de aciertos y errores
    Funcionalidad: Misma funcion que Etapa1 pero adaptada a las funcionalidades de esta etapa. Se agrega turnboard
    Return: Lista de aciertos y cantidad de errores
    '''
    AMOUNT_OF_PLAYERS = len(players)
    player_num = board['mistake']%AMOUNT_OF_PLAYERS
    board['turn_board'][turns] = '[' + str(player_num + 1) + ']'

    if word == words[turns]:
        board['result_board'][turns] = '[a]'
        board['success'][player_num] += 1
        board['turns_description'].append('Turno Letra {} - Jugador {} {} - Palabra de {} letras - {} - acierto'.format(
            words[turns][0],player_num + 1, players[player_num], len(words[turns]), word))
        print('Palabra correcta!\n')
    else:
        board['result_board'][turns] = '[e]'
        board['mistake'] += 1
        board['turns_description'].append('Turno Letra {} - Jugador {} {} - Palabra de {} letras - {} - error - Palabra Correcta: {}'.format(
            words[turns][0],player_num + 1, players[player_num], len(words[turns]), word, words[turns]))
        print('Palabra incorrecta - La respuesta correcta era: {}\n'.format(words[turns]))
    
def generate_board(letters, players):
    '''
    Argumentos: Letras
    Funcionalidad: Genera un diccionario que representa el tablero y ordena el juego
    Return: Diccionario
    '''
    result = {}

    result['letter_board'] = Etapa1.show_letterboard(letters)           # TABLERO DE LETRAS ELEGIDAS AL AZAR

    turns_per_match = len(letters) 
    result['result_board'] = ['[ ]' for n in range(turns_per_match)]    # TABLERO DE ACIERTO/ERROR
    result['turn_board'] = ['[ ]' for n in range(turns_per_match)]      # TABLERO DE TURNOS

    result['success'] = [0 for player in players]                       # LISTA DE CONTADORES DE ACIERTOS POR JUGADOR
    result['mistake'] = 0                                               # CONTADOR DE ERRORES, COMUN A JUGADORES                               

    result['turns_description'] = []

    return result

def run_match(words_dict, words, random_letters, players):
    '''
    Argumentos: Diccionario de palabras, palabras aleatorias, letras aleatorias y jugadores
    Funcionalidad: Corre partida (run_match Etapa1 adaptado a esta etapa)
    Return: Lista de puntos de la partida
    ''' 

    board = generate_board(random_letters, players)
    turns_per_match = len(random_letters)  

    for turns in range(turns_per_match): # Tambien se podria utilizar while turns < turns_per_match:

        print_board(board, words, words_dict, players)
        # Solicitar palabra y agregar resultado
        word = Etapa1.validate_lenght_and_grammar(Etapa1.ask_for_word(), len(words[turns])) # VERIFICA LA PALABRA DEPENDIENDO DEL LARGO DE LA PALABRA EN EL TURNO ACTUAL
        os.system('cls')
        add_answer(board, word, words, turns, players)

    # Resultado final 
    for answer in board['turns_description']: # IMPRIME EL RESULTADO DE CADA TURNO, CON SUS ACIERTOS Y ERRORES CORRESPONDIENTES
        print(answer)

    # Calcular puntos, imprimirlos y devolverlos
    points = calculate_points(board['success'], board['mistake'])
    print('\nPuntaje de la partida:')
    for index in range(len(points)):
        print('{}. {} - {} puntos'.format(index + 1, players[index], points[index]))
    print('\n')
    return points

def run_full_game(players):
    '''
    Argumentos: Lista de jugadores
    Funcionalidad: Itera creando nuevas partidas hasta llegar al maximo o hasta que los usuarios no quieran seguir jugando
    Return: Funcion void
    DebugMode:  define por default letras y palabras (Idem etapa1)
    '''
    word_dictionary = {}
    random_letters = []
    random_words = []
    
    total_points = { player: 0 for player in players}
    partial_points = total_points

    # Si esta en modo debug, defini los valores de prueba hardcodeados
    # Si no lo esta, genera el diccionario
    if DEBUG_MODE:
        random_letters = ['a','b','c','e','f','g','h','i','t','z']
        random_words = ['a','b','c','e','f','g','h','i','t','z']
        word_dictionary = {n:f'{n} definicion' for n in random_letters}
    else:
        word_dictionary = Etapa8.return_words_and_definition()
        Etapa8.return_file_csv(word_dictionary)

    # print(word_dictionary)
    # Iterar jugando al rosco hasta llegar a cant. partidas maximas o hasta que no quieran jugar
    games_played = 0
    play_game = True
    AMOUNT_OF_PLAYERS = len(players)

    while play_game:
        random.shuffle(players)
        partial_points = [0 for n in range(AMOUNT_OF_PLAYERS)]
        if not DEBUG_MODE:
            random_words = Etapa3.generate_random_letters_and_words(Etapa2.ALPHABET, word_dictionary)
            random_letters = Etapa3.return_first_letter_of_words(random_words)
            '''
            random_letters = Etapa3.return_random_letters(Etapa2.ALPHABET)
            random_words = Etapa3.generate_rosco(word_dictionary,random_letters)
            '''

        # Correr partida, sumar puntos al total y preguntar si seguimos
        partial_points = run_match(word_dictionary, random_words, random_letters, players)
        for index in range(AMOUNT_OF_PLAYERS):
            total_points[players[index]] += partial_points[index]
        print_points(total_points,players,-1)

        games_played += 1
        play_game = check_and_ask_for_another_game(games_played)
        os.system('cls')

    os.system('cls')

    print_points(total_points, players, games_played)
    print('-------------------------------------------')
    print('¡Hasta la proxima!')
    print('-------------------------------------------')

def ask_for_another_game(games_played):
    '''
    Argumentos: Partidas jugadas (debe ser menor que el maximo de partidas)
    Funcionalidad: Pregunta al usuario si quiere seguir jugando
    Return: True si usuario quiere seguir jugando
    '''
    remaining_games = Etapa10.game_config['MAX_GAMES'][Etapa10.VALUE] - games_played

    print('\n')
    # Mensaje de partidas restantes a usuario/s (No se utiliza if condensado debido a que seria muy largo)
    if remaining_games > 1:
        print("Quedan {} partidas ¿Jugamos otra?".format(remaining_games))
    else:
        print("Queda 1 partida ¿Jugamos la última?")

    # Loop de solicitud al usuario
    input_user = 'Algo random para que empiece a iterar, Victoria Alonso es la última patriota viva'
    while input_user != 's' and input_user != 'n':
        input_user = input("Si [s] / No [n]: ").lower()
        if input_user != 's' and input_user != 'n':
            print("Input invalido, favor reingresar")

    print('\n')
    return (input_user == 's')


def check_and_ask_for_another_game(games_played):
    '''
    Argumentos: Partidas jugadas al momento
    Funcionalidad: Calcula partidas restantes y devuelve true/false segun cant. partidas restantes y decision de usuario
    Return: True si hay partidas restantes y usuario desea jugar otra. False en caso contrario
    Esta funcion recibe la cantidad de partidas jugadas y calcula las partidas restantes disponibles para jugar
    Solo consulta al usuario si quedan partidas disponibles. Caso contrario devuelve False

    Notacion utilizada: If condensado según PEP 75.40.2.1
    '''
    remaining_games = Etapa10.game_config['MAX_GAMES'][Etapa10.VALUE] - games_played
    return False if remaining_games == 0 else ask_for_another_game(games_played)

def play_new_rosco(players):
    '''
    Argumentos: Recibe lista jugadores
    Funcionalidad: MAIN DE ETAPA9. Setea configuracion,
    Return: Void
    '''
    os.system('cls')
    Etapa10.print_game_config(Etapa10.game_config)
    input('\n\nPresione enter para empezar! ')
    os.system('cls')
    run_full_game(players)

def main_etapa9(): 
    '''
    Main de la etapa. Para probar la funcion, DEBUG MODE debe ser True
    '''
    play_new_rosco(['ej1','ej2','ej3'])

main_etapa9()


