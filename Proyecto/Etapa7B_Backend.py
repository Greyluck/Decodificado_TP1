"""
constantes y variables globales
"""
debug_mode = False
ARCHIVE_END = ['','']
MAX_LENGHT_PASS = 12
MIN_LENGHT_PASS = 6
MAX_LENGHT_USER = 20
MIN_LENGHT_USER = 4
ACCEPTED_CHAR = ['#','!']
ACCENT_MARK_MIN = ['á','é','í','ó','ú']
ACCENT_MARK_UPPER = ['Á','É','Í','Ó','Ú']
USER_INDEX = 0
PASSWORD_INDEX = 1
MAX_PLAYEBLE_USERS = 4

LOGIN_STATUS_OK = 1 # Usuario logueado exitosamente
LOGIN_STATUS_FAIL = 2 # El usuario o la contraseña son incorrectas
LOGIN_STATUS_LOGED = 3 # El usuario ya esta logueado
LOGIN_STATUS_MAX = 4 # Se alcanzo la maxima cantidad de jugadores

REGISTER_STATUS_OK = 1 # Se grabo en el archivo un nuevo usuario valido con una contraseña valida que antes no existia.
REGISTER_STATUS_USED = 2 # El usuario ya existia
REGISTER_STATUS_INVALID_USER = 3 # El usuario no es valido
REGISTER_STATUS_INVALID_PASS = 4 # La contraseña no es valida
users_list = []

def obtain_users_archive(route, mode):
    """
    recibe una ruta de un archivo y el modo de apertura, devuelve none si no existe
    """
    try:
        users_archive = open(route, mode)
    except:
        users_archive = None

    if debug_mode:
        print(users_archive)
    return users_archive

users_archive = obtain_users_archive('users.csv','r+')

def obtain_line(archive):
    """
    Recibe al archivo de obtain_users_archive y retorna las lineas que lo componen
    """
    line = archive.readline()
    if line == '':
        result = ARCHIVE_END
    else:
        result = tuple(line.strip().split(';')) 
        if debug_mode:
            print("el csv: ", result)
    return result

def check_user_exist(user):
    """
    recive un usuario y devuelve true si existe en el csv
    """
    line = obtain_line(users_archive)
    result = False
    i = 0
    if debug_mode:
        print("la lista: ", tuple)
    while not result and line != ARCHIVE_END:
        if user == line[USER_INDEX]:
            result = True
        line = obtain_line(users_archive)    
    users_archive.seek(0)
    return result

def create_valid_password(password):
    """ 
    recibe una clave y devuelve true si es valida y false si no cumple las caracteristicas
    """
    result = False
    lenght = len(password)
    upper_count = min_count = num_count = valid_char_count = invalid_char_count = spaces_count = i = 0
    while lenght <= MAX_LENGHT_PASS and lenght >= MIN_LENGHT_PASS and invalid_char_count == spaces_count == 0 and i <= lenght-1:
        if password[i] == ' ':
            spaces_count += 1
        elif not password[i].isalpha() and not password[i].isnumeric() and password[i] not in ACCEPTED_CHAR and password[i] not in ACCENT_MARK_MIN and password[i] not in ACCENT_MARK_UPPER:
            invalid_char_count += 1
        elif password[i] in ACCEPTED_CHAR:
            valid_char_count += 1
        elif password[i].isnumeric():
            num_count += 1
        elif password[i].isupper() or password[i] in ACCENT_MARK_UPPER:
            upper_count += 1
        elif password[i].islower() or password[i] in ACCENT_MARK_MIN:
            min_count += 1
        i += 1
    if upper_count >= 1 and min_count >= 1 and num_count >= 1 and valid_char_count >= 1 and invalid_char_count == spaces_count == 0:
        result = True
    return result

def create_valid_user(user):
    """ 
    recibe un usuario y devuelve verdadero si el usuario es valido y no existe en el csv
    """
    result = False
    lenght = len(user)
    invalid_count = i = 0
    while lenght >= MIN_LENGHT_USER and lenght <= MAX_LENGHT_USER  and invalid_count == 0 and i <= lenght-1:
        if not user[i].isalpha() and not user[i].isnumeric() and user[i] != '-' and user[i] not in ACCENT_MARK_MIN and user[i] not in ACCENT_MARK_UPPER:
            invalid_count +=1
        i += 1
    if invalid_count == 0 and lenght >= MIN_LENGHT_USER and lenght <= MAX_LENGHT_USER:
        result= True    
    return result

