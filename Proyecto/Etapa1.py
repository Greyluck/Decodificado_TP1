"""Etapa 1: Interacción con usuario"""
# El responsable de esta etapa es Lucas Aldonate.
# El responsable de su revision es Valentino Ceniceros.
# (Esta seccion fue revisada adicionalmente por Emilio Ontiveros.)

def show_letterboard(random_letters): 
    '''
    Esta funcion recibe como parametro la lista de 10 letras seleccionadas al azar (rosco) y se encarga
    de generar el tablero que muesta las letras. Ej: [A] [B] [C] ...
    '''
    letters_list = [f'[{n.upper()}]' for n in random_letters]
    return letters_list

def print_board(board, turns, words, words_dict):
    '''
    Esta funcion recibe como parametros un diccionario (board) con los datos que se imprimen en el tablero (letras y cuadros de aciertos/errores), enteros que representan
    la cantidad de dichos aciertos y errores, la lista de letras; y ademas recibe el numero de turno actual, la lista de palabras y el diccionario palabras|definiciones,
    los cuales utiliza para imprimir el tablero que muestra los detalles de la partida en cada turno
    '''
    print('{}\n{}\n\nAciertos: {}\nErrores: {}\nTurno letra {} - Palabra de {} letras\nDefinicion: {}'.format(
        board['letters_in_board'], board['results_in_board'], board['success'], board['mistake'],
        board['letters_list'][turns][1], len(words[turns]), words_dict[words[turns]]))

def ask_for_word():
    '''
    Esta funcion se encarga de solicitar el ingreso de la palabra
    a adivinar en cada turno
    '''
    word = str.lower(input('Ingrese una única palabra, compuesta solo con letras y de la longitud pedida: '))
    return word
    
def validate_lenght_and_grammar(string, lenght): 
    '''
    Esta funcion recibe como parametros la palabra ingresada por el usuario y la longitud
    de la palabra correcta en dicho turno. La funcion se encarga de validar que dicha
    palabra ingresada sea puramente alfabetica y de la longitud correspondiente
    '''
    while (not string.isalpha()) or (len(string) != lenght):
        print('Error: la palabra no cumple los requisitos pedidos')
        string = ask_for_word()
    return string

def add_answer(board, word, actual_letter, correct_word, turns): 
    '''
    Esta funcion recibe como parametros un diccionario que contiene (el tablero de resultados, los contadores de error y acierto y la lista con las descripciones de cada turno jugado), 
    la palabra y la letra del turno actual, la palabra correcta, el numero de turno actual.
    Se encarga de guardar el resultado de cada turno (acierto/error) con el fin de imprimirlos al final de la partida
    '''
    if word == correct_word:
        board['resultboard'][turns] = '[a]'
        board['success'] += 1
        board['turns_description_list'].append('Turno Letra {} - Palabra de {} letras - {} - acierto'.format(
            actual_letter, len(correct_word), word))
        print('Palabra correcta!\n')
    else:
        board['resultboard'][turns] = '[e]'
        board['mistake'] += 1
        board['turns_description_list'].append('Turno Letra {} - Palabra de {} letras - {} - error - Palabra Correcta: {}'.format(
            actual_letter, len(correct_word), word, correct_word))
        print(f'Palabra incorrecta - La respuesta correcta era: {correct_word}\n')
    return board['success'], board['mistake']

def generate_board(letters):
    '''
    REFACTORIZACION DE CODIGO (Etap6 - PARTE 2 TP)
    Esta funcion recibe como parametro la lista de letras elegidas al azar y crea un diccionario que contiene los
    tableros que se imprimen por pantalla, la lista con las descripciones de cada turno y los contadores de acierto y error.

    * Se utiliza esta funcion que crea el diccionario para que las funciones print_board y add_answer no reciban tantos
    parametros, ya que estos estaran incluidos en el diccionario board.
    '''
    board = {}
    board['letters_list'] = show_letterboard(letters) # TABLERO DE LETRAS ELEGIDAS AL AZAR
    turns_per_match = len(letters) 
    board['resultboard'] = ['[ ]' for n in range(turns_per_match)] # TABLERO DE RESULTADOS 
    board['success'] = 0  # CONTADOR DE ACIERTOS
    board['mistake'] = 0  # CONTADOR DE ERRORES
    board['turns_description_list'] = [] 

    return board
    
def run_match(words_dict, words, random_letters):
    '''
    Esta funcion recibe como parametros el diccionario de palabras|definiciones,
    la lista de palabras a usar y las letras aleatorias.
    Se encarga de generar el desarrollo de la partida, dando uso a la funciones antes definidas.
    Retorna la tupla results que contiene la cantidad de aciertos y errores que posteriormente es
    utilizada en la Etapa 5 para calcular los puntajes.
    (Es la funcion principal de la Etapa 1)
    ''' 
    board = generate_board(random_letters) # GENERA EL DICCIONARIO CON LOS RESPECTIVOS PARAMETROS A UTILIZAR
    turns_per_match = len(random_letters) 
    for turns in range(turns_per_match): # Tambien se podria utilizar while turns < turns_per_match:
        board['letters_in_board'] = ''.join(board['letters_list'])
        board['results_in_board'] = ''.join(board['resultboard'])
        print_board(board, turns, words, words_dict)
        word = validate_lenght_and_grammar(ask_for_word(), len(words[turns])) # VERIFICA LA PALABRA DEPENDIENDO DEL LARGO DE LA PALABRA EN EL TURNO ACTUAL
        board['success'], board['mistake'] = add_answer(board, word, board['letters_list'][turns][1], words[turns], turns)
    board['letters_in_board'] = ''.join(board['letters_list'])
    board['results_in_board'] = ''.join(board['resultboard'])
    print(f'{board["letters_in_board"]}\n{board["results_in_board"]}\n\nAciertos: {board["success"]}\nErrores: {board["mistake"]}') # IMPRIME EL FINAL DE LA PARTIDA ACTUAL
    for answer in board['turns_description_list']: # IMPRIME EL RESULTADO DE CADA TURNO, CON SUS ACIERTOS Y ERRORES CORRESPONDIENTES
        print(answer)
    results = (board['success'], board['mistake'])
    return results

def main_etapa1(): 
    '''
    Esta funcion tiene un rol parecido a lo que seria un main, pero solo destinado a la Etapa 1,
    ejecuta todo lo necesario para poner el juego en funcionamiento de una manera ordenada
    '''
    # ----------------------------------------------------------- # 
    # ACA SE USA LA FUNCION QUE GENERARIA LA LISTA DE LETRAS RANDOM (EN LA ETAPA 3)
    random_letters = ['a','b','c','e','f','g','h','i','t','z']  

    # ACA SE USA LA FUNCION QUE GENERARIA LA LISTA DE 10 PALABRAS (EN LA ETAPA 3)
    words = [n for n in random_letters]  

    # ACA SE USA LA FUNCION QUE GENERARIA EL DICCIONARIO (EN LA ETAPA 2)
    words_dict = {n:f'{n}definicion' for n in random_letters}

    # SE UTILIZARON DATOS CREADOS AL MOMENTO DE DISEÑAR LA ETAPA 1 PARA CORROBORAR SU CORRECTO FUNCIONAMIENTO, YA QUE EN ESE MOMENTO NO ESTABAN LISTAS LAS DEMAS ETAPAS

    # ----------------------------------------------------------- # 
    
    run_match(words_dict, words, random_letters)

#main_etapa1()


