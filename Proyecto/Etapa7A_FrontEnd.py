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

# Otros
bd_generic = 0

def create_GUI(current_menu=MENU_VALUE_MAIN_MENU):
    """ Crea un GUI (Game User Interface). Sino se le pasa ningun parametro asume que es el main menu"""

    # -----------------------------------------------------------------------------------------------
    # ROOT ------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    """ El root contiene los frames. Cada frame es una seccion donde ingresaremos elementos tales como labels y botones"""
    root = Tk()                                       # Creamos la raiz
    root.title ("El rosco")                           # Le damos titulo a la ventana
    root.iconbitmap("Decodificado.ico")               # Determinamos el icono que utilizara la ventana

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
    # FRAMES --------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # Se crearan 4 frames para el GUI:
    # Frame 0: Se va a usar para titulos y logo
    my_frame_0 = Frame(my_main_frame)                   # Creamos un frame
    my_frame_0.grid(row=0,column=0)                     # Seteamos las configuraciones de posicion. 

    # Frame 1: Se va a usar para usuario y contraseña
    my_frame = Frame(my_main_frame)                     # Creamos un frame
    my_frame.grid(row=1,column=0)                       # Seteamos las configuraciones de posicion. 

    # Frame 2: Se usa para colocar el boton de creacion de usuario o la grilla de usuarios logeados
    my_frame2=Frame(my_main_frame)
    my_frame2.grid(row=2,column=0)
    my_frame2.config(height=200,width=200, padx=padding, pady=padding, bd=bd_generic, relief="groove")
        
    # Frame 3: Se usa para las cosas que van abajo de todo centradas (La firma por ejemplo)
    my_frame3=Frame(my_main_frame)
    my_frame3.grid(row=9,column=0)
    my_frame3.config(height=200,width=200, padx=padding, pady=padding, relief="groove")
    
    # ---------------------------------------------------------------------------------------------
    # FRAME 0 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    if current_menu == MENU_VALUE_MAIN_MENU: 
        imagen_rosco=PhotoImage(file="Rosco.png")
        title_Label = Label(my_frame_0,image=imagen_rosco)
        info_text = StringVar()
        info_text.set("TIP: Ingrese el usuario")
        label_of_info_text = Label(my_frame_0,textvariable=info_text).grid(row=1,column=0) 
    else: 
        title_Label = Label(my_frame_0,text="El Rosco", font=("Times New roman",22,"bold"), fg='PURPLE')
    title_Label.grid(row=0,column=0)
        
    # ---------------------------------------------------------------------------------------------
    # FRAME 1 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # Los inputs deben usar un string var para extraerlos con facilidad.
    user_input  = StringVar(my_frame)
    pass1_input = StringVar(my_frame)
    pass2_input = StringVar(my_frame)

    COLUMNA_NOMBRE_DE_CAMPO = 0
    COLUMNA_CAMPOS_A_LLENAR = 1
    FILA_USER = 2
    FILA_PASS = 3
    FILA_PASS_VERIFICATION = 4

    Label(my_frame,text="Jugador").grid(row=2,column=COLUMNA_NOMBRE_DE_CAMPO,sticky="w") 
    player_name_entry = Entry(my_frame, text=user_input).grid(row=FILA_USER,column=COLUMNA_CAMPOS_A_LLENAR,sticky="w") 

    Label(my_frame,text="Contraseña").grid(row=3,column=COLUMNA_NOMBRE_DE_CAMPO,sticky="w") 
    player_password_entry  = Entry(my_frame, text=pass1_input,show="*").grid(row=FILA_PASS,column=COLUMNA_CAMPOS_A_LLENAR,sticky="w") 

    if current_menu == MENU_VALUE_USER_CREATION:  # Menu de creacion de usuario
        # Frame 1
        Label(my_frame,text="Verifique contraseña").grid(row=FILA_PASS_VERIFICATION,column=COLUMNA_NOMBRE_DE_CAMPO,sticky="w") 
        player_password_verification_entry  = Entry(my_frame, text=pass2_input, show = "*").grid(row=FILA_PASS_VERIFICATION,column=COLUMNA_CAMPOS_A_LLENAR,sticky="w") 

        # Frame 2
        create_user_button  = Button (my_frame2, text="Crear usuario", command=lambda:create_new_user(user_input.get(),pass1_input.get(),pass2_input.get())).grid(row=8,column=0)

    elif current_menu == MENU_VALUE_MAIN_MENU:     # Menu de inicio
        # Frame 2 - Estoy usando una grilla, en la cual agrego los elementos.
        user_font       = ("Times New roman",10,"bold")
        user_name_font  = ("Arial",10,"italic")

        player1 = Label(my_frame2,text="Jugador 1:", font=user_font, fg='RED').grid(row=1,column=0,sticky="w") 
        player2 = Label(my_frame2,text="Jugador 2:", font=user_font, fg='BLUE').grid(row=2,column=0,sticky="w") 
        player3 = Label(my_frame2,text="Jugador 3:", font=user_font, fg='ORANGE').grid(row=3,column=0,sticky="w") 
        player4 = Label(my_frame2,text="Jugador 4:", font=user_font, fg='GREEN').grid(row=4,column=0,sticky="w") 
        
        player1_name = StringVar()
        player1_name.set("Disponible")
        player2_name = StringVar()
        player2_name.set("Disponible")
        player3_name = StringVar()
        player3_name.set("Disponible")
        player4_name = StringVar()
        player4_name.set("Disponible")

        player1_label = Label(my_frame2,textvariable=player1_name, font=user_name_font, fg='RED').grid(row=1,column=1,sticky="w") 
        player2_label = Label(my_frame2,textvariable=player2_name, font=user_name_font, fg='BLUE').grid(row=2,column=1,sticky="w") 
        player3_label = Label(my_frame2,textvariable=player3_name, font=user_name_font, fg='ORANGE').grid(row=3,column=1,sticky="w") 
        player4_label = Label(my_frame2,textvariable=player4_name, font=user_name_font, fg='GREEN').grid(row=4,column=1,sticky="w") 

        play_button = Button (my_frame2, text="Jugar!", command=lambda: play_game()).grid(row=9,column=0,columnspan=2)
        # -----------------------------
        # Botones ---------------------
        # -----------------------------
        user_grid=(player1_name,player2_name,player3_name,player4_name)
        login_button              = Button (my_frame, text="Ingresar", command=lambda:login_with_user(info_text, user_input.get(),pass1_input.get(),user_grid)).grid(row=8,column=0) 
        open_user_creation_button = Button (my_frame, text="Crear usuario nuevo", command=lambda: create_new_user_GUI()).grid(row=8,column=1)
        
    # ---------------------------------------------------------------------------------------------
    # FRAME FINAL -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    if current_menu == MENU_VALUE_MAIN_MENU: 
        Label(my_frame3,text="Creado por el equipo", font=("Times New roman",10,"bold italic")).grid(row=2,column=0,sticky="w") 
        imagen_equipo=PhotoImage(file="Decodificado titulo.png")
        team_Label = Label(my_frame3,image=imagen_equipo)
        team_Label.grid(row=3,column=0)
    else:
        Label(my_frame3,text="Creado por decodificado", font=("Times New roman",8,"bold italic")).grid(row=2,column=0,sticky="w") 
        
    def play_game():
        if len(Etapa7B_Backend.users_list)>0:
            Etapa7B_Backend.users_archive.close()
            root.destroy()
            Etapa9.play_new_rosco(Etapa7B_Backend.users_list)
        else: show_pop_up("Ingrese al menos un jugador")
    
    # -----------------------------
    # LOOP ------------------------
    # -----------------------------
    # IMPORTANTE: Generamos un bucle que se utilizar para las representaciones graficas. El main loop debe ir siempre ultimo.
    root.mainloop()