def check_user_pass(tuple):
    """
    recibe una tupla de valores (usuario, contraseña) y retorna True si son correctas y coinciden, false de lo contrario
    """
    line = obtain_line(users_archive)
    result = False
    if debug_mode: i = 0
    if debug_mode:
        print("la lista: ", tuple)
    while not result and line != ARCHIVE_END:
        if debug_mode:
            print(f"la linea {i}: {line} ")
        if tuple == line:
            result = True
        line = obtain_line(users_archive)
        if debug_mode: i+=1
    users_archive.seek(0)
    return result



def register_user_pass(tuple):
    """
    Recibe una tupla de valores (usuario, contraseña), valida que el usuario ingresado sea valido, 
    que no exista, y que la contraseña sea valida. Retorna el register status correspondiente.
    REGISTER_STATUS_OK           = Se grabo en el archivo un nuevo usuario valido con una contraseña valida que antes no existia.
    REGISTER_STATUS_USED         = El usuario ya existia
    REGISTER_STATUS_INVALID_USER = El usuario no es valido
    REGISTER_STATUS_INVALID_PASS = La contraseña no es valida
    """    
    if create_valid_user(tuple[USER_INDEX]) and not check_user_exist(tuple[USER_INDEX]) and create_valid_password(tuple[PASSWORD_INDEX]):
        users_archive_a = obtain_users_archive('users.csv','a')
        if debug_mode:print("esta es la tupla ", tuple) 
        line = ';'.join(tuple) + '\n'
        users_archive_a.write(line)
        result = REGISTER_STATUS_OK  
    elif check_user_exist(tuple[USER_INDEX]):
        result = REGISTER_STATUS_USED
    elif not create_valid_user(tuple[USER_INDEX]):
        result = REGISTER_STATUS_INVALID_USER
    elif not create_valid_password(tuple[PASSWORD_INDEX]):
        result = REGISTER_STATUS_INVALID_PASS
    return result

def login_users(tuple):
    """
    Recibe la tupla de usuarios y devuelve el estado:
    LOGIN_STATUS_OK    = Usuario logueado exitosamente
    LOGIN_STATUS_FAIL  =  El usuario o la contraseña son incorrectas
    LOGIN_STATUS_LOGED = El usuario ya esta logueado
    LOGIN_STATUS_MAX   =  Se alcanzo la maxima cantidad de jugadores
    """
    result = 0
    validate_tuple = check_user_pass(tuple)
    if validate_tuple and tuple[USER_INDEX] not in users_list:
        result = LOGIN_STATUS_OK 
        users_list.append(tuple[USER_INDEX])
    elif not check_user_pass(tuple):
        result = LOGIN_STATUS_FAIL
    elif tuple[USER_INDEX] in users_list:
        result = LOGIN_STATUS_LOGED
    elif len(users_list) == MAX_PLAYEBLE_USERS:
        result = LOGIN_STATUS_MAX
    return result

def play_button():
    """
    toma a los jugadores logueados
    """
    #command = lambda: [root.destroy(), users_archive.close(), random.shuffle(users)]
    
#if debug_mode:
    #print(check_user_exist('emilio'))
    #print(check_user_exist('emil'))
    #print(create_valid_user('emilio'))
    #print(create_valid_user('emilio-ontivero'))
    #print(create_valid_user('emilio-ontivero1'))
    #print(create_valid_user('emilio-ontivero@'))
    #print(create_valid_user('emi'))
    #print(create_valid_user('esteusuarioesdemasiadolargoparaquelafunciondetrue'))
    #print(check_user_pass(('emilio', 'ontiveros')))
    #print(check_user_pass(('jorge1', 'pruebaconpassincorrecta')))
    #print(register_user_pass(('cenii','bocayoteamo')))
    #print(register_user_pass(('valentino-ceniceros','Valido1#')))

#print(register_user_pass(('emilio','Valido1#')))#devolvera 1
#print(register_user_pass(('lucas-aldonate','Valido1!')))#devolvera 1
#print(register_user_pass(('emilio','Valido1!')))#devolvera 2
#print(register_user_pass(('emilio0147@','Valido1#')))#devolvera 3
#print(register_user_pass(('emilio-ontiveros','Valido1@')))#devolvera 4

#def main():
 #   login = check_user_pass()
  #  registe = register_user_pass()
#main()

