"""Etapa 7: Interfaz grafica - Front End"""
# El responsable de esta etapa es Emilio Ontiveros.
# El responsable de su revision es Valentino Ceniceros.

# -----------------------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------------------
from tkinter import *  

# Menus
MENU_VALUE_MAIN_MENU = 0                #   0) Menu principal 
MENU_VALUE_USER_CREATION = 1            #   1) Creacion de usuario
MENU_VALUE_PLAYING_GAME = 2             #   2) Jugando

def create_GUI(current_menu=MENU_VALUE_MAIN_MENU):
    """ Crea un GUI (Game User Interface). Sino se le pasa ningun parametro asume que es el main menu"""

    # -----------------------------------------------------------------------------------------------
    # Variables y constantes
    # -----------------------------------------------------------------------------------------------
    # Debug Mode
    debug_mode = True 

    # Padding generico que sera usado para todo.
    padding = 2

    # Colores
    COLOR_CREMA  = "#e0d3a6"
    COLOR_MARRON = "#473722"

    # Root
    bg_root = COLOR_MARRON   #Borde exterior
    padding = 5

    # Otros
    bd_generic = 0

    # -----------------------------------------------------------------------------------------------
    # ROOT ------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    """ El root contiene los frames. Cada frame es una seccion donde ingresaremos elementos tales como labels y botones"""
    root = Tk()                                       # Creamos la raiz
    root.title ("El rosco")                         # Le damos titulo a la ventana
    root.iconbitmap("Talisman.ico")                 # Determinamos el icono que utilizara la ventana
    # -----------------------------
    # Definiciones de tamaño
    # -----------------------------
    #root.geometry("500x400")                        # Defninimos el tamaño de la ventana. 
    #root.maxsize(width=600,height=600)              # Defninimos el tamaño maximo de la ventana. 
    #root.minsize(width=500,height=0)                # Defninimos el tamaño minimo de la ventana. 
    root.resizable(False,False)                      # Impedimos la modificacion del tamaño de la ventana
    root.config(padx=padding,pady=padding)           # El padding son los "margenes", estan definidos arriba
    #NOTA: Si removemos el geometry y resizable es true, se adaptara al tamaño de su contenido

    # -----------------------------
    # Definiciones de formato
    # -----------------------------
    root.config(bg=COLOR_CREMA)                      # Seteamos las configuraciones de fondo
    root.config(bd=bd_generic)                       # Seteamos el borde
    root.config(bg=bg_root)                          # Seteamos el fondo del root
    root.config(relief="groove")                     # Seteamos el tipo de borde

    # -----------------------------
    # Main Frame ------------------
    # -----------------------------
    """ La idea de este frame es contener a todos los demas frames."""
    # Creo el main frame (que contendra un canvas)
    my_main_frame = Frame(root)
    my_main_frame.grid(row=0,column=0)

    # ---------------------------------------------------------------------------------------------
    # FRAME 0 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    """ Se va a usar para titulos y demas"""
    my_frame_0 = Frame(my_main_frame)                   # Creamos un frame
    my_frame_0.grid(row=0,column=0)                     # Seteamos las configuraciones de posicion. 

    # -----------------------------
    # LABEL -----------------------
    # -----------------------------
    # NOTA: 
    #  - Una forma de agregar un label rapidamente es: Label(myFrame,text="Texto de prueba").place(x=50,y=50)
    #  - Otra forma es: nombreDelLabel = Label(contenedor,opciones) y luego ir agregando los valores necesarios 
    myLabel = Label(my_frame_0,text="El Rosco", font=("Times New roman",22,"bold"), fg='PURPLE')
    myLabel.grid(row=0,column=0)

    # ---------------------------------------------------------------------------------------------
    # FRAME 1 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    myFrame = Frame(my_main_frame)                     # Creamos un frame
    myFrame.grid(row=1,column=0)                       # Seteamos las configuraciones de posicion. 
    # Para la posicion de las cosas se pueden usar PACK, PLACE o GRID. En teoria no habria que mesclarlas
    #   - myLabel.grid(row=0,column=0)  <-- Utiliza una tabla o grilla de columnas y filas
    #   - myLabel.place(x=1,y=1)        <-- El label se adatara al contenedor
    #   - myLabel.pack()                <-- El contenedor se adaptara al texto
    #       - myFrame.pack(anchor="n")  <- De esta forma se alinea por PX
    #       - Side define la alineacion clasica. Anchor usa cardinales "N,W,S,E"
    #       - myFrame.pack(fill="center", expand=True) Se utiliza para que el frame se adapte al tamaño en pantalla automaticamente al expandirla

    # Seteamos las configuraciones tales como tamaño y background (Para el frame)
    myFrame.config(height=200,width=200)            # El tamaño del frame
    myFrame.config(padx=padding,pady=padding)       # El padding son los "margenes", estan definidos arriba
    myFrame.config(bg="#f7f2e1")                    # Color de fondo
    myFrame.config(cursor="hand2")                  # Tipo de cursor que usa sobre el frame
    myFrame.config(bd=bd_generic)                            # Tamaño/grosor del borde
    myFrame.config(relief="groove")                 # El tipo de borde

    # -----------------------------
    # GRID ------------------------
    # -----------------------------
    # Estoy usando una grilla, en la cual agrego los elementos.
    Label(myFrame,text="Jugador").grid(row=2,column=0,sticky="w") 
    Entry(myFrame).grid(row=2,column=1,sticky="w") 

    Label(myFrame,text="Contraseña").grid(row=3,column=0,sticky="w") 
    Entry(myFrame).grid(row=3,column=1,sticky="w") 

    if current_menu == MENU_VALUE_USER_CREATION:  # Menu de creacion de usuario
        Label(myFrame,text="Verifique contraseña").grid(row=4,column=0,sticky="w") 
        Entry(myFrame).grid(row=4,column=1,sticky="w") 
    
        # ---------------------------------------------------------------------------------------------
        # FRAME 2 -------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # El frame 2 esta centrado. Se usa para las cosas debajo de los campos  dobles.
        myFrame2=Frame(my_main_frame)
        myFrame2.grid(row=2,column=0)
        myFrame2.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=bd_generic, relief="groove")
        create_user_button  = Button (myFrame2, text="Crear usuario", command=create_new_user).grid(row=8,column=0)

    elif current_menu == MENU_VALUE_MAIN_MENU:     # Menu de inicio
        # ---------------------------------------------------------------------------------------------
        # FRAME 2 -------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # El frame 2 esta centrado. Se usa para las cosas debajo de los campos  dobles.
        myFrame2=Frame(my_main_frame)
        myFrame2.grid(row=2,column=0)
        myFrame2.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=bd_generic, relief="groove")
        
        # -----------------------------
        # Botones ---------------------
        # -----------------------------
        # Creamos una variable que almacenara el valor que luego cambiara.
        textocambiante = StringVar()

        # En este caso le asigno un valor especifico que quiero que muestre por defecto
        textocambiante.set("Ingrese el usuario")

        # Creo el lable y entry que contendran los valores que cambiaran.
        LabelQueCambiaAlPresionarElbutton= Label(myFrame2,textvariable=textocambiante).grid(row=6,column=0) 

        login_button              = Button (myFrame, text="Ingresar", command=lambda:login_with_user(textocambiante)).grid(row=8,column=0) 
        # TODO borrar el texto cambiante sino es necesario
        open_user_creation_button = Button (myFrame, text="Crear usuario nuevo", command=lambda: create_new_user_GUI()).grid(row=8,column=1)

        # ---------------------------------------------------------------------------------------------
        # FRAME 3 -------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # El frame 3 esta se usa para los users
        myFrame3=Frame(my_main_frame)
        myFrame3.grid(row=3,column=0)
        myFrame3.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=2, relief="groove")

        # -----------------------------
        # GRID ------------------------
        # -----------------------------
        # Estoy usando una grilla, en la cual agrego los elementos.
        user_font       = ("Times New roman",10,"bold")
        user_Name_font  = ("Arial",10,"italic")

        player1 = Label(myFrame3,text="Jugador 1:", font=user_font, fg='RED').grid(row=1,column=0,sticky="w") 
        player2 = Label(myFrame3,text="Jugador 2:", font=user_font, fg='BLUE').grid(row=2,column=0,sticky="w") 
        player3 = Label(myFrame3,text="Jugador 3:", font=user_font, fg='ORANGE').grid(row=3,column=0,sticky="w") 
        player4 = Label(myFrame3,text="Jugador 4:", font=user_font, fg='GREEN').grid(row=4,column=0,sticky="w") 

        player1_Name = Label(myFrame3,text="Disponible", font=user_Name_font, fg='RED').grid(row=1,column=1,sticky="w") 
        player2_Name = Label(myFrame3,text="Disponible", font=user_Name_font, fg='BLUE').grid(row=2,column=1,sticky="w") 
        player3_Name = Label(myFrame3,text="Disponible", font=user_Name_font, fg='ORANGE').grid(row=3,column=1,sticky="w") 
        player4_Name = Label(myFrame3,text="Disponible", font=user_Name_font, fg='GREEN').grid(row=4,column=1,sticky="w") 

    # ---------------------------------------------------------------------------------------------
    # FRAME FINAL -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # Se usa para las cosas que van abajo de todo centradas (La firma por ejemplo)
    myFrame4=Frame(my_main_frame)
    myFrame4.grid(row=9,column=0)
    myFrame4.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", relief="groove")
    Label(myFrame4,text="Creado por Decodificado", font=("Times New roman",10,"bold italic")).grid(row=1,column=0,sticky="w") 

    # -----------------------------
    # LOOP ------------------------
    # -----------------------------
    # IMPORTANTE: Generamos un bucle que se utilizar para las representaciones graficas. El main loop debe ir siempre ultimo.
    root.mainloop()

def create_new_user_GUI():
    """ Llama a la funcion de crear un GUI, pero para creacion de usuario"""
    create_GUI(MENU_VALUE_USER_CREATION)
    
def create_new_user ():
    """Envia los parametros necesarios para crear un usuario"""
    pass

def login_with_user(textocambiante):
    textocambiante.set("Se loggeo")

def main():
    create_GUI()

main()