def create_new_user_GUI():
    """Crea una gui de creacion de usuario"""
    create_GUI(MENU_VALUE_USER_CREATION)
    
def create_new_user (user_value="",pass_value="",pass_v_value=""):
    """Envia los parametros necesarios para crear un usuario"""
    if debug_mode: print("Usuario:",user_value,"Password:",pass_value,"|",pass_v_value)

    # Verifica que se cumplan las condiciones basicas para enviar la tupla usuario clave
    if user_value=="": show_pop_up("Usuario vacio")
    elif pass_v_value=="": show_pop_up("Contraseña vacia")
    elif pass_v_value != pass_value: show_pop_up("Las contraseñas no coinciden")
    else:
        if debug_mode: print("enviando tupla usuario clave")
        tuple=(user_value,pass_value)

        # Envia los datos, retorna un estado y muestra un mensaje al usuario.
        status = Etapa7B_Backend.register_user_pass(tuple)
        print("Status:",status)
        if status == Etapa7B_Backend.REGISTER_STATUS_OK:
            show_pop_up("Usuario creado con exito")
        if status == Etapa7B_Backend.REGISTER_STATUS_USED:
            show_pop_up("Usuario ya existente, intente de nuevo")
        if status == Etapa7B_Backend.REGISTER_STATUS_INVALID_USER:
            show_pop_up("Usuario invalido, el usuario debe:\n  - Tener una longitud entre 4 y 20 caracteres\n  - Estar formado solo por letras, numeros y el guion medio")
        if status == Etapa7B_Backend.REGISTER_STATUS_INVALID_PASS:
            show_pop_up("Contraseña invalida, la contrasenia debe:\n  - Tener una longitud entre 6 y 12 caracteres\n  - Contener caracteres alfanumericos, a excepcion de letras acentuadas y los caracteres '#','!'\n- Debe contener una letra mayuscula, una minuscula, un numero y alguno de los siguientes caracteres: '#' '!'")

def show_pop_up(pop_up_text):
    messagebox.showinfo(title=None, message=pop_up_text)
    pass

def login_with_user(info_text,user,password,user_grid):
    if debug_mode: (print("Se hizo click en login"))
    if user=="": show_pop_up("Usuario vacio")
    elif password=="": show_pop_up("Contraseña vacia")
    elif len(Etapa7B_Backend.users_list)>=4: show_pop_up("Se alcanzo el maximo de jugadores")
    else:
        logged_user_tuple = (user,password)
        resultado_del_login = Etapa7B_Backend.login_users(logged_user_tuple)
        
        if resultado_del_login == Etapa7B_Backend.LOGIN_STATUS_OK:
            info_text.set("Se loggeo el jugador.")
            show_pop_up("Se loggeo el jugador")
            cantidad_de_jugadores = len(Etapa7B_Backend.users_list)
            if debug_mode: print("La cantidad de jugadores es de",len(Etapa7B_Backend.users_list))
            user_grid[cantidad_de_jugadores-1].set(user)

        elif resultado_del_login == Etapa7B_Backend.LOGIN_STATUS_LOGED:
            show_pop_up("Jugador ya logueado")
        elif resultado_del_login == Etapa7B_Backend.LOGIN_STATUS_MAX:
            show_pop_up("Se alcanzo el maximo de jugadores")
        elif resultado_del_login == Etapa7B_Backend.LOGIN_STATUS_FAIL:
            show_pop_up("El usuario o la contraseña son incorrectas")
            
def main():
    create_GUI()
