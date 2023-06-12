import Etapa10 
#----------------------------------------PALABRAS y DEFINICIONES----------------------------------------------#
def return_words_and_definition():
    """
    Toma los dos archivos txt de palabras y definicines y retorna un diccionario clave:valor
    """  
    palabras = open("palabras.txt", encoding="utf8")
    line = palabras.readline().rstrip("\n")

    definiciones = open("definiciones.txt", encoding="utf8")
    line_definition = definiciones.readline().rstrip("\n")

    LEN_MIN_WORDS = Etapa10.game_config["MIN_WORD_LENGHT"][Etapa10.VALUE]

    dicc_words_secret = {} 

    while line != "" and line_definition != "":

        if len(line) >= LEN_MIN_WORDS and line.isalpha():

            dicc_words_secret[line] = line_definition
            line= palabras.readline().rstrip("\n")
            line_definition = definiciones.readline().rstrip("\n")
        
        else:

            line= palabras.readline().rstrip("\n")
            line_definition = definiciones.readline().rstrip("\n")

    palabras.close()
    definiciones.close()
    
    return dicc_words_secret
#-----------------------------------------DEVUELVE ARCHIVO CSV-----------------------------------------------#

def return_file_csv(dicc_out_word_definition):
    """
    Toma el diccionario de palabras secretas y lo guarda en un archivo csv
    """
    
    file = open("Diccionario.CSV","w", encoding="utf8")
    sorted_dicc = sorted(dicc_out_word_definition.items(), key=lambda x: x[0])
                    
    for word in sorted_dicc:

        file.write(f"{word[0]},{word[1]}\n")
    file.close()
#------------------------------------------------MAIN---------------------------------------------------------#

def main():
    """
    El programa recorre dos archivos de tipo 'txt', los filtra a travez de condiciones y devuelve un diccionario
    con estas palabras y definiciones guardados en un archivo .CSV
    """
    dicc_out_word_definition= return_words_and_definition()
    print(return_file_csv(dicc_out_word_definition))

#main()