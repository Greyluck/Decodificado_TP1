debug_mode =False
ARCHIVE_END = ['','']

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


def obtain_lines(archive):
    """
    Recibe al archivo de obtain_users_archive y retorna las lineas que lo componen
    """
    lines = archive.readlines()
    if lines == '':
        result = ARCHIVE_END
    else:
        result = [tuple(line.strip().split(',')) for line in lines]
        if debug_mode:
            print("el csv: ", result)
    return result




def check_user_pass(tuple):
    """
    recibe una tupla de valores (usuario, contraseña) y retorna True si estan en el csv, false de lo contrario
    """
    users_archive = obtain_users_archive('users.csv','r')
    lines = obtain_lines(users_archive)
    result = False
    i = 0
    if debug_mode:
        print("la lista: ", tuple)
    while not result and i <= len(lines)-1:
        line = lines[i]
        if debug_mode:
            print(f"la linea {i}: {line} ")
        if tuple == line:
            result = True
        i+=1
    return result
def register_user_pass(tuple):
    """
    recibe una tupla de valores (usuario, contraseña) y las escribe en el csv, si la tupla no estaba en en csv la agrega y devuelve true caso contrario devuelve false
    """
    result = False
    try:
        if not check_user_pass(tuple):
            users_archive = obtain_users_archive('users.csv','a')
            if debug_mode:print("esta es la tupla ", tuple) 
            line = ','.join(tuple) + '\n'
            users_archive.write(line)
            result = True 
    except:
        result = False
        if debug_mode:
            print("la terna usuario clave ya existe en el csv")
    return result
if debug_mode:
    print(check_user_pass(('emilio', 'pepe')))
    print(check_user_pass(('jorge1', 'pruebaconpassincorrecta')))
    #print(register_user_pass(('cenii','bocayoteamo')))
    #print(register_user_pass(('lucas','riber')))
    
def main():
    print(check_user_pass(('cenii','bocayoteamo')))
    print(check_user_pass(('cenii','pruebaconpassincorrecta')))
    print(register_user_pass(('tomi','starwars no es fantasia')))
#main()
