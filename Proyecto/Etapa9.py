"""Etapa 9: Dinámica del juego"""
# El responsable de esta etapa es Santiago Testa.

import Etapa1   # TP1 - Interfaz de consola
import Etapa2   # TP1 - Generacion de diccionario
import Etapa3   # TP1 - Generacion aleatoria de letras y palabras
'''
import Etapa7   # TP2 - Llamado de usuarios
'''
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
    Edit Santi - Parte 9: Se modularizo esta funcion debido a que es mas complejo que la Et

    Esta funcion recibe como parametros los datos que se imprimen en el tablero (letras y cuadros de aciertos/errores), enteros que representan
    la cantidad de dichos aciertos y errores, la lista de letras, el numero de turno actual, la lista de palabras y el diccionario palabras|definiciones,
    los cuales utiliza para imprimir el tablero que muestra los detalles de la partida en cada turno
    '''
    print('{}\n{}\n{}\n\nJugadores:\n'.format(letters_in_board, turns_in_board, results_in_board)) 
    print_players_result(success,mistake,players)   # Imprimir resultado parcial de jugadores
    print_play()

def print_players_result(success,mistake,players):
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

def print_play(success, mistake, letters_list, words, words_dict, players):
    '''
    Argumentos: Aciertos/errores, lista de letras, palabras, diccionario y jugadores
    Funcionalidad: Mostrar mensaje de Jugador que debe responder, letra palabra y definicion
    Return: Funcion void

    Nota: La idea de que calcule el turno es minimizar la cantidad de datos guardados por la funcion
    '''
    # Calculo de turnos jugados, sumando aciertos y errores (minimizar cant. de variables)
    turns = mistake
    for success in success:
        turns += success

    # Mostrar jugada
    AMOUNT_OF_PLAYERS = len(players)
    number_player_inplay = mistake%AMOUNT_OF_PLAYERS
    print('Turno Jugador {} {} - letra {} - Palabra de {} letras\nDefinicion: {}'.format(
        number_player_inplay + 1, players[number_player_inplay], letters_list[turns][1], len(words[turns]), words_dict[words[turns]]))

def print_total_points(total_points,players,games_played):
    if games_played == -1:
        print('Puntaje parcial:')
    else:
        print('Reporte final:\nPartidas jugadas: {}\n\nPuntaje final:'.format(games_played))

    for player in range(len(players)):
        print('{}. {} - {} puntos'.format(player + 1, players[player],total_points[player]))

def calculate_points(success, mistake):
    AMOUNT_OF_PLAYERS = len(success)
    
    result = [ success * Etapa10.game_config['SUCCESS_POINT'][0] for success in success]
    for player_num in range(AMOUNT_OF_PLAYERS):
        result[player_num] -= mistake//AMOUNT_OF_PLAYERS * Etapa10.game_config['FAIL_POINT'][0]
        if player_num < mistake%AMOUNT_OF_PLAYERS:
            result[player_num] -= Etapa10.game_config['FAIL_POINT'][0]
    return result

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

def add_answer(word, actual_letter, correct_word, resultboard, turnboard, turns_description_list, turns, success, mistake, players): 
    '''
    Edit Santi - Parte 9:  Se debe agregar el turnboard

    Esta funcion recibe como parametros la palabra y la letra del turno actual, la palabra correcta, la lista de aciertos/errores,
    la lista de resultados de cada turno, el numero de turno actual y la cantidad de aciertos y errores hasta el momento.
    Se encarga de guardar el resultado de cada turno (acierto/error) con el fin de imprimirlos al final de la partida
    '''
    AMOUNT_OF_PLAYERS = len(players)
    player_num = mistake%AMOUNT_OF_PLAYERS
    turnboard[turns] = '[' + chr(player_num) + ']'

    if word == correct_word:
        resultboard[turns] = '[a]'
        success[player_num] += 1
        turns_description_list.append('Turno Letra {} - Jugador {} {} - Palabra de {} letras - {} - acierto'.format(
            actual_letter,player_num + 1, players[player_num], len(correct_word), word))
        print('Palabra correcta!\n')
    else:
        resultboard[turns] = '[e]'
        mistake += 1
        turns_description_list.append('Turno Letra {} - Jugador {} {} - Palabra de {} letras - {} - error - Palabra Correcta: {}'.format(
            actual_letter,player_num + 1, players[player_num], len(correct_word), word, correct_word))
        print('Palabra incorrecta - La respuesta correcta era: {}\n'.format(correct_word))
    return success, mistake
    
def run_match(words_dict, words, random_letters, players):
    '''
    ''' 
    # Lista letra, jugador de turno, acierto si o no 
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

        # Imprimir Tablero, resultado de jugadores y jugada que se va a hacer (ex print board)
        print('{}\n{}\n{}\n\nJugadores:\n'.format(letters_in_board, turns_in_board, results_in_board)) 
        print_players_result(success,mistake,players)
        print_play(success, mistake, letters_list, words, words_dict, players)

        # Solicitar palabra y agregar resultado
        word = Etapa1.validate_lenght_and_grammar(Etapa1.ask_for_word(), len(words[turns])) # VERIFICA LA PALABRA DEPENDIENDO DEL LARGO DE LA PALABRA EN EL TURNO ACTUAL
        success, mistake = add_answer(word, letters_list[turns][1], words[turns], resultboard, turnboard, turns_description_list, turns, success, mistake, players)
        # add_answer(word, actual_letter, correct_word, resultboard, turnboard, turns_description_list, turns, success, mistake, players): 
    letters_in_board = ''.join(letters_list)
    results_in_board = ''.join(resultboard)

    # Resultado final
    for answer in turns_description_list: # IMPRIME EL RESULTADO DE CADA TURNO, CON SUS ACIERTOS Y ERRORES CORRESPONDIENTES
        print(answer)

    # Calcular puntos, imprimirlos y devolverlos
    points = calculate_points(success, mistake)
    print('\nPuntaje de la partida:')
    for index in range(len(points)):
        print('{}. {} - {} puntos'.format(index + 1, players[index], points[index]))
    print('\n')
    return points

def run_full_game(players):
    '''
    Esta funcion itera creando nuevas partidas hasta llegar al maximo o hasta que los usuarios no quieran seguir jugando
    En modo debug define por default letras y palabras (Idem etapa1)
    '''
    word_dictionary = {}
    random_letters = []
    random_words = []
    
    total_points = [0 for n in range(len(players))]
    partial_points = total_points

    # Si esta en modo debug, defini los valores de prueba hardcodeados
    # Si no lo esta, genera el diccionario
    if DEBUG_MODE:
        random_letters = ['a','b','c','e','f','g','h','i','t','z']
        random_words = ['a','b','c','e','f','g','h','i','t','z']
        word_dictionary = {n:f'{n} definicion' for n in random_letters}
    else:
        word_dictionary = Etapa2.return_short_words()

    # Iterar jugando al rosco hasta llegar a cant. partidas maximas o hasta que no quieran jugar
    games_played = 0
    play_game = True
    while play_game:
        partial_points = [0 for n in range(len(players))]
        if not DEBUG_MODE:
            random_letters = Etapa3.return_random_letters()
            random_words = Etapa3.generate_rosco()

        # Correr partida, sumar puntos al total y preguntar si seguimos
        partial_points = run_match(word_dictionary, random_words, random_letters, players)
        for index in range(len(total_points)):
            total_points[index] += partial_points[index]
        print_total_points(total_points,players,-1)

        games_played += 1
        play_game = check_and_ask_for_another_game(games_played)

    print_total_points(total_points, players, games_played)
    print('-------------------------------------------')
    print('¡Hasta la proxima!')
    print('-------------------------------------------')

def ask_for_another_game(games_played):
    remaining_games = Etapa10.game_config['MAX_GAMES'][0] - games_played

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
    remaining_games = Etapa10.game_config['MAX_GAMES'][0] - games_played
    return False if remaining_games == 0 else ask_for_another_game(games_played)

def play_new_rosco():
    Etapa10.print_game_config(Etapa10.set_game_config())
    players = ['a1','a2','a3','a4']
    if not DEBUG_MODE:
       '''
       players = Etapa7.   Traer Jugadores
       '''  
       a = 2
       print(a)
    run_full_game(players)

def main_etapa9(): 
    '''
    Main de la etapa. Para probar la funcion, DEBUG MODE debe ser True
    '''
    play_new_rosco()

#main_etapa9()


