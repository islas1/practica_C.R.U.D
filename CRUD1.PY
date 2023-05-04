from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


#esto conecta con la base de datos del xampp
try :
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="Cuenta"
    )
except pymysql.connect.Error as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
    exit()

def Inicio_Sesion():
    ventana3 = tk.Tk()
    ventana3.configure(bg="paleturquoise")
    ventana3.configure(padx=80)
    ventana3.configure(pady=100)
    ventana3.title("Practica1_CRUD")

def Crear_Cuenta():
    db = pymysql.connect(
    host="localhost",
    user="root",
    password="",    
    db="Cuenta"
    )

   #base = "INSERT INTO login (ID, Nombre, Correo, Contraseña) VALUES ('{0}', '{1}', '{2}', '{3}')".format(    
        #name.get(), namemasc.get(), calle.get(), age.get(), serv.get(), raza.get())

    fcursor = db.cursor()
    consulta = "SELECT * FROM login WHERE Nombre = "
    fcursor.execute(consulta)
    datos = fcursor.fetchall()
    print(datos)

    #fcursor.execute(base)
    db.commit()
    db.close

    ventana2 = Tk()
    ventana2.configure(bg="paleturquoise")
    ventana2.configure(padx=80)
    ventana2.configure(pady=100)
    ventana2.title("Practica1_CRUD")
    #                    ID
    Label(ventana2, text="Id:", bg="lightcyan").grid(row=0, column=0, padx=5, pady=5)
    entrada_id = Entry(ventana2)
    entrada_id.grid(row=0, column=1, padx=5, pady=5)
    #                    NOMBRE
    Label(ventana2, text="Nombre:", bg="lightcyan").grid(row=1, column=0, padx=5, pady=5)
    entrada_nombre = Entry(ventana2)
    entrada_nombre.grid(row=1, column=1, padx=5, pady=5)
    #                    EDAD
    Label(ventana2, text="Edad:", bg="lightcyan").grid(row=2, column=0, padx=5, pady=5)
    entrada_edad = Entry(ventana2)
    entrada_edad.grid(row=2, column=1, padx=5, pady=5)
    #                    CORREO
    Label(ventana2, text="Email:", bg="lightcyan").grid(row=3, column=0, padx=5, pady=5)
    entrada_email = Entry(ventana2)
    entrada_email.grid(row=3, column=1, padx=5, pady=5)
    #                    CONTRASEÑA
    Label(ventana2, text="Contraseña:", bg="lightcyan").grid(row=4, column=0, padx=5, pady=5)
    entrada_contra = Entry(ventana2)
    entrada_contra.grid(row=4, column=1, padx=5, pady=5)

#genera la ventana principal
ventana = tk.Tk()
ventana.configure(bg="paleturquoise")
ventana.configure(padx=80)
ventana.configure(pady=100)
ventana.title("Practica1_CRUD")
tK =tk.Label(ventana, text=" Bienvenido a GameWorld ", bg="lightcyan",
          fg="black", width="20", height="1", font=("Bahnschrift", 15)).pack()
#crear_cuenta = Tk = Button(ventana, text="Crear Cuenta",bg="beige", command=Inicio)
#crear_cuenta.pack(padx=20, pady=20)
Iniciar_Sesion = tk.Button(ventana, text="Crear Cuenta",bg="beige", command=Crear_Cuenta)
Iniciar_Sesion.pack(padx=20, pady=20)
Iniciar_Sesion =  tk.Button(ventana, text="Iniciar Sesión",bg="beige", command=Inicio_Sesion)
Iniciar_Sesion.pack(padx=20, pady=20)
crear_cuenta = tk.Button(ventana, text="Cerrar",bg="beige", command=ventana.quit)
crear_cuenta.pack(padx=20, pady=20)
ventana.mainloop()