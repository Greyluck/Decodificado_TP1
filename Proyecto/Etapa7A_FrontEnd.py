"""Etapa 7: Interfaz grafica - Front End"""
# El responsable de esta etapa es Emilio Ontiveros.
# El responsable de su revision es Valentino Ceniceros.

# -----------------------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox  
import Etapa7B_Backend
import Etapa9


# Menus
MENU_VALUE_MAIN_MENU = 0                #   0) Menu principal 
MENU_VALUE_USER_CREATION = 1            #   1) Creacion de usuario
MENU_VALUE_PLAYING_GAME = 2             #   2) Jugando

# Debug Mode
debug_mode = True 

def create_GUI(current_menu=MENU_VALUE_MAIN_MENU):
    """ Crea un GUI (Game User Interface). Sino se le pasa ningun parametro asume que es el main menu"""

    # -----------------------------------------------------------------------------------------------
    # Variables y constantes
    # -----------------------------------------------------------------------------------------------
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
    #  - Una forma de agregar un label rapidamente es: Label(my_frame,text="Texto de prueba").place(x=50,y=50)
    #  - Otra forma es: nombreDelLabel = Label(contenedor,opciones) y luego ir agregando los valores necesarios 
    myLabel = Label(my_frame_0,text="El Rosco", font=("Times New roman",22,"bold"), fg='PURPLE')
    myLabel.grid(row=0,column=0)

    # Texto de informacion # TODO: Por algun motivo solo aparece en la pantalla principal... incluso si borro el IF. Revisar
    if current_menu==MENU_VALUE_MAIN_MENU:
        info_text = StringVar()
        info_text.set("TIP: Ingrese el usuario")
        label_of_info_text = Label(my_frame_0,textvariable=info_text).grid(row=1,column=0) 

    # ---------------------------------------------------------------------------------------------
    # FRAME 1 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    my_frame = Frame(my_main_frame)                     # Creamos un frame
    my_frame.grid(row=1,column=0)                       # Seteamos las configuraciones de posicion. 
    # Para la posicion de las cosas se pueden usar PACK, PLACE o GRID. En teoria no habria que mesclarlas
    #   - myLabel.grid(row=0,column=0)  <-- Utiliza una tabla o grilla de columnas y filas
    #   - myLabel.place(x=1,y=1)        <-- El label se adatara al contenedor
    #   - myLabel.pack()                <-- El contenedor se adaptara al texto
    #       - my_frame.pack(anchor="n")  <- De esta forma se alinea por PX
    #       - Side define la alineacion clasica. Anchor usa cardinales "N,W,S,E"
    #       - my_frame.pack(fill="center", expand=True) Se utiliza para que el frame se adapte al tamaño en pantalla automaticamente al expandirla

    # Seteamos las configuraciones tales como tamaño y background (Para el frame)
    my_frame.config(height=200,width=200)            # El tamaño del frame
    my_frame.config(padx=padding,pady=padding)       # El padding son los "margenes", estan definidos arriba
    my_frame.config(bg="#f7f2e1")                    # Color de fondo
    my_frame.config(cursor="hand2")                  # Tipo de cursor que usa sobre el frame
    my_frame.config(bd=bd_generic)                            # Tamaño/grosor del borde
    my_frame.config(relief="groove")                 # El tipo de borde

    # -----------------------------
    # GRID ------------------------
    # -----------------------------
    """ Estoy usando una grilla, en la cual agrego los elementos."""

    # Los inputs deben usar un string var para extraerlos con facilidad.
    user_input = StringVar(my_frame)
    pass1_input = StringVar(my_frame)
    pass2_input = StringVar(my_frame)


    Label(my_frame,text="Jugador").grid(row=2,column=0,sticky="w") 
    player_name_entry = Entry(my_frame, text=user_input).grid(row=2,column=1,sticky="w") 

    Label(my_frame,text="Contraseña").grid(row=3,column=0,sticky="w") 
    player_password_entry  = Entry(my_frame, text=pass1_input,show="*").grid(row=3,column=1,sticky="w") 

    if current_menu == MENU_VALUE_USER_CREATION:  # Menu de creacion de usuario
        Label(my_frame,text="Verifique contraseña").grid(row=4,column=0,sticky="w") 
        player_password_verification_entry  = Entry(my_frame, text=pass2_input).grid(row=4,column=1,sticky="w") 
        # Creo un segundo frame para centrar el boton.
        my_frame2=Frame(my_main_frame)
        my_frame2.grid(row=2,column=0)
        my_frame2.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=bd_generic, relief="groove")
        create_user_button  = Button (my_frame2, text="Crear usuario", command=lambda:create_new_user(user_input.get(),pass1_input.get(),pass2_input.get())).grid(row=8,column=0)

    elif current_menu == MENU_VALUE_MAIN_MENU:     # Menu de inicio
        # -----------------------------
        # Botones ---------------------
        # -----------------------------
        login_button              = Button (my_frame, text="Ingresar", command=lambda:login_with_user(info_text, (user_input.get(),pass1_input.get()) )).grid(row=8,column=0) 
        open_user_creation_button = Button (my_frame, text="Crear usuario nuevo", command=lambda: create_new_user_GUI()).grid(row=8,column=1)
        
        # ---------------------------------------------------------------------------------------------
        # FRAME 3 -------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------
        # El frame 3 esta se usa para los users
        my_frame3=Frame(my_main_frame)
        my_frame3.grid(row=3,column=0)
        my_frame3.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=2, relief="groove")
    
        # -----------------------------
        # GRID ------------------------
        # -----------------------------
        # Estoy usando una grilla, en la cual agrego los elementos.
        user_font       = ("Times New roman",10,"bold")
        user_Name_font  = ("Arial",10,"italic")

        player1 = Label(my_frame3,text="Jugador 1:", font=user_font, fg='RED').grid(row=1,column=0,sticky="w") 
        player2 = Label(my_frame3,text="Jugador 2:", font=user_font, fg='BLUE').grid(row=2,column=0,sticky="w") 
        player3 = Label(my_frame3,text="Jugador 3:", font=user_font, fg='ORANGE').grid(row=3,column=0,sticky="w") 
        player4 = Label(my_frame3,text="Jugador 4:", font=user_font, fg='GREEN').grid(row=4,column=0,sticky="w") 

        player1_Name = Label(my_frame3,text="Disponible", font=user_Name_font, fg='RED').grid(row=1,column=1,sticky="w") 
        player2_Name = Label(my_frame3,text="Disponible", font=user_Name_font, fg='BLUE').grid(row=2,column=1,sticky="w") 
        player3_Name = Label(my_frame3,text="Disponible", font=user_Name_font, fg='ORANGE').grid(row=3,column=1,sticky="w") 
        player4_Name = Label(my_frame3,text="Disponible", font=user_Name_font, fg='GREEN').grid(row=4,column=1,sticky="w") 

    # ---------------------------------------------------------------------------------------------
    # FRAME FINAL -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # Se usa para las cosas que van abajo de todo centradas (La firma por ejemplo)
    my_frame4=Frame(my_main_frame)
    my_frame4.grid(row=9,column=0)
    my_frame4.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", relief="groove")

    def play_game():
        Etapa7B_Backend.users_archive.close()
        root.destroy()
        Etapa9.play_new_rosco(Etapa7B_Backend.users_list)
    play_button = Button (my_frame4, text="Jugar!", command=lambda: play_game()).grid(row=0,column=0)

    Label(my_frame4,text="Creado por Decodificado", font=("Times New roman",10,"bold italic")).grid(row=1,column=0,sticky="w") 

    # -----------------------------
    # LOOP ------------------------
    # -----------------------------
    # IMPORTANTE: Generamos un bucle que se utilizar para las representaciones graficas. El main loop debe ir siempre ultimo.
    root.mainloop()

