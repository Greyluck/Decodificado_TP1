"""Etapa 1: Interacción con usuario"""
# El responsable de esta etapa es Lucas Aldonate.
# El responsable de su revision es Valentino Ceniceros.
# (Esta seccion fue revisada adicionalmente por Emilio Ontiveros.)

import string 

def show_letterboard(random_letters): 
    '''
    Esta funcion recibe como parametro la lista de 10 letras seleccionadas al azar (rosco) y se encarga
    de generar el tablero que muesta las letras: [A] [B] [C] ...
    '''
    letters_list = [f'[{n.upper()}]' for n in random_letters]
    return letters_list

def print_board(letters_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict):
    '''
    Esta funcion recibe como parametros los datos necesarios para poder
    imprimir el tablero que muestra los detalles de la partida en cada turno
    '''
    print('{}\n{}\n\nAciertos: {}\nErrores: {}\nTurno letra {} - Palabra de {} letras\nDefinicion: {}'.format(
        letters_in_board, results_in_board, success, mistake, letters_list[turns][1], len(words[turns]), words_dict[words[turns]]))

def ask_for_word():
    '''
    Esta funcion se encarga de solicitar el ingreso de la palabra
    a adivinar en cada turno
    '''
    word = str(input('Ingrese una única palabra, compuesta solo con letras y de la longitud pedida: '))
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

def add_answer(word, actual_letter, correct_word, resultboard, turns_description_list, turns, success, mistake): 
    '''
    Esta funcion recibe como parametros los datos necesarios para guardar el resultado de cada turno
    con el fin de imprimirlos al final de la partida, asi como tambien decide si el usuario acerto o cometio
    un error adivinando la palabra
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
    
def run_match(words_dict, words, random_letters):
    '''
    Esta funcion recibe como parametros el diccionario de palabras:definiciones y la lista de palabras a usar.
    Se encarga de generar el desarrollo de la partida.
    (Es la funcion principal de la Etapa 1)
    '''
    letters_list = show_letterboard(random_letters) # MUESTRA EL TABLERO DE LETRAS ELEGIDAS AL AZAR
    turns_per_match = len(letters_list) 
    resultboard = ['[ ]' for n in range(turns_per_match)] # CREA EL TABLERO DE RESULTADOS
    turns = 0 # ITERADOR TANTO DE LAS LETRAS COMO DE LA PALABRA EN EL TURNO ACTUAL
    success = 0 # CONTADOR DE ACIERTOS
    mistake = 0 # CONTADOR DE ERRORES
    turns_description_list = []
    while turns < turns_per_match:
        letters_in_board = ''.join(letters_list)
        results_in_board = ''.join(resultboard)
        print_board(letters_in_board, results_in_board, success, mistake, letters_list, turns, words, words_dict)
        word = validate_lenght_and_grammar(ask_for_word(), len(words[turns])) # VERIFICA LA PALABRA DEPENDIENDO DEL LARGO DE LA PALABRA EN EL TURNO ACTUAL
        success, mistake = add_answer(word, letters_list[turns][1], words[turns], resultboard, turns_description_list, turns, success, mistake)
        turns += 1
    letters_in_board = ''.join(letters_list)
    results_in_board = ''.join(resultboard)
    print(f'{letters_in_board}\n{results_in_board}\n\nAciertos: {success}\nErrores: {mistake}') # IMPRIME EL FINAL DE LA PARTIDA ACTUAL
    for answer in turns_description_list: # IMPRIME EL RESULTADO DE CADA TURNO, CON SUS ACIERTOS Y ERRORES CORRESPONDIENTES
        print(answer)
    results = (success, mistake)
    return results
    # PUEDE RETORNAR CANTIDAD DE ACIERTOS Y ERRORES PARA IR CALCULANDO RESULTADOS (10 PTS ACIERTO/-3 PTS ERROR) CON ETAPA 5

def main_etapa1(): 
    '''
    Esta funcion tiene un rol parecido a lo que seria un main, pero solo destinado a la Etapa 1,
    ejecuta todo lo necesario para poner el juego en funcionamiento de una manera ordenada
    '''
    # ----------------------------------------------------------- # 
    # ACA SE USA LA FUNCION QUE GENERARIA EL DICCIONARIO (EN LA ETAPA 2)
    words_dict = {n:f'{n}definicion' for n in string.ascii_lowercase}

    # ACA SE USA LA FUNCION QUE GENERARIA LA LISTA DE 10 PALABRAS (EN LA ETAPA 3)
    words = [n for n in string.ascii_lowercase[:10]]  

    # ACA SE USA LA FUNCION QUE GENERARIA LA LISTA DE LETRAS RANDOM (EN LA ETAPA 3)
    random_letters = ['a','b','c','e','f','g','h','i','t','z']  
    # ----------------------------------------------------------- # 
    
    run_match(words_dict, words, random_letters)
    # ACA VA LA ETAPA 5

#main_etapa1()


