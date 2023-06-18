"""Etapa 7: Interfaz grafica - Front End"""
# El responsable de esta etapa es Emilio Ontiveros.
# El responsable de su revision es Valentino Ceniceros.

# -----------------------------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------------------------
from tkinter import *   

def create_GUI():
    # -----------------------------------------------------------------------------------------------
    # Variables y constantes
    # -----------------------------------------------------------------------------------------------
    # Debug Mode
    debugMode=True 

    # Padding generico que sera usado para todo.
    padding = 2

    # Colores
    colorCrema="#e0d3a6"
    colorMarron="#473722"

    # Root
    bgRoot=colorMarron   #Borde exterior
    padding = 5

    # Otros
    bd_generic = 7

    # -----------------------------------------------------------------------------------------------
    # ROOT ------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
    """ El root contiene los frames. Cada frame es una seccion donde ingresaremos elementos tales como labels y botones"""
    root=Tk()                                       # Creamos la raiz
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
    root.config(bg=colorCrema)                      # Seteamos las configuraciones de fondo
    root.config(bd=bd_generic)                               # Seteamos el borde
    root.config(bg=bgRoot)                          # Seteamos el fondo del root
    root.config(relief="groove")                    # Seteamos el tipo de borde

    # -----------------------------
    # Main Frame ------------------
    # -----------------------------
    """ La idea de este frame es contener a todos los demas frames."""
    # Creo el main frame (que contendra un canvas)
    myMainFrame=Frame(root)
    myMainFrame.grid(row=0,column=0)

    # ---------------------------------------------------------------------------------------------
    # FRAME 0 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    """ Se va a usar para titulos y demas"""
    myFrame0=Frame(myMainFrame)                       # Creamos un frame
    myFrame0.grid(row=0,column=0)                     # Seteamos las configuraciones de posicion. 

    # -----------------------------
    # LABEL -----------------------
    # -----------------------------
    # NOTA: 
    #  - Una forma de agregar un label rapidamente es: Label(myFrame,text="Texto de prueba").place(x=50,y=50)
    #  - Otra forma es: nombreDelLabel = Label(contenedor,opciones) y luego ir agregando los valores necesarios 
    myLabel = Label(myFrame0,text="Rosco")
    myLabel.grid(row=0,column=0)

    # ---------------------------------------------------------------------------------------------
    # FRAME 1 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    myFrame=Frame(myMainFrame)                       # Creamos un frame
    myFrame.grid(row=1,column=0)                     # Seteamos las configuraciones de posicion. 
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
    if debugMode == True: Entry(myFrame,bg="Red").grid(row=2,column=1,sticky="w") 

    Label(myFrame,text="Contraseña").grid(row=3,column=0,sticky="w") 
    if debugMode == True: Entry(myFrame,bg="Blue").grid(row=3,column=1,sticky="w") 

    # ---------------------------------------------------------------------------------------------
    # FRAME 2 -------------------------------------------------------------------------------------
    # ---------------------------------------------------------------------------------------------
    # Usando lo aplicado en el frame anterior cree este para separar la ejecucion de botones
    myFrame2=Frame(myMainFrame)
    myFrame2.grid(row=2,column=0)
    myFrame2.config(height=200,width=200, padx=padding, pady=padding, bg="#f7f2e1", bd=bd_generic, relief="groove")

    # -----------------------------
    # Botones ---------------------
    # -----------------------------
    # Creamos una variable que almacenara el valor que luego cambiara.
    textocambiante = StringVar()

    # En este caso le asigno un valor especifico que quiero que muestre por defecto
    textocambiante.set("Texto no modificado")

    # Creo el lable y entry que contendran los valores que cambiaran.
    LabelQueCambiaAlPresionarElBoton = Label(myFrame2,textvariable=textocambiante).grid(row=6,column=0) 

    def funcionDelBoton():
        textocambiante.set("Texto cambiado")

    boton = Button (myFrame2, text="enviar", command=funcionDelBoton).grid(row=8,column=0)

    # -----------------------------
    # LOOP ------------------------
    # -----------------------------
    # IMPORTANTE: Generamos un bucle que se utilizar para las representaciones graficas. El main loop debe ir siempre ultimo.
    root.mainloop()

def main():
    create_GUI()

main()