def create_new_user_GUI():
    """ Llama a la funcion de crear un GUI, pero para creacion de usuario"""
    create_GUI(MENU_VALUE_USER_CREATION)
    
def create_new_user (user_value="",pass_value="",pass_v_value=""):
    """Envia los parametros necesarios para crear un usuario"""
    if debug_mode: print("Usuario:",user_value,"Password:",pass_value,"|",pass_v_value)
    if pass_v_value == pass_value:
        tuple=(user_value,pass_value)

        # Envia los datos, y retorna un estado.
        status = Etapa7B_Backend.register_user_pass(tuple)
        if status == Etapa7B_Backend.REGISTER_STATUS_OK:
            show_pop_up("Usuario creado con exito")
            messagebox.Message(master=None)
        if status == Etapa7B_Backend.REGISTER_STATUS_USED:
            show_pop_up("Usuario ya existente, intente de nuevo")
        if status == Etapa7B_Backend.REGISTER_STATUS_INVALID_USER:
            show_pop_up("Usuario invalido, intente de nuevo")
        if status == Etapa7B_Backend.REGISTER_STATUS_INVALID_PASS:
            show_pop_up("Password invalido, intente de nuevo")

# TODO: Es un copy paste de lo anterior. Idealmente no se va a abrir un pop up, sino cambiar un texto.
def show_pop_up(pop_up_text):
    root = Tk()                                       # Creamos la raiz
    root.title ("El rosco")                         # Le damos titulo a la ventana
    root.iconbitmap("Talisman.ico")                 # Determinamos el icono que utilizara la ventana
    root.resizable(False,False)                      # Impedimos la modificacion del tamaño de la ventana
    my_main_frame = Frame(root)
    my_main_frame.grid(row=0,column=0)
    my_frame_0 = Frame(my_main_frame)                   # Creamos un frame
    my_frame_0.grid(row=0,column=0)                     # Seteamos las configuraciones de posicion. 
    Label(my_frame_0,text=(pop_up_text)).grid(row=0,column=0)
    Label(my_frame_0,text=("(Puede cerrar la ventana)")).grid(row=1,column=0)
    

def login_with_user(info_text,logged_user_tuple):
    if (Etapa7B_Backend.login_users(logged_user_tuple)) == 1: # Devuelve el codigo de OK
        info_text.set("Se loggeo el jugador")

def main():
    create_GUI()
