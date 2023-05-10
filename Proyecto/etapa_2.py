from datos import obtener_lista_definiciones

def return_short_words(main_list):
    """
    Recibe la lista principal y devuleve un diccionario con palabras de un largo determinado
    """

    out_dicc={}
    MIN_LETERS=5
    INDEX_NAME=0
    INDEX_DEFINITION=1

    for word in main_list:
        if len(word[INDEX_NAME])>=MIN_LETERS:

            out_dicc[word[INDEX_NAME]]=word[INDEX_DEFINITION]
    return out_dicc

def return_quantity(short_word_dicc):
    """
    Devuleve la cantidad de palabras que inician con una letra en especifico y la cantidad total de 
    palabras en el diccioanrio
    """
    lista_abecedario=["a","b","c", "d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    INDEX_NAME=0
    out_dicc_just_letter={}
    lista_de_palabras=[]

    for word in short_word_dicc:
        lista_de_palabras.append(word[INDEX_NAME])

    total_words_in_dicc=0

    for letra in lista_abecedario:
        out_dicc_just_letter[letra]= lista_de_palabras.count(letra)
        total_words_in_dicc += out_dicc_just_letter[letra]
        
    return out_dicc_just_letter, total_words_in_dicc

def main():
    """
    Recibe una lista que contiene las palabras candidatas
    y sus definiciones, las analiza y retorna un out_dicc con palabras especificas. Para, posteriormente
    haberiguar cuantas palabras inician.
    """
    main_list= obtener_lista_definiciones()
    short_word_dicc= return_short_words(main_list)
    quantity, total= return_quantity(short_word_dicc) #return_quantity devuelve cantidad y total
    # print("Los numeros de palabras por letra son: ", quantity, "y el total es: ", total)
    
main()







