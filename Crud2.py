from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector

#esto conecta con la base de datos del xampp
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="escuela"
    )
except mysql.connector.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()

# Crear la tabla de alumnos si no existe
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT, email VARCHAR(255))")

# Función para leer todos los alumnos de la base de datos
def leer_alumnosDB():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM alumnos")
    return cursor.fetchall()

# Función para agregar un nuevo alumno a la base de datos
def agregar_alumnoDB(nombre, edad, email):
    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, edad, email) VALUES (%s, %s, %s)", (nombre, edad, email))
        db.commit()
    except mysql.connector.Error as error:
        messagebox.showerror("Error al agregar el alumno", f"No se pudo agregar el alumno: {error}")
    finally:
        cursor.close()

# Función para actualizar un alumno existente en la base de datos
def actualizar_alumnoDB(id, nombre, edad, email):
    iid = int(id)
    cursor = db.cursor()
    print("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    cursor.execute("UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE id = %s", (nombre, edad, email, iid))
    db.commit()

# Función para eliminar un alumno existente de la base de datos
def eliminar_alumnoDB(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    db.commit()

# Función para mostrar una lista de todos los alumnos
def mostrar_alumnos():
    # Limpiar la tabla
    for widget in tabla_alumnos.winfo_children():
        widget.destroy()

    # Obtener todos los alumnos
    alumnos = leer_alumnosDB()

    # Mostrar los alumnos en la tabla
    for i, alumno in enumerate(alumnos):
        id = alumno[0]
        nombre = alumno[1]
        edad = alumno[2]   
        email = alumno[3]

        Label(tabla_alumnos, text=id).grid(row=i, column=0)
        Label(tabla_alumnos, text=nombre).grid(row=i, column=1)
        Label(tabla_alumnos, text=edad).grid(row=i, column=2)
        Label(tabla_alumnos, text=email).grid(row=i, column=3)

def agregar_alumno():
    # Obtener los datos del nuevo alumno
    nombre = entrada_nombre.get()  
    edad = entrada_edad.get()
    email = entrada_email.get()

    # Validar que los campos no estén vacíos
    if not nombre or not edad or not email:
        messagebox.showerror("Error al agregar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Agregar el nuevo alumno
    agregar_alumnoDB(nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()

# Función para actualizar un alumno existente
def actualizar_alumno():
    # Obtener los datos del alumno a actualizar
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    email = entrada_email.get()
    id = entrada_id.get()

    # Validar que los campos no estén vacíos
    if not id or not nombre or not edad or not email:
        messagebox.showerror("Error al actualizar el alumno", "Por favor ingrese todos los datos del alumno")
        return

    # Actualizar el alumno
    actualizar_alumnoDB(id, nombre, edad, email)

    # Limpiar los campos de entrada
    entrada_id.delete(0, END)
    entrada_nombre.delete(0, END)
    entrada_edad.delete(0, END)
    entrada_email.delete(0, END)

    # Mostrar la lista actualizada de alumnos
    mostrar_alumnos()

# Función para eliminar un alumno existente
def eliminar_alumno():
    # Obtener el ID del alumno a eliminar
    id = entrada_id.get()

    # Validar que se haya ingresado un ID
    if not id:
        messagebox.showerror("Error al eliminar el alumno", "Por favor ingrese el ID del alumno a eliminar")
        return

    # Preguntar al usuario si está seguro de eliminar el alumno
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este alumno?")

    if confirmar:   
        # Eliminar el alumno
        eliminar_alumnoDB(id)

        # Limpiar los campos de entrada
        entrada_id.delete(0, END)
        entrada_nombre.delete(0, END)
        entrada_edad.delete(0, END)
        entrada_email.delete(0, END)

        # Mostrar la lista actualizada de alumnos
        mostrar_alumnos()

def compro():
    edadint1 = edad1
    edadint2 = int(edadint1)
    band=True
    ventana4 = tk.Tk()
    ventana4.configure(bg="paleturquoise")
    ventana4.configure(padx=80)
    ventana4.configure(pady=100)
    ventana4.title("¡Casi listo!")
    if edadint2 < 12:
         messagebox.showerror("Edad no permitida","Es necesario tener mas de 12 años")
    elif band==True:
        ventana4.destroy
        ventanajaja.destroy

def siguiente():
    ventana5 = tk.Tk()
    ventana5.configure(bg="paleturquoise")
    ventana5.configure(padx=100)
    ventana5.configure(pady=150)
    ventana5.title("Confirmacion")
    tk.Label(ventana5, text=" Si esta seguro de que los datos ingresados sean correctos presione finalizar, de lo contrario presione regresar  ", bg="beige",
          fg="black", width="100", height="1", font=("Bahnschrift", 12)).pack()
    tk.Label(ventana5, text="     ", bg="paleturquoise",
          fg="black", width="100", height="1", font=("Bahnschrift", 8)).pack()
    tk.Label(ventana5, text="     ", bg="paleturquoise",
          fg="black", width="100", height="1", font=("Bahnschrift", 8)).pack()
    tk.Label(ventana5, text="     ", bg="paleturquoise",
          fg="black", width="100", height="1", font=("Bahnschrift", 8)).pack()
    tk.Button(ventana5, text=" Finalizar ",bg="beige", command=lambda:[ventana5.destroy,ventanajaja.destroy]).pack(padx=5, pady=5)
    tk.Button(ventana5, text="Regresar",bg="beige", command=ventana5.destroy).pack(padx=5, pady=5)  
    
def Crear_Cuenta():
    ventana2 = Tk()
    ventana2.configure(bg="paleturquoise")
    ventana2.configure(padx=80)
    ventana2.configure(pady=100)
    ventana2.title("Creación de la cuenta")
    #                    ID
    #Label(ventana2, text="Id:", bg="lightcyan").grid(row=0, column=0, padx=5, pady=5)
    #entrada_id = Entry(ventana2)
    #entrada_id.grid(row=0, column=1, padx=5, pady=5)
    #                    NOMBRE
    Label(ventana2, text="Nombre:", bg="lightcyan").grid(row=1, column=0, padx=5, pady=5)
    entrada_nombre9 = Entry(ventana2)
    entrada_nombre9.grid(row=1, column=1, padx=5, pady=5)
    #                    EDAD
    Label(ventana2, text="Edad:", bg="lightcyan").grid(row=2, column=0, padx=5, pady=5)
    entrada_edad9 = Entry(ventana2)
    entrada_edad9.grid(row=2, column=1, padx=5, pady=5)
    #                    CORREO
    Label(ventana2, text="Email:", bg="lightcyan").grid(row=3, column=0, padx=5, pady=5)
    entrada_email9 = Entry(ventana2)
    entrada_email9.grid(row=3, column=1, padx=5, pady=5)
    #                    CONTRASEÑA
    Label(ventana2, text="Contraseña:", bg="lightcyan").grid(row=4, column=0, padx=5, pady=5)
    entrada_contra9 = Entry(ventana2)
    entrada_contra9.grid(row=4, column=1, padx=5, pady=5)

    tk.Button(ventana2, text="Siguiente",bg="beige", command=siguiente).grid(row=5, column=1, padx=5, pady=5)
    tk.Button(ventana2, text="Regresar",bg="beige", command=ventana2.destroy).grid(row=6, column=1, padx=5, pady=5) 

    #global Id
    #Id = entrada_id
    global name
    name = entrada_nombre9
    global edad1
    edad1 = entrada_edad9
    global email1
    email1 = entrada_email9
    global contra
    contra = entrada_contra9
    global ventanajaja
    ventanajaja = ventana2

def Inicio_Sesion():
    def valid():
        name4 = str(name)
        contra4 = str(contra)
        name3 = str(name2)
        contra3 = str(contra2)
        if name3 != name4 :
            messagebox.showerror("Error al verificar los datos", "Alguno de los datos no es correcto")
        else :
            ventana13 = tk.Tk()
            ventana13.configure(bg="paleturquoise")
            ventana13.configure(padx=150)
            ventana13.configure(pady=100)
            ventana13.title("Filtro")
            tK =tk.Label(ventana13, text=""" Inicio de sesion exitoso, presione "continuar" para modificar su equipo """, bg="lightcyan",
                fg="black", width="80", height="1", font=("Bahnschrift", 8)).pack()
            iniciar_sesion = tk.Button(ventana13, text="Continuar",command=ventana_final)
            iniciar_sesion.pack(padx=20, pady=20)
            


    ventana3 = tk.Tk()
    ventana3.configure(bg="paleturquoise")
    ventana3.configure(padx=100)
    ventana3.configure(pady=150)
    ventana3.title("Inicio de Sesión")
    #tk.Label(ventana3, text="Ingrese su nombre", bg="navajo white",fg="black", width="50", height="2", font=("Bahnschrift", 12)).pack()
    Label(ventana3, text="Nombre:", bg="lightcyan").grid(row=1, column=0, padx=5, pady=5)
    entrada_nombre10 = Entry(ventana3)
    entrada_nombre10.grid(row=1, column=1, padx=5, pady=5)
    Label(ventana3, text="Contraseña:", bg="lightcyan").grid(row=2, column=0, padx=5, pady=5)
    entrada_contra10 = Entry(ventana3)
    entrada_contra10.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(ventana3, text="Siguiente",bg="beige", command=valid).grid(row=5, column=1, padx=5, pady=5)
    
    global name2
    name2 = entrada_nombre10

    global contra2
    contra2 = entrada_contra10

def ventana_final():
    ventana = Tk()
    ventana.configure(bg="beige")
    ventana.configure(padx=80)
    ventana.configure(pady=50)
    ventana.title("Practica1_CRUD") 
    # Crear los campos de entrada para los datos del alumno
    Label(ventana, text="Id:").grid(row=0, column=0, padx=5, pady=5)
    entrada_idx = Entry(ventana)
    entrada_idx.grid(row=0, column=1, padx=5, pady=5)

    Label(ventana, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
    entrada_nombrex = Entry(ventana)
    entrada_nombrex.grid(row=1, column=1, padx=5, pady=5)

    Label(ventana, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
    entrada_edadx = Entry(ventana)
    entrada_edadx.grid(row=2, column=1, padx=5, pady=5)

    Label(ventana, text="Email:").grid(row=3, column=0, padx=5, pady=5)
    entrada_emailx = Entry(ventana)
    entrada_emailx.grid(row=3, column=1, padx=5, pady=5)

    # Crear los botones para agregar, actualizar y eliminar alumnos
    Button(ventana,bg="beige", text="Agregar Jugador", command=agregar_alumno).grid(row=0, column=2, padx=5, pady=5)
    Button(ventana, text="Actualizar Jugador", command=actualizar_alumno).grid(row=1, column=2, padx=5, pady=5)
    Button(ventana, text="Eliminar Jugador", command=eliminar_alumno).grid(row=2, column=2, padx=5, pady=5)

    # Crear la tabla para mostrar los alumnos
    tabla_alumnosx = Frame(ventana)
    tabla_alumnosx.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    Label(tabla_alumnosx, text="ID").grid(row=0, column=0)
    Label(tabla_alumnosx, text="Nombre").grid(row=0, column=1)
    Label(tabla_alumnosx, text="Edad").grid(row=0, column=2)
    Label(tabla_alumnosx, text="Email").grid(row=0, column=3)

    global tabla_alumnos
    tabla_alumnos = tabla_alumnosx
    global entrada_nombre
    entrada_nombre = entrada_nombrex
    global entrada_id
    entrada_id = entrada_idx
    global entrada_edad
    entrada_edad = entrada_edadx
    global entrada_email
    entrada_email = entrada_emailx

    # Mostrar la lista de alumnos en la tabla
    mostrar_alumnos()

    # Iniciar el loop de la ventana
    ventana.mainloop()

#genera la ventana principal
ventana11 = tk.Tk()
ventana11.configure(bg="paleturquoise")
ventana11.configure(padx=80)
ventana11.configure(pady=100)
ventana11.title("Practica1_CRUD")
tK =tk.Label(ventana11, text=" Bienvenido a GameWorld ", bg="lightcyan",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
#crear_cuenta = Tk = Button(ventana, text="Crear Cuenta",bg="beige", command=Inicio)
#crear_cuenta.pack(padx=20, pady=20)
Iniciar_Sesion = tk.Button(ventana11, text="Crear Cuenta",bg="beige", command=Crear_Cuenta)
Iniciar_Sesion.pack(padx=20, pady=20)
Iniciar_Sesion =  tk.Button(ventana11, text="Iniciar Sesión",bg="beige", command=Inicio_Sesion)
Iniciar_Sesion.pack(padx=20, pady=20)
crear_cuenta = tk.Button(ventana11, text="Cerrar",bg="beige", command=ventana11.quit)
crear_cuenta.pack(padx=20, pady=20)
ventana11.mainloop()