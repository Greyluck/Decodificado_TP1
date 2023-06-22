"""Etapa 10: Archivo de Configuración"""
# El responsable de esta etapa es Lucas Aldonate.

# VALORES DE CONFIGURACION POR DEFECTO

DEFAULT_CONFIG = {
    'MIN_WORD_LENGHT': [4, 'omision'],
    'LETTERS_ROSCO_QUANTITY': [10, 'omision'],
    'MAX_GAMES': [5, 'omision'],
    'SUCCESS_POINT':[10, 'omision'],
    'FAIL_POINT': [3, 'omision']
}

# CONSTANTES

END_OF_CONFIG_FILE = ['', ''] # SE UTILIZA PARA SABER CUANDO SE TERMINO POR RECORRER UN ARCHIVO
VALUE = 0  # REPRESENTA EL INDICE DEL VALOR DE LAS VARIABLES DE CONFIGURACION EN EL DICCIONARIO
STATUS = 1 # REPRESENTA EL INDICE DEL ESTADO DE COMO FUERON OBTENIDOS LOS VALORES DE LAS VARIABLES (POR OMISION O CONFIGURACION)

# FUNCIONES

def check_config_file(route, mode = 'r'):
    '''
    Esta funcion recibe como parametros la ruta del archivo de configuracion y establece el modo de solo lectura.
    Se encarga de corroborar que el archivo exista para poder utilizarlo.
    En caso de existir devuelve dicho archivo abierto, caso contrario devuelve un booleano 'None'
    '''
    try:
        config_file = open(route, mode)
    except:
        config_file = None
    return config_file

def obtain_line(config_file):
    '''
    Esta funcion recibe como parametro el archivo previamente abierto en la funcion anterior.
    Se encarga de transformar las lineas del archivo en una lista para poder utilizar sus valores.
    '''
    line = config_file.readline()
    if line == '':
        result = END_OF_CONFIG_FILE
    else:
        result = line.rstrip().split(',')
    return result

def set_game_config(config_file):
    '''
    Esta es la funcion principal de la Etapa10. Se encarga de armar la configuracion que se va a utilizar
    en la partida. 
    Devuelve un diccionario con claves que representan las distintas variables de la configuracion y
    una lista de la forma [value, status] siendo value el numero correspondiente a la variable y status
    si fue agregado por configuracion o por omision.
    '''
    game_config = {} # DICCIONARIO QUE VA A CONTENER LA CONFIGURACION DE LA PARTIDA
    if config_file: # SI EL ARCHIVO EXISTE, SE PROCEDE A ARMAR EL DICCIONARIO CON LA CONFIGURACION DE LA PARTIDA
        line = obtain_line(config_file)
        while line != END_OF_CONFIG_FILE:
            game_variable, value = line 
            if value.isnumeric() and int(value) > 0: # CHEQUEA QUE EL VALOR SEA NUMERICO Y MAYOR A 0. EN CASO DE SERLO ASIGNA EL VALOR POR CONFIGURACION
                game_config[game_variable] = [int(value), 'configuracion']
                line = obtain_line(config_file)
            else: # EN EL CASO DE NO EXISTIR ALGUN VALOR, SE LE ASIGNA EL VALOR POR DEFECTO CORRESPONDIENTE (POR OMISION)
                game_config[game_variable] = DEFAULT_CONFIG[game_variable]
                line = obtain_line(config_file)
        config_file.close()
    else: # SI EL ARCHIVO NO EXISTE LA CONFIGURACION DE LA PARTIDA SERA LA ESTABLECIDA POR DEFECTO (POR OMISION)
        game_config = DEFAULT_CONFIG
    return game_config

def print_game_config(game_config):
    '''
    Esta funcion recibe como parametro el diccionario con la configuracion de la partida.
    Se encarga de imprimir al principio de la partida como fue obtenida dicha configuracion.
    '''
    keys = list(game_config.keys())
    print('La configuracion de esta partida es:')
    for key in keys:
        print(f'{key} = {game_config[key][VALUE]} -> obtenida por {game_config[key][STATUS]}')

config_file = check_config_file('configuracion.csv')
game_config = set_game_config(config_file)
#print_game_config(game_config)

