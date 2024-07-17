import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Conexion import *
from Alumno import *
from Profesor import *
from Administrador import *
from Login import *
from Grupo import *
from Materia import *
from Calificacion import *
import re
import datetime


def iniciar_sesion(usuario_entry, contrasena_entry, ventanaInicioSesion):
    global usuarioGeneral
    
    usuarioGeneral = usuario_entry.get()
    contrasena = contrasena_entry.get()
    tipoUsuario = CLogin.login(usuarioGeneral, contrasena)

    # Verificar las credenciales del alumno
    if tipoUsuario == "alumno": #usuario_prueba@alumno.paet.mx, clave
        messagebox.showinfo("Inicio de sesión", "¡Bienvenido Alumno!")
        ventanaInicioSesion.destroy()
        mostrar_ventanaPrincipal()
    # Verificar las credenciales del administrador
    elif tipoUsuario == "admin": #administrador_prueba@administrador.paet.mx, clave
        messagebox.showinfo("Inicio de sesión", "¡Bienvenido Administrador!")
        ventanaInicioSesion.destroy()
        ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.resizable(False, False)  # Bloquear la opción de maximizar
        mostrar_ventanaMenu(ventanaPrincipal)
    # Verificar las credenciales del profesor
    elif tipoUsuario == "prof": #administrador_prueba@administrador.paet.mx, clave
        messagebox.showinfo("Inicio de sesión", "¡Bienvenido Profesor!")
        ventanaInicioSesion.destroy()
        ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.resizable(False, False)
        mostrar_ventanaPrincipal_profesor(ventanaPrincipal)
    else:
        messagebox.showerror("Inicio de sesión", "Credenciales incorrectas")
        usuario_entry.delete(0, 'end')
        contrasena_entry.delete(0, 'end')

def mostrar_inicio_sesion():
    # Crear la ventanaInicioSesion principal
    ventanaInicioSesion = tk.Tk()
    ventanaInicioSesion.resizable(False, False)  # Bloquear la opción de maximizar

    ventanaInicioSesion.title("Inicio de sesión")

    # Centrar la ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaInicioSesion.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaInicioSesion.winfo_screenheight()

    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 500) / 2)

    # Utiliza el tamaño inicial y la posición calculada
    ventanaInicioSesion.geometry(f"600x400+{x_pos}+{y_pos}")

    canvas = tk.Canvas(ventanaInicioSesion, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas.pack()
    canvas.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas.create_rectangle(0, 90, ancho_ventanaInicioSesion, 60, fill=color_hex1, outline="")
    canvas.create_rectangle(0, altura_ventanaInicioSesion, ancho_ventanaInicioSesion, 360, fill=color_hex1, outline="")

    # Crear los widgets y configurar eventos
    texto_inicio_sesion, usuario_entry, contrasena_entry, olvide_contrasena_label, preparatoria_autonoma_de_toluca_label, usuario_label, contrasenia_label, iniciar_sesion_due, registrarse_due, pie_pagina, iniciar_sesion_button = crear_widgets(ventanaInicioSesion)
    configurar_eventos(olvide_contrasena_label, registrarse_due)
    colocar_widgets(texto_inicio_sesion, iniciar_sesion_due, registrarse_due, usuario_entry, contrasena_entry, iniciar_sesion_button, olvide_contrasena_label, preparatoria_autonoma_de_toluca_label, usuario_label, contrasenia_label, pie_pagina)
    
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaInicioSesion, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    # Iniciar el bucle de la aplicación
    ventanaInicioSesion.mainloop()

def mostrar_ventanaMenu(ventanaPrincipal):
    
    ventanaPrincipal.title("Menú Principal")
    imagen_perfil = Image.open("Imagenes\\icono1_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)

    imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)


    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    canvas2.place(x=0, y=0)

    #Botones
    boton = tk.Button(canvas2, text="Perfil", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPerfil_admin(ventanaPrincipal))
    canvas2.create_window(-61, 90, anchor="w", window=boton)
    boton2 = tk.Button(canvas2, text="Editar Alumn", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionAlumno(ventanaPrincipal))
    canvas2.create_window(-7, 120, anchor="w", window=boton2)
    boton3 = tk.Button(canvas2, text="Editar Profes", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionProfesor(ventanaPrincipal))
    canvas2.create_window(-7, 150, anchor="w", window=boton3)
    boton4 = tk.Button(canvas2, text="Editar Admin", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionAdmin(ventanaPrincipal))
    canvas2.create_window(-7, 180, anchor="w", window=boton4)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def mostrar_ventanaPrincipal():
    ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
    ventanaPrincipal.resizable(False, False)  # Bloquear la opción de maximizar
    ventanaPrincipal.title("Menú Principal")

    
    imagen_perfil = Image.open("Imagenes\\icono1.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)

    imagen_perfil2 = Image.open("Imagenes\\icono2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil2
    icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

    imagen_perfil3 = Image.open("Imagenes\\icono3.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil3
    icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

    imagen_perfil4 = Image.open("Imagenes\\icono4.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)


    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    
    #Botones
    boton = tk.Button(canvas2, text="Perfil", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPerfil(ventanaPrincipal))
    canvas2.create_window(-61, 90, anchor="w", window=boton)
    boton2 = tk.Button(canvas2, text="Grupos", width=158, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaTrayectoria(ventanaPrincipal))
    canvas2.create_window(-45, 120, anchor="w", window=boton2)
    boton3 = tk.Button(canvas2, text="Calificaciones", width=114, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaCalificaciones(ventanaPrincipal))
    canvas2.create_window(0, 150, anchor="w", window=boton3)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def mostrar_ventanaModificacionAlumno(ventanaPrincipal):
    
    def mostrar_ventanaAltas_alumno(ventanaPrincipal):

        global entry_nombre
        global entry_CURP
        global entry_FechaNac
        global entry_numCuenta
        global genero_seleccionado
        global nacionalidad_seleccionada
        global contrasena_alumno

        ventanaPrincipal.title("Altas de alumnos")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Nuevo alumno", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.49, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.56, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.63, anchor="w")
        usuario_label6 = tk.Label(ventanaPrincipal, text="Contraseña del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label6.place(relx=0.3, rely=0.71, anchor="w")

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado = tk.StringVar(ventanaPrincipal)
        genero_seleccionado.set(opciones_genero[0])  # Seleccionar la primera opción por defecto

        opciones_nacionalidad = ["mexicana", "extranjera"]
        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre.place(relx=0.7, rely=0.35, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.415, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.485, anchor="w")
        entry_CURP = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP.place(relx=0.7, rely=0.56, anchor="w")
        entry_FechaNac = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac.place(relx=0.7, rely=0.63, anchor="w")
        contrasena_alumno = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        contrasena_alumno.place(relx=0.7, rely=0.71, anchor="w")
        
        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaBajas_alumno(ventanaPrincipal):

        ventanaPrincipal.title("Bajas de alumnos")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar alumno", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

        entry_numCuenta = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre.place(relx=0.7, rely=0.50, anchor="w")
        entry_CURP = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
        entry_CURP.place(relx=0.7, rely=0.57, anchor="w")
        
        def eliminar_alumno():
            try:
                numCuenta = entry_numCuenta.get()

                if not numCuenta or len(numCuenta) < 1:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_nombre.delete(0, 'end')
                    return
                
                # Si todos los datos son válidos, ingresar el alumno
                cursorRowCount = CAlumno.borrarAlumnoPorNumeroDeCuenta(numCuenta)

                if cursorRowCount == 0:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_numCuenta.delete(0, 'end')
                    return
                messagebox.showinfo("Info", "Alumno eliminado exitosamente")
                entry_numCuenta.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos en Bajas de alumnos {}".format(error))


        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
        
        
        ventanaPrincipal.mainloop()

    def mostrar_ventanaModificaciones_alumno(ventanaPrincipal):
        
        global entry_nombre
        global entry_CURP
        global entry_FechaNac
        global entry_numCuenta
        global genero_seleccionado
        global nacionalidad_seleccionada
        global entry_numCuenta

        ventanaPrincipal.title("Modificaciones de alumnos")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")
        
        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Modificación de información", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.43, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.505, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.64, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.71, anchor="w")
        

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado = tk.StringVar(ventanaPrincipal)
        genero_seleccionado.set(opciones_genero[0])  # Seleccionar la primera opción por defecto


        opciones_nacionalidad = ["mexicana", "extranjera"]

        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_numCuenta = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre.place(relx=0.7, rely=0.43, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.50, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.57, anchor="w")
        entry_CURP = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP.place(relx=0.7, rely=0.64, anchor="w")
        entry_FechaNac = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac.place(relx=0.7, rely=0.71, anchor="w")
        
        def validar_campos():
            if entry_numCuenta.get() and entry_nombre.get() and entry_CURP.get() and entry_FechaNac.get():
                boton_confirmarCambios.config(state="normal", bg=color_hex2)  # Habilitar el botón "Confirmar cambios" y establecer el color de fondo normal
            else:
                boton_confirmarCambios.config(state="disabled", bg="gray")  # Deshabilitar el botón "Confirmar cambios" y establecer el color de fondo en gris

        # Asociar la función validar_campos a cada campo de entrada para que se llame cada vez que se modifique un campo
        entry_numCuenta.bind("<KeyRelease>", lambda event: validar_campos())
        entry_nombre.bind("<KeyRelease>", lambda event: validar_campos())
        entry_CURP.bind("<KeyRelease>", lambda event: validar_campos())
        entry_FechaNac.bind("<KeyRelease>", lambda event: validar_campos())

        def aceptar_modificacion():
            num_cuenta = entry_numCuenta.get()  # Obtener el número de cuenta ingresado manualmente
            cursorRowCount = CAlumno.validacion_alumno(num_cuenta)
            alumnos = CAlumno.buscarAlumnoPorNumeroDeCuenta(num_cuenta)  # Buscar los alumnos por número de cuenta
            if alumnos and cursorRowCount != 0:
                # Solo tomamos el primer alumno encontrado para llenar los campos
                alumno = alumnos[0]
                llenar_campos_con_informacion_alumno(alumno)  # Llenar los campos con la información del alumno
            else:
                messagebox.showerror("Error", "No se encontró ningún alumno con ese número de cuenta")

        def llenar_campos_con_informacion_alumno(alumno):
            if alumno:
                nombre, genero, nacionalidad, CURP, fecha_nac = alumno
                entry_nombre.delete(0, 'end')
                entry_nombre.insert(0, nombre)
                genero_seleccionado.set(genero)
                nacionalidad_seleccionada.set(nacionalidad)
                entry_CURP.delete(0, 'end')
                entry_CURP.insert(0, CURP)
                entry_FechaNac.delete(0, 'end')
                entry_FechaNac.insert(0, fecha_nac)
                validar_campos()  # Verificar si todos los campos están completos después de llenarlos
            else:
                messagebox.showerror("Error", "No se encontró ningún alumno con ese número de cuenta")

        boton_buscarAlumno = tk.Button(ventanaPrincipal, text="Buscar Alumno", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=aceptar_modificacion)
        boton_buscarAlumno.place(relx=0.625, rely=0.82, anchor="center")

        boton_confirmarCambios = tk.Button(ventanaPrincipal, text="Confirmar cambios", width=47, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=actualizar_datos_de_base_de_datos, state="disabled", bg="gray")
        boton_confirmarCambios.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaConsultas_alumno(ventanaPrincipal):
        ventanaPrincipal.title("Consultas de alumnos")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los alumnos", padx=0, pady=1, bg="white")
        groupBox.place(relx=0.615, rely=0.58, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

        tree = ttk.Treeview(groupBox, columns=("Nombre", "Género", "Nacionalidad", "CURP", "Fecha Nac", "NC"), show='headings',height=5)
        tree.grid(row=0, column=0, sticky="nsew")

        # Configurar scrollbar horizontal
        scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=scroll_x.set)

        # Configurar scrollbar vertical
        scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=scroll_y.set)
        tree.configure(height=14)
        tree.column("#1", anchor="center", width=110)
        tree.heading("#1", text="Nombre")
        tree.column("#2", anchor="center", width=50)
        tree.heading("#2", text="Género")
        tree.column("#3", anchor="center", width=80)
        tree.heading("#3", text="Nacionalidad")
        tree.column("#4", anchor="center", width=70)
        tree.heading("#4", text="CURP")
        tree.column("#5", anchor="center", width=70)
        tree.heading("#5", text="Fecha Nac")
        tree.column("#6", anchor="center", width=60)
        tree.heading("#6", text="NC")

        for row in CAlumno.mostrarAlumno():
            tree.insert("","end", values=row)

        
        # Función para mostrar la información completa al hacer doble clic en una fila
        def mostrar_info_completa(event):
            item = tree.item(tree.selection())
            values = item['values']
            messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

        # Vincular evento de doble clic a la función mostrar_info_completa
        tree.bind("<Double-1>", mostrar_info_completa)

        ventanaPrincipal.mainloop()

    def pasar_datos_de_base_de_datos():
        global entry_nombre
        global entry_CURP
        global entry_FechaNac
        global entry_numCuenta
        global genero_seleccionado
        global nacionalidad_seleccionada
        global contrasena_alumno

        try:
            nombre = entry_nombre.get()
            genero = genero_seleccionado.get()
            nacionalidad = nacionalidad_seleccionada.get()
            curp = entry_CURP.get()
            fechaNac = entry_FechaNac.get()
            contra = contrasena_alumno.get() 
            print("Nombre: "+ entry_nombre.get())
            cursorID = CAlumno.login(contra)
            cursorCURPRowCount = CAlumno.validacion_curp(curp)
            patron = r"^[a-zA-ZÀ-ÿ']+([ \t]+[a-zA-ZÀ-ÿ']+)*$"

            if not re.search(patron, nombre):
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return

            if entry_nombre is None or len(entry_nombre.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac.delete(0, 'end')
                return

            if len(curp) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP.delete(0, 'end')
                return

            if cursorCURPRowCount == 1:
                messagebox.showerror("CURP", "¡Curp repetido!")
                entry_CURP.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CAlumno.ingresarAlumno(nombre, genero, nacionalidad, curp, fechaNac, cursorID)   
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre.delete(0, 'end')
            entry_CURP.delete(0, 'end')
            entry_FechaNac.delete(0, 'end')
            contrasena_alumno.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos {}".format(error))

    def actualizar_datos_de_base_de_datos():
        global entry_nombre
        global entry_CURP
        global entry_FechaNac
        global entry_numCuenta
        global genero_seleccionado
        global nacionalidad_seleccionada
        global entry_numCuenta

        try:
            nombre = entry_nombre.get()
            genero = genero_seleccionado.get()
            nacionalidad = nacionalidad_seleccionada.get()
            CURP = entry_CURP.get()
            fechaNac = entry_FechaNac.get()
            numCuenta = entry_numCuenta.get()
            print("Nombre: "+ entry_nombre.get())

            if entry_nombre is None or len(entry_nombre.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                entry_nombre.delete(0, 'end')
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac.delete(0, 'end')
                return

            if len(CURP) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CAlumno.actualizarAlumno(nombre, genero, nacionalidad, CURP, fechaNac, numCuenta)
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre.delete(0, 'end')
            entry_CURP.delete(0, 'end')
            entry_FechaNac.delete(0, 'end')
            entry_numCuenta.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos {}".format(error))


    #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
    ventanaPrincipal.title("Modificación de alumnos")
    
    imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)

    imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil2
    icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

    imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil3
    icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

    imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

    imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil6
    icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    canvas2.place(x=0, y=0)

    #Botones
    boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaMenu(ventanaPrincipal))
    canvas2.create_window(-26, 90, anchor="w", window=boton)
    boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_alumno(ventanaPrincipal))
    canvas2.create_window(-61, 120, anchor="w", window=boton2)
    boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_alumno(ventanaPrincipal))
    canvas2.create_window(-53, 150, anchor="w", window=boton3)
    boton4 = tk.Button(canvas2, text="Modificación", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificaciones_alumno(ventanaPrincipal))
    canvas2.create_window(-7, 180, anchor="w", window=boton4)
    boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_alumno(ventanaPrincipal))
    canvas2.create_window(-28, 210, anchor="w", window=boton6)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def mostrar_ventanaModificacionProfesor(ventanaPrincipal):
    
    def mostrar_ventanaAltas_profe(ventanaPrincipal):
        global entry_nombre_profe
        global entry_CURP_profe
        global entry_FechaNac_profe
        global entry_numCuenta_profe
        global genero_seleccionado_profe
        global nacionalidad_seleccionada_profe
        global contrasena_profesor

        ventanaPrincipal.title("Altas de profesores")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Nuevo profesor", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.49, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.56, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.63, anchor="w")
        usuario_label6 = tk.Label(ventanaPrincipal, text="Contraseña del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label6.place(relx=0.3, rely=0.71, anchor="w")

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado_profe = tk.StringVar(ventanaPrincipal)
        genero_seleccionado_profe.set(opciones_genero[0])  # Seleccionar la primera opción por defecto

        opciones_nacionalidad = ["mexicana", "extranjera"]
        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada_profe = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada_profe.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_nombre_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_profe.place(relx=0.7, rely=0.35, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado_profe, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.415, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada_profe, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.485, anchor="w")
        entry_CURP_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP_profe.place(relx=0.7, rely=0.56, anchor="w")
        entry_FechaNac_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac_profe.place(relx=0.7, rely=0.63, anchor="w")
        contrasena_profesor = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        contrasena_profesor.place(relx=0.7, rely=0.71, anchor="w")
        
        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaBajas_profe(ventanaPrincipal):

        ventanaPrincipal.title("Bajas de profesores")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar profesor", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

        entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_profe.place(relx=0.7, rely=0.50, anchor="w")
        entry_CURP_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
        entry_CURP_profe.place(relx=0.7, rely=0.57, anchor="w")
        
        def eliminar_alumno():
            try:
                numCuenta = entry_numCuenta_profe.get()

                if not numCuenta or len(numCuenta) < 1:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_nombre_profe.delete(0, 'end')
                    return
                
                # Si todos los datos son válidos, ingresar el alumno
                cursorRowCount = CProfesor.borrarProfePorNumeroDeCuenta(numCuenta)

                if cursorRowCount == 0:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_numCuenta_profe.delete(0, 'end')
                    return
                messagebox.showinfo("Info", "Profesor eliminado exitosamente")
                entry_numCuenta_profe.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos en Bajas de profesores {}".format(error))


        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
        
        
        ventanaPrincipal.mainloop()

    def mostrar_ventanaModificaciones_profe(ventanaPrincipal):
        
        global entry_nombre_profe
        global entry_CURP_profe
        global entry_FechaNac_profe
        global entry_numCuenta_profe
        global genero_seleccionado_profe
        global nacionalidad_seleccionada_profe
        global entry_numCuenta_profe

        ventanaPrincipal.title("Modificación de profesores")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")
        
        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Modificación de información", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.43, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.505, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.64, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del profesor: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.71, anchor="w")
        

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado_profe = tk.StringVar(ventanaPrincipal)
        genero_seleccionado_profe.set(opciones_genero[0])  # Seleccionar la primera opción por defecto


        opciones_nacionalidad = ["mexicana", "extranjera"]

        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada_profe = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada_profe.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_profe.place(relx=0.7, rely=0.43, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado_profe, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.50, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada_profe, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.57, anchor="w")
        entry_CURP_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP_profe.place(relx=0.7, rely=0.64, anchor="w")
        entry_FechaNac_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac_profe.place(relx=0.7, rely=0.71, anchor="w")
        
        def validar_campos():
            if entry_numCuenta_profe.get() and entry_nombre_profe.get() and entry_CURP_profe.get() and entry_FechaNac_profe.get():
                boton_confirmarCambios.config(state="normal", bg=color_hex2)  # Habilitar el botón "Confirmar cambios" y establecer el color de fondo normal
            else:
                boton_confirmarCambios.config(state="disabled", bg="gray")  # Deshabilitar el botón "Confirmar cambios" y establecer el color de fondo en gris

        # Asociar la función validar_campos a cada campo de entrada para que se llame cada vez que se modifique un campo
        entry_numCuenta_profe.bind("<KeyRelease>", lambda event: validar_campos())
        entry_nombre_profe.bind("<KeyRelease>", lambda event: validar_campos())
        entry_CURP_profe.bind("<KeyRelease>", lambda event: validar_campos())
        entry_FechaNac_profe.bind("<KeyRelease>", lambda event: validar_campos())

        def aceptar_modificacion():
            num_cuenta = entry_numCuenta_profe.get()  # Obtener el número de cuenta ingresado manualmente
            cursorRowCount = CProfesor.validacion_Profe(num_cuenta)
            alumnos = CProfesor.buscarProfePorNumeroDeCuenta(num_cuenta)  # Buscar los alumnos por número de cuenta
            if alumnos and cursorRowCount != 0:
                # Solo tomamos el primer alumno encontrado para llenar los campos
                alumno = alumnos[0]
                llenar_campos_con_informacion_alumno(alumno)  # Llenar los campos con la información del alumno
            else:
                messagebox.showerror("Error", "No se encontró ningún profesor con ese número de cuenta")

        def llenar_campos_con_informacion_alumno(alumno):
            if alumno:
                nombre, genero, nacionalidad, CURP, fecha_nac = alumno
                entry_nombre_profe.delete(0, 'end')
                entry_nombre_profe.insert(0, nombre)
                genero_seleccionado_profe.set(genero)
                nacionalidad_seleccionada_profe.set(nacionalidad)
                entry_CURP_profe.delete(0, 'end')
                entry_CURP_profe.insert(0, CURP)
                entry_FechaNac_profe.delete(0, 'end')
                entry_FechaNac_profe.insert(0, fecha_nac)
                validar_campos()  # Verificar si todos los campos están completos después de llenarlos
            else:
                messagebox.showerror("Error", "No se encontró ningún alumno con ese número de cuenta")

        boton_buscarAlumno = tk.Button(ventanaPrincipal, text="Buscar Profesor", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=aceptar_modificacion)
        boton_buscarAlumno.place(relx=0.625, rely=0.82, anchor="center")

        boton_confirmarCambios = tk.Button(ventanaPrincipal, text="Confirmar cambios", width=47, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=actualizar_datos_de_base_de_datos, state="disabled", bg="gray")
        boton_confirmarCambios.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaConsultas_profe(ventanaPrincipal):
        ventanaPrincipal.title("Consultas de profesores")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los profesores", padx=0, pady=1, bg="white")
        groupBox.place(relx=0.615, rely=0.58, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

        tree = ttk.Treeview(groupBox, columns=("Nombre", "Género", "Nacionalidad", "CURP", "Fecha Nac", "NC"), show='headings',height=5)
        tree.grid(row=0, column=0, sticky="nsew")

        # Configurar scrollbar horizontal
        scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=scroll_x.set)

        # Configurar scrollbar vertical
        scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=scroll_y.set)
        tree.configure(height=14)
        tree.column("#1", anchor="center", width=110)
        tree.heading("#1", text="Nombre")
        tree.column("#2", anchor="center", width=50)
        tree.heading("#2", text="Género")
        tree.column("#3", anchor="center", width=80)
        tree.heading("#3", text="Nacionalidad")
        tree.column("#4", anchor="center", width=70)
        tree.heading("#4", text="CURP")
        tree.column("#5", anchor="center", width=70)
        tree.heading("#5", text="Fecha Nac")
        tree.column("#6", anchor="center", width=60)
        tree.heading("#6", text="NC")

        for row in CProfesor.mostrarProfe():
            tree.insert("","end", values=row)

        
        # Función para mostrar la información completa al hacer doble clic en una fila
        def mostrar_info_completa(event):
            item = tree.item(tree.selection())
            values = item['values']
            messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

        # Vincular evento de doble clic a la función mostrar_info_completa
        tree.bind("<Double-1>", mostrar_info_completa)

        ventanaPrincipal.mainloop()

    def pasar_datos_de_base_de_datos():
        global entry_nombre_profe
        global entry_CURP_profe
        global entry_FechaNac_profe
        global entry_numCuenta_profe
        global genero_seleccionado_profe
        global nacionalidad_seleccionada_profe
        global contrasena_profesor

        try:
            nombre = entry_nombre_profe.get()
            genero = genero_seleccionado_profe.get()
            nacionalidad = nacionalidad_seleccionada_profe.get()
            curp = entry_CURP_profe.get()
            fechaNac = entry_FechaNac_profe.get()
            contra = contrasena_profesor.get()
            print("Nombre: "+ entry_nombre_profe.get())
            cursorID = CProfesor.login(contra)
            cursorCURPRowCount = CProfesor.validacion_curp(curp)
            patron = r"^[a-zA-ZÀ-ÿ']+([ \t]+[a-zA-ZÀ-ÿ']+)*$"

            if not re.search(patron, nombre):
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return


            if entry_nombre_profe is None or len(entry_nombre_profe.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac_profe.delete(0, 'end')
                return

            if len(curp) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP_profe.delete(0, 'end')
                return

            if cursorCURPRowCount == 1:
                messagebox.showerror("CURP", "¡Curp repetido!")
                entry_CURP_profe.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CProfesor.ingresarProfe(nombre, genero, nacionalidad, curp, fechaNac, cursorID)   
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre_profe.delete(0, 'end')
            entry_CURP_profe.delete(0, 'end')
            entry_FechaNac_profe.delete(0, 'end')
            contrasena_profesor.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del profesor en la función pasar_datos_de_base_de_datos {}".format(error))

    def actualizar_datos_de_base_de_datos():
        global entry_nombre_profe
        global entry_CURP_profe
        global entry_FechaNac_profe
        global entry_numCuenta_profe
        global genero_seleccionado_profe
        global nacionalidad_seleccionada_profe
        global entry_numCuenta_profe

        try:
            nombre = entry_nombre_profe.get()
            genero = genero_seleccionado_profe.get()
            nacionalidad = nacionalidad_seleccionada_profe.get()
            CURP = entry_CURP_profe.get()
            fechaNac = entry_FechaNac_profe.get()
            numCuenta = entry_numCuenta_profe.get()
            print("Nombre: "+ entry_nombre_profe.get())

            if entry_nombre_profe is None or len(entry_nombre_profe.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                entry_nombre_profe.delete(0, 'end')
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac_profe.delete(0, 'end')
                return

            if len(CURP) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP_profe.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CProfesor.actualizarProfe(nombre, genero, nacionalidad, CURP, fechaNac, numCuenta)
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre_profe.delete(0, 'end')
            entry_CURP_profe.delete(0, 'end')
            entry_FechaNac_profe.delete(0, 'end')
            entry_numCuenta_profe.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del profesor en la función pasar_datos_de_base_de_datos {}".format(error))

    #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
    ventanaPrincipal.title("Modificación de Profesores")
    
    imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)

    imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil2
    icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

    imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil3
    icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

    imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

    imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil6
    icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    canvas2.place(x=0, y=0)

    #Botones
    boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaMenu(ventanaPrincipal))
    canvas2.create_window(-26, 90, anchor="w", window=boton)
    boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_profe(ventanaPrincipal))
    canvas2.create_window(-61, 120, anchor="w", window=boton2)
    boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_profe(ventanaPrincipal))
    canvas2.create_window(-53, 150, anchor="w", window=boton3)
    boton4 = tk.Button(canvas2, text="Modificación", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificaciones_profe(ventanaPrincipal))
    canvas2.create_window(-7, 180, anchor="w", window=boton4)
    boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_profe(ventanaPrincipal))
    canvas2.create_window(-28, 210, anchor="w", window=boton6)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def mostrar_ventanaModificacionAdmin(ventanaPrincipal):

    def mostrar_ventanaAltas_admin(ventanaPrincipal):
        global entry_nombre_admin
        global entry_CURP_admin
        global entry_FechaNac_admin
        global entry_numCuenta_admin
        global genero_seleccionado_admin
        global nacionalidad_seleccionada_admin
        global contrasena_administrador

        ventanaPrincipal.title("Altas de adminstradores")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Nuevo administrador", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.49, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.56, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.63, anchor="w")
        usuario_label6 = tk.Label(ventanaPrincipal, text="Contraseña del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label6.place(relx=0.3, rely=0.71, anchor="w")

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado_admin = tk.StringVar(ventanaPrincipal)
        genero_seleccionado_admin.set(opciones_genero[0])  # Seleccionar la primera opción por defecto

        opciones_nacionalidad = ["mexicana", "extranjera"]
        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada_admin = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada_admin.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_nombre_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_admin.place(relx=0.7, rely=0.35, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado_admin, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.415, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada_admin, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.485, anchor="w")
        entry_CURP_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP_admin.place(relx=0.7, rely=0.56, anchor="w")
        entry_FechaNac_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac_admin.place(relx=0.7, rely=0.63, anchor="w")
        contrasena_administrador = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        contrasena_administrador.place(relx=0.7, rely=0.71, anchor="w")
        
        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaBajas_admin(ventanaPrincipal):

        ventanaPrincipal.title("Bajas de administradores")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar administrador", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

        entry_numCuenta_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta_admin.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_admin.place(relx=0.7, rely=0.50, anchor="w")
        entry_CURP_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
        entry_CURP_admin.place(relx=0.7, rely=0.57, anchor="w")
        
        def eliminar_alumno():
            try:
                numCuenta = entry_numCuenta_admin.get()

                if not numCuenta or len(numCuenta) < 1:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_nombre_admin.delete(0, 'end')
                    return
                
                # Si todos los datos son válidos, ingresar el alumno
                cursorRowCount = CAdmin.borrarAdminPorNumeroDeCuenta(numCuenta)

                if cursorRowCount == 0:
                    messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                    entry_numCuenta_admin.delete(0, 'end')
                    return
                messagebox.showinfo("Info", "Alumno eliminado exitosamente")
                entry_numCuenta_admin.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos en Bajas de alumnos {}".format(error))


        boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
        boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
        
        
        ventanaPrincipal.mainloop()

    def mostrar_ventanaModificaciones_admin(ventanaPrincipal):
        
        global entry_nombre_admin
        global entry_CURP_admin
        global entry_FechaNac_admin
        global entry_numCuenta_admin
        global genero_seleccionado_admin
        global nacionalidad_seleccionada_admin
        global entry_numCuenta_admin

        ventanaPrincipal.title("Modificaciones de administradores")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")
        
        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Modificación de información", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
        usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label2.place(relx=0.3, rely=0.43, anchor="w")
        usuario_labelG = tk.Label(ventanaPrincipal, text="Género: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_labelG.place(relx=0.3, rely=0.505, anchor="w")
        usuario_label3 = tk.Label(ventanaPrincipal, text="Nacionalidad del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label3.place(relx=0.3, rely=0.57, anchor="w")
        usuario_label4 = tk.Label(ventanaPrincipal, text="CURP del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label4.place(relx=0.3, rely=0.64, anchor="w")
        usuario_label5 = tk.Label(ventanaPrincipal, text="Fecha de nacimiento del administrador: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        usuario_label5.place(relx=0.3, rely=0.71, anchor="w")
        

        opciones_genero = ["M", "F"]
        # Variable para almacenar la selección del usuario
        genero_seleccionado_admin = tk.StringVar(ventanaPrincipal)
        genero_seleccionado_admin.set(opciones_genero[0])  # Seleccionar la primera opción por defecto


        opciones_nacionalidad = ["mexicana", "extranjera"]

        # Variable para almacenar la selección del usuario
        nacionalidad_seleccionada_admin = tk.StringVar(ventanaPrincipal)
        nacionalidad_seleccionada_admin.set(opciones_nacionalidad[0])  # Seleccionar la primera opción por defecto

        entry_numCuenta_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_numCuenta_admin.place(relx=0.7, rely=0.37, anchor="w")
        entry_nombre_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_nombre_admin.place(relx=0.7, rely=0.43, anchor="w")
        entry_genero = tk.OptionMenu(ventanaPrincipal, genero_seleccionado_admin, *opciones_genero)
        entry_genero.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_genero.place(relx=0.697, rely=0.50, anchor="w")
        entry_nacionalidad = tk.OptionMenu(ventanaPrincipal, nacionalidad_seleccionada_admin, *opciones_nacionalidad)
        entry_nacionalidad.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
        entry_nacionalidad.place(relx=0.697, rely=0.57, anchor="w")
        entry_CURP_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_CURP_admin.place(relx=0.7, rely=0.64, anchor="w")
        entry_FechaNac_admin = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
        entry_FechaNac_admin.place(relx=0.7, rely=0.71, anchor="w")
        
        def validar_campos():
            if entry_numCuenta_admin.get() and entry_nombre_admin.get() and entry_CURP_admin.get() and entry_FechaNac_admin.get():
                boton_confirmarCambios.config(state="normal", bg=color_hex2)  # Habilitar el botón "Confirmar cambios" y establecer el color de fondo normal
            else:
                boton_confirmarCambios.config(state="disabled", bg="gray")  # Deshabilitar el botón "Confirmar cambios" y establecer el color de fondo en gris

        # Asociar la función validar_campos a cada campo de entrada para que se llame cada vez que se modifique un campo
        entry_numCuenta_admin.bind("<KeyRelease>", lambda event: validar_campos())
        entry_nombre_admin.bind("<KeyRelease>", lambda event: validar_campos())
        entry_CURP_admin.bind("<KeyRelease>", lambda event: validar_campos())
        entry_FechaNac_admin.bind("<KeyRelease>", lambda event: validar_campos())

        def aceptar_modificacion():
            num_cuenta = entry_numCuenta_admin.get()  # Obtener el número de cuenta ingresado manualmente
            cursorRowCount = CAdmin.validacion_admin(num_cuenta)
            alumnos = CAdmin.buscarAdminPorNumeroDeCuenta(num_cuenta)  # Buscar los alumnos por número de cuenta
            if alumnos and cursorRowCount != 0:
                # Solo tomamos el primer alumno encontrado para llenar los campos
                alumno = alumnos[0]
                llenar_campos_con_informacion_alumno(alumno)  # Llenar los campos con la información del alumno
            else:
                messagebox.showerror("Error", "No se encontró ningún alumno con ese número de cuenta")

        def llenar_campos_con_informacion_alumno(alumno):
            if alumno:
                nombre, genero, nacionalidad, CURP, fecha_nac = alumno
                entry_nombre_admin.delete(0, 'end')
                entry_nombre_admin.insert(0, nombre)
                genero_seleccionado_admin.set(genero)
                nacionalidad_seleccionada_admin.set(nacionalidad)
                entry_CURP_admin.delete(0, 'end')
                entry_CURP_admin.insert(0, CURP)
                entry_FechaNac_admin.delete(0, 'end')
                entry_FechaNac_admin.insert(0, fecha_nac)
                validar_campos()  # Verificar si todos los campos están completos después de llenarlos
            else:
                messagebox.showerror("Error", "No se encontró ningún alumno con ese número de cuenta")

        boton_buscarAlumno = tk.Button(ventanaPrincipal, text="Buscar Administrador", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=aceptar_modificacion)
        boton_buscarAlumno.place(relx=0.625, rely=0.82, anchor="center")

        boton_confirmarCambios = tk.Button(ventanaPrincipal, text="Confirmar cambios", width=47, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=actualizar_datos_de_base_de_datos, state="disabled", bg="gray")
        boton_confirmarCambios.place(relx=0.625, rely=0.9, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaConsultas_admin(ventanaPrincipal):
        ventanaPrincipal.title("Consultas de administradores")
        
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los administrador", padx=0, pady=1, bg="white")
        groupBox.place(relx=0.615, rely=0.58, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

        tree = ttk.Treeview(groupBox, columns=("Nombre", "Género", "Nacionalidad", "CURP", "Fecha Nac", "NC"), show='headings',height=5)
        tree.grid(row=0, column=0, sticky="nsew")

        # Configurar scrollbar horizontal
        scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")
        tree.configure(xscrollcommand=scroll_x.set)

        # Configurar scrollbar vertical
        scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=scroll_y.set)
        tree.configure(height=14)
        tree.column("#1", anchor="center", width=110)
        tree.heading("#1", text="Nombre")
        tree.column("#2", anchor="center", width=50)
        tree.heading("#2", text="Género")
        tree.column("#3", anchor="center", width=80)
        tree.heading("#3", text="Nacionalidad")
        tree.column("#4", anchor="center", width=70)
        tree.heading("#4", text="CURP")
        tree.column("#5", anchor="center", width=70)
        tree.heading("#5", text="Fecha Nac")
        tree.column("#6", anchor="center", width=60)
        tree.heading("#6", text="NC")

        for row in CAdmin.mostrarAdmin():
            tree.insert("","end", values=row)

        
        # Función para mostrar la información completa al hacer doble clic en una fila
        def mostrar_info_completa(event):
            item = tree.item(tree.selection())
            values = item['values']
            messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

        # Vincular evento de doble clic a la función mostrar_info_completa
        tree.bind("<Double-1>", mostrar_info_completa)

        ventanaPrincipal.mainloop()

    def pasar_datos_de_base_de_datos():
        global entry_nombre_admin
        global entry_CURP_admin
        global entry_FechaNac_admin
        global entry_numCuenta_admin
        global genero_seleccionado_admin
        global nacionalidad_seleccionada_admin
        global contrasena_administrador

        try:
            nombre = entry_nombre_admin.get()
            genero = genero_seleccionado_admin.get()
            nacionalidad = nacionalidad_seleccionada_admin.get()
            curp = entry_CURP_admin.get()
            fechaNac = entry_FechaNac_admin.get()
            contra = contrasena_administrador.get()
            print("Nombre: "+ entry_nombre_admin.get())
            cursorID = CAdmin.login(contra)
            cursorCURPRowCount = CAdmin.validacion_curp(curp)
            patron = r"^[a-zA-ZÀ-ÿ']+([ \t]+[a-zA-ZÀ-ÿ']+)*$"

            if not re.search(patron, nombre):
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return

            if entry_nombre_admin is None or len(entry_nombre_admin.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac_admin.delete(0, 'end')
                return

            if len(curp) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP_admin.delete(0, 'end')
                return

            if cursorCURPRowCount == 1:
                messagebox.showerror("CURP", "¡Curp repetido!")
                entry_CURP_admin.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CAdmin.ingresarAdmin(nombre, genero, nacionalidad, curp, fechaNac, cursorID)   
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre_admin.delete(0, 'end')
            entry_CURP_admin.delete(0, 'end')
            entry_FechaNac_admin.delete(0, 'end')
            contrasena_administrador.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos {}".format(error))

    def actualizar_datos_de_base_de_datos():
        global entry_nombre_admin
        global entry_CURP_admin
        global entry_FechaNac_admin
        global entry_numCuenta_admin
        global genero_seleccionado_admin
        global nacionalidad_seleccionada_admin
        global entry_numCuenta_admin

        try:
            nombre = entry_nombre_admin.get()
            genero = genero_seleccionado_admin.get()
            nacionalidad = nacionalidad_seleccionada_admin.get()
            CURP = entry_CURP_admin.get()
            fechaNac = entry_FechaNac_admin.get()
            numCuenta = entry_numCuenta_admin.get()
            print("Nombre: "+ entry_nombre_admin.get())

            if entry_nombre_admin is None or len(entry_nombre_admin.get()) < 2:
                messagebox.showerror("Alumno", "¡Nombre inválido!")
                entry_nombre_admin.delete(0, 'end')
                return

            # Validar el formato de la fecha
            if not validar_fecha(fechaNac):
                messagebox.showerror("Info", "Fecha de nacimiento incorrecta")
                entry_FechaNac_admin.delete(0, 'end')
                return

            if len(CURP) != 18:
                messagebox.showerror("Info", "CURP incorrecto")
                entry_CURP_admin.delete(0, 'end')
                return
            
            # Si todos los datos son válidos, ingresar el alumno
            CAdmin.actualizarAdmin(nombre, genero, nacionalidad, CURP, fechaNac, numCuenta)
            messagebox.showinfo("Info", "Datos guardados correctamente")
            entry_nombre_admin.delete(0, 'end')
            entry_CURP_admin.delete(0, 'end')
            entry_FechaNac_admin.delete(0, 'end')
            entry_numCuenta_admin.delete(0, 'end')
        
        except ValueError as error:
            print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos {}".format(error))

    
    #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
    ventanaPrincipal.title("Modificación de Administradores")
    
    imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)
    
    imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil2
    icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

    imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil3
    icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

    imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

    imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil6
    icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    canvas2.place(x=0, y=0)

    #Botones
    boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaMenu(ventanaPrincipal))
    canvas2.create_window(-26, 90, anchor="w", window=boton)
    boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_admin(ventanaPrincipal))
    canvas2.create_window(-61, 120, anchor="w", window=boton2)
    boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_admin(ventanaPrincipal))
    canvas2.create_window(-53, 150, anchor="w", window=boton3)
    boton4 = tk.Button(canvas2, text="Modificación", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificaciones_admin(ventanaPrincipal))
    canvas2.create_window(-7, 180, anchor="w", window=boton4)
    boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_admin(ventanaPrincipal))
    canvas2.create_window(-28, 210, anchor="w", window=boton6)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def mostrar_ventanaPerfil(ventanaPrincipal):
    global usuarioGeneral
    print(usuarioGeneral)

    auxiliar = CAlumno.buscarAlumnoPorNumeroDeCuenta(usuarioGeneral)
    ventanaPrincipal.title("Perfil")
    # Crear el rectángulo
    rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
    rectangulo.place(relx=0.644, rely=0.651, anchor="center")

    texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Datos del alumno", font=("Helvetica", 16, "bold"), bg="white")
    texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

    if auxiliar:
        # Mostrar los datos del alumno
        usuario_label = tk.Label(ventanaPrincipal, text=auxiliar[0][0], font=("Helvetica", 10, "italic"), fg="black", bg="white")
        usuario_label.place(relx=0.6, rely=0.55, anchor="center")

        genero_label = tk.Label(ventanaPrincipal, text="Género:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        genero_label.place(relx=0.3, rely=0.65, anchor="w")
        usuario_genero_label = tk.Label(ventanaPrincipal, text=auxiliar[0][1], font=("Helvetica", 10), fg="black", bg="white")
        usuario_genero_label.place(relx=0.7, rely=0.65, anchor="w")

        nacionalidad_label = tk.Label(ventanaPrincipal, text="Nacionalidad:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        nacionalidad_label.place(relx=0.3, rely=0.71, anchor="w")
        usuario_nacionalidad_label = tk.Label(ventanaPrincipal, text=auxiliar[0][2], font=("Helvetica", 10), fg="black", bg="white")
        usuario_nacionalidad_label.place(relx=0.7, rely=0.71, anchor="w")

        curp_label = tk.Label(ventanaPrincipal, text="CURP:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        curp_label.place(relx=0.3, rely=0.77, anchor="w")
        usuario_curp_label = tk.Label(ventanaPrincipal, text=auxiliar[0][3], font=("Helvetica", 10), fg="black", bg="white")
        usuario_curp_label.place(relx=0.7, rely=0.77, anchor="w")

        fechaNac_label = tk.Label(ventanaPrincipal, text="Fecha de nacimiento:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        fechaNac_label.place(relx=0.3, rely=0.83, anchor="w")
        usuario_fechaNac_label = tk.Label(ventanaPrincipal, text=str(auxiliar[0][4]), font=("Helvetica", 10), fg="black", bg="white")
        usuario_fechaNac_label.place(relx=0.7, rely=0.83, anchor="w")

        numCuenta_label = tk.Label(ventanaPrincipal, text="Número de cuenta:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        numCuenta_label.place(relx=0.3, rely=0.89, anchor="w")
        usuario_numCuenta_label = tk.Label(ventanaPrincipal, text=str(usuarioGeneral), font=("Helvetica", 10), fg="black", bg="white")
        usuario_numCuenta_label.place(relx=0.7, rely=0.89, anchor="w")
    else:
        messagebox.showerror("Error", "No se encontró al alumno")

    global imagen_tk2
    imagenPerfil = Image.open(r"Imagenes\\Estudiante.png")
    imagenPerfil = imagenPerfil.resize((120, 70))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagenPerfil)
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk2, borderwidth=0, highlightthickness=0, bg="white")
    label_imagen.place(x=295, y=130)

    ventanaPrincipal.mainloop()

def mostrar_ventanaPerfil_admin(ventanaPrincipal):
    global usuarioGeneral

    auxiliar = CAdmin.buscarAdminPorNumeroDeCuenta(usuarioGeneral)
    ventanaPrincipal.title("Perfil")
    # Crear el rectángulo
    rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
    rectangulo.place(relx=0.644, rely=0.651, anchor="center")

    texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Datos del administrador", font=("Helvetica", 16, "bold"), bg="white")
    texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

    if auxiliar:
        # Mostrar los datos del alumno
        usuario_label = tk.Label(ventanaPrincipal, text=auxiliar[0][0], font=("Helvetica", 10, "italic"), fg="black", bg="white")
        usuario_label.place(relx=0.6, rely=0.55, anchor="center")

        genero_label = tk.Label(ventanaPrincipal, text="Género:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        genero_label.place(relx=0.3, rely=0.65, anchor="w")
        usuario_genero_label = tk.Label(ventanaPrincipal, text=auxiliar[0][1], font=("Helvetica", 10), fg="black", bg="white")
        usuario_genero_label.place(relx=0.7, rely=0.65, anchor="w")

        nacionalidad_label = tk.Label(ventanaPrincipal, text="Nacionalidad:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        nacionalidad_label.place(relx=0.3, rely=0.71, anchor="w")
        usuario_nacionalidad_label = tk.Label(ventanaPrincipal, text=auxiliar[0][2], font=("Helvetica", 10), fg="black", bg="white")
        usuario_nacionalidad_label.place(relx=0.7, rely=0.71, anchor="w")

        curp_label = tk.Label(ventanaPrincipal, text="CURP:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        curp_label.place(relx=0.3, rely=0.77, anchor="w")
        usuario_curp_label = tk.Label(ventanaPrincipal, text=auxiliar[0][3], font=("Helvetica", 10), fg="black", bg="white")
        usuario_curp_label.place(relx=0.7, rely=0.77, anchor="w")

        fechaNac_label = tk.Label(ventanaPrincipal, text="Fecha de nacimiento:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        fechaNac_label.place(relx=0.3, rely=0.83, anchor="w")
        usuario_fechaNac_label = tk.Label(ventanaPrincipal, text=str(auxiliar[0][4]), font=("Helvetica", 10), fg="black", bg="white")
        usuario_fechaNac_label.place(relx=0.7, rely=0.83, anchor="w")

        numCuenta_label = tk.Label(ventanaPrincipal, text="Número de cuenta:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
        numCuenta_label.place(relx=0.3, rely=0.89, anchor="w")
        usuario_numCuenta_label = tk.Label(ventanaPrincipal, text=str(usuarioGeneral), font=("Helvetica", 10), fg="black", bg="white")
        usuario_numCuenta_label.place(relx=0.7, rely=0.89, anchor="w")
    else:
        messagebox.showerror("Error", "No se encontró al admin")

    global imagen_tk2
    imagenPerfil = Image.open(r"Imagenes\\Estudiante.png")
    imagenPerfil = imagenPerfil.resize((120, 70))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk2 = ImageTk.PhotoImage(imagenPerfil)
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk2, borderwidth=0, highlightthickness=0, bg="white")
    label_imagen.place(x=295, y=130)

    ventanaPrincipal.mainloop()

def mostrar_ventanaTrayectoria(ventanaPrincipal):
            
    global entry_numCuenta_GRUPO
    global usuarioGeneral
    ventanaPrincipal.title("Consultas de Grupos")
    
    # Crear el rectángulo
    rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
    rectangulo.place(relx=0.644, rely=0.651, anchor="center")

    groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los Grupos", padx=0, pady=1, bg="white")
    groupBox.place(relx=0.615, rely=0.62, anchor="center")  # Ajustado para colocar correctamente el LabelFrame


    tree = ttk.Treeview(groupBox, columns=("ID Grupo", "Nombre de Referencia", "Nombre de la Materia","Nombre del Profesor"), show='headings',height=5)
    tree.grid(row=0, column=0, sticky="nsew")

    # Configurar scrollbar horizontal
    scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
    scroll_x.grid(row=1, column=0, sticky="ew")
    tree.configure(xscrollcommand=scroll_x.set)

    # Configurar scrollbar vertical
    scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scroll_y.set)
    tree.configure(height=15)
    tree.column("#1", anchor="center", width=80)
    tree.heading("#1", text="ID Grupo")
    tree.column("#2", anchor="center", width=120)
    tree.heading("#2", text="Nombre de Referencia")
    tree.column("#3", anchor="center", width=120)
    tree.heading("#3", text="Nombre de la Materia")
    tree.column("#4", anchor="center", width=120)
    tree.heading("#4", text="Nombre del Profesor")

    for row in CGrupo.buscarGrupoPorNC(usuarioGeneral):
        tree.insert("","end", values=row)

    
    # Función para mostrar la información completa al hacer doble clic en una fila
    def mostrar_info_completa(event):
        item = tree.item(tree.selection())
        values = item['values']
        messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

    # Vincular evento de doble clic a la función mostrar_info_completa
    tree.bind("<Double-1>", mostrar_info_completa)


    ventanaPrincipal.mainloop()

def mostrar_ventanaCalificaciones(ventanaPrincipal):
            
    global entry_numCuenta_GRUPO
    global usuarioGeneral
    ventanaPrincipal.title("Consultas de Grupos")
    
    # Crear el rectángulo
    rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
    rectangulo.place(relx=0.644, rely=0.651, anchor="center")

    groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los Grupos", padx=0, pady=1, bg="white")
    groupBox.place(relx=0.615, rely=0.62, anchor="center")  # Ajustado para colocar correctamente el LabelFrame


    tree = ttk.Treeview(groupBox, columns=("ID Calificación", "Materia", "NC Alumno","Nombre alumno", "Calificacion"), show='headings',height=5)
    tree.grid(row=0, column=0, sticky="nsew")

    # Configurar scrollbar horizontal
    scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
    scroll_x.grid(row=1, column=0, sticky="ew")
    tree.configure(xscrollcommand=scroll_x.set)

    # Configurar scrollbar vertical
    scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scroll_y.set)
    tree.configure(height=15)
    tree.column("#1", anchor="center", width=80)
    tree.heading("#1", text="ID Calificacion")
    tree.column("#2", anchor="center", width=100)
    tree.heading("#2", text="Materia")
    tree.column("#3", anchor="center", width=80)
    tree.heading("#3", text="NC del alumno")
    tree.column("#4", anchor="center", width=100)
    tree.heading("#4", text="Nombre del alumno")
    tree.column("#5", anchor="center", width=80)
    tree.heading("#5", text="Calificacion")

    for row in CCalificacion.buscarCalifPorID(usuarioGeneral):
        tree.insert("","end", values=row)

    
    # Función para mostrar la información completa al hacer doble clic en una fila
    def mostrar_info_completa(event):
        item = tree.item(tree.selection())
        values = item['values']
        messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

    # Vincular evento de doble clic a la función mostrar_info_completa
    tree.bind("<Double-1>", mostrar_info_completa)


    ventanaPrincipal.mainloop()

def mostrar_ventanaReinscripcion(ventanaPrincipal):
    ventanaPrincipal.title("Reinscripción")
    
    # Crear el rectángulo
    rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
    rectangulo.place(relx=0.644, rely=0.651, anchor="center")

    
    texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Reinscripción", font=("Helvetica", 16, "bold"), bg="white")
    texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")
     
    ventanaPrincipal.mainloop()

def validar_fecha(fecha):
    # Expresión regular para el formato año-día-mes
    patron = r'^\d{4}-\d{2}-\d{2}$'
    
    if not re.match(patron, fecha):
        return False
    
    # Extraer los componentes de la fecha
    año, mes, día = map(int, fecha.split('-'))
    
    # Validar los rangos
    if año < 1800 or año > 2024:
        return False
    if mes < 1 or mes > 12:
        return False
    if día < 1 or día > 31:
        return False
    
    return True

def mostrar_ventanaPrincipal_profesor(ventanaPrincipal):

    def mostrar_ventanaPerfil_profesor(ventanaPrincipal):
        global usuarioGeneral
        print(usuarioGeneral)

        auxiliar = CProfesor.buscarProfePorNumeroDeCuenta(usuarioGeneral)
        ventanaPrincipal.title("Perfil")
        # Crear el rectángulo
        rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
        rectangulo.place(relx=0.644, rely=0.651, anchor="center")

        texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Datos del profesor", font=("Helvetica", 16, "bold"), bg="white")
        texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

        if auxiliar:
            # Mostrar los datos del alumno
            usuario_label = tk.Label(ventanaPrincipal, text=auxiliar[0][0], font=("Helvetica", 10, "italic"), fg="black", bg="white")
            usuario_label.place(relx=0.6, rely=0.55, anchor="center")

            genero_label = tk.Label(ventanaPrincipal, text="Género:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            genero_label.place(relx=0.3, rely=0.65, anchor="w")
            usuario_genero_label = tk.Label(ventanaPrincipal, text=auxiliar[0][1], font=("Helvetica", 10), fg="black", bg="white")
            usuario_genero_label.place(relx=0.7, rely=0.65, anchor="w")

            nacionalidad_label = tk.Label(ventanaPrincipal, text="Nacionalidad:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            nacionalidad_label.place(relx=0.3, rely=0.71, anchor="w")
            usuario_nacionalidad_label = tk.Label(ventanaPrincipal, text=auxiliar[0][2], font=("Helvetica", 10), fg="black", bg="white")
            usuario_nacionalidad_label.place(relx=0.7, rely=0.71, anchor="w")

            curp_label = tk.Label(ventanaPrincipal, text="CURP:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            curp_label.place(relx=0.3, rely=0.77, anchor="w")
            usuario_curp_label = tk.Label(ventanaPrincipal, text=auxiliar[0][3], font=("Helvetica", 10), fg="black", bg="white")
            usuario_curp_label.place(relx=0.7, rely=0.77, anchor="w")

            fechaNac_label = tk.Label(ventanaPrincipal, text="Fecha de nacimiento:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            fechaNac_label.place(relx=0.3, rely=0.83, anchor="w")
            usuario_fechaNac_label = tk.Label(ventanaPrincipal, text=str(auxiliar[0][4]), font=("Helvetica", 10), fg="black", bg="white")
            usuario_fechaNac_label.place(relx=0.7, rely=0.83, anchor="w")

            numCuenta_label = tk.Label(ventanaPrincipal, text="Número de cuenta:", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            numCuenta_label.place(relx=0.3, rely=0.89, anchor="w")
            usuario_numCuenta_label = tk.Label(ventanaPrincipal, text=str(usuarioGeneral), font=("Helvetica", 10), fg="black", bg="white")
            usuario_numCuenta_label.place(relx=0.7, rely=0.89, anchor="w")
        else:
            messagebox.showerror("Error", "No se encontró al alumno")

        global imagen_tk2
        imagenPerfil = Image.open(r"Imagenes\\Estudiante.png")
        imagenPerfil = imagenPerfil.resize((120, 70))  # Ajustar el tamaño de la imagen si es necesario
        imagen_tk2 = ImageTk.PhotoImage(imagenPerfil)
        label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk2, borderwidth=0, highlightthickness=0, bg="white")
        label_imagen.place(x=295, y=130)

        ventanaPrincipal.mainloop()

    def mostrar_ventanaModificacionMateria(ventanaPrincipal):
    
        def mostrar_ventanaAltas_Materia(ventanaPrincipal):
            global entry_nombre_materia
            global hora_inicio
            global hora_fin
            global dia_clase

            ventanaPrincipal.title("Altas de Materias")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Nueva Materia", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre de la Materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
            usuario_labelG = tk.Label(ventanaPrincipal, text="Fecha de inicio del curso: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")
            usuario_label4 = tk.Label(ventanaPrincipal, text="Hora de inicio de clase: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label4.place(relx=0.3, rely=0.49, anchor="w")
            usuario_label5 = tk.Label(ventanaPrincipal, text="Día de clase: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label5.place(relx=0.3, rely=0.56, anchor="w")

            opciones_fecha_inicio = ["2024-06-15", "2024-07-15", "2024-08-15", "2024-09-15"]
            # Variable para almacenar la selección del usuario
            hora_inicio = tk.StringVar(ventanaPrincipal)
            hora_inicio.set(opciones_fecha_inicio[0])  # Seleccionar la primera opción por defecto

            opciones_hora_inicio = ["07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00","15:00:00"]
            # Variable para almacenar la selección del usuario
            hora_fin = tk.StringVar(ventanaPrincipal)
            hora_fin.set(opciones_hora_inicio[0])  # Seleccionar la primera opción por defecto

            opciones_dia_clase = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
            # Variable para almacenar la selección del usuario
            dia_clase = tk.StringVar(ventanaPrincipal)
            dia_clase.set(opciones_dia_clase[0])  # Seleccionar la primera opción por defecto


            entry_nombre_materia = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_materia.place(relx=0.7, rely=0.35, anchor="w")
            entry_hora_inicio = tk.OptionMenu(ventanaPrincipal, hora_inicio, *opciones_fecha_inicio)
            entry_hora_inicio.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_hora_inicio.place(relx=0.697, rely=0.415, anchor="w")
            entry_fecha_inicio = tk.OptionMenu(ventanaPrincipal, hora_fin, *opciones_hora_inicio)
            entry_fecha_inicio.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_fecha_inicio.place(relx=0.697, rely=0.485, anchor="w")
            entry_dia_clase = tk.OptionMenu(ventanaPrincipal, dia_clase, *opciones_dia_clase)
            entry_dia_clase.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_dia_clase.place(relx=0.697, rely=0.555, anchor="w")
            
            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def mostrar_ventanaBajas_Materia(ventanaPrincipal):

            ventanaPrincipal.title("Bajas de Materias")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar materia", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id de la materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
            usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

            entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_profe.place(relx=0.7, rely=0.50, anchor="w")
            entry_CURP_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
            entry_CURP_profe.place(relx=0.7, rely=0.57, anchor="w")
            
            def eliminar_alumno():
                try:
                    numCuenta = entry_numCuenta_profe.get()

                    if not numCuenta or len(numCuenta) < 1:
                        messagebox.showerror("Materia", "¡Id no encontrado!")
                        entry_nombre_profe.delete(0, 'end')
                        return
                    
                    # Si todos los datos son válidos, ingresar el alumno
                    cursorRowCount = CMateria.borrarMateriaPorId(numCuenta)

                    if cursorRowCount == 0:
                        messagebox.showerror("Materia", "¡Id no encontrado!")
                        entry_numCuenta_profe.delete(0, 'end')
                        return
                    messagebox.showinfo("Info", "Materia eliminada exitosamente")
                    entry_numCuenta_profe.delete(0, 'end')
                
                except ValueError as error:
                    print("Error al ingresar datos en bajas de materias {}".format(error))


            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
            
            
            ventanaPrincipal.mainloop()

        def mostrar_ventanaModificaciones_Materia(ventanaPrincipal):
            
            def validar_campos():
                if entry_nombre_materia.get() and hora_inicio.get() and hora_fin.get() and dia_clase.get():
                    boton_confirmarCambios.config(state="normal", bg=color_hex2)
                else:
                    boton_confirmarCambios.config(state="disabled", bg="gray")

            def aceptar_modificacion():
                id_materia = entry_numCuenta_profe.get()
                resultados = CMateria.buscarMateriaPorId(id_materia)
                if resultados:
                    llenar_campos_con_informacion_alumno(resultados[0]) 
                else:
                    messagebox.showerror("Error", "No se encontró ninguna materia con ese id")

            def llenar_campos_con_informacion_alumno(alumno):
                if alumno:
                    nombre, fecha_inicio, hora_inicio_val, dia_clase_val = alumno
                    entry_nombre_materia.delete(0, 'end')
                    entry_nombre_materia.insert(0, nombre)
                    hora_inicio.set(fecha_inicio)
                    hora_fin.set(hora_inicio_val)
                    dia_clase.set(dia_clase_val)
                    validar_campos()
                else:
                    messagebox.showerror("Error", "No se encontró ninguna materia ..")

            global entry_nombre_materia
            global hora_inicio
            global hora_fin
            global dia_clase
            global entry_numCuenta_profe

            ventanaPrincipal.title("Modificación de Materias")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")
            
            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Modificación de información", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id de la materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre de la Materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.43, anchor="w")
            usuario_labelG = tk.Label(ventanaPrincipal, text="Hora de inicio: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.505, anchor="w")
            usuario_label3 = tk.Label(ventanaPrincipal, text="Fecha de inicio: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label3.place(relx=0.3, rely=0.57, anchor="w")
            usuario_label4 = tk.Label(ventanaPrincipal, text="Día: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label4.place(relx=0.3, rely=0.64, anchor="w")
            

            opciones_fecha_inicio = ["2024-06-15", "2024-07-15", "2024-08-15", "2024-09-15"]
            # Variable para almacenar la selección del usuario
            hora_inicio = tk.StringVar(ventanaPrincipal)
            hora_inicio.set(opciones_fecha_inicio[0])  # Seleccionar la primera opción por defecto

            opciones_hora_inicio = ["07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00", "12:00:00", "13:00:00", "14:00:00","15:00:00"]
            # Variable para almacenar la selección del usuario
            hora_fin = tk.StringVar(ventanaPrincipal)
            hora_fin.set(opciones_hora_inicio[0])  # Seleccionar la primera opción por defecto

            opciones_dia_clase = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
            # Variable para almacenar la selección del usuario
            dia_clase = tk.StringVar(ventanaPrincipal)
            dia_clase.set(opciones_dia_clase[0])  # Seleccionar la primera opción por defecto

            entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre_materia = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_materia.place(relx=0.7, rely=0.44, anchor="w")
            entry_hora_inicio = tk.OptionMenu(ventanaPrincipal, hora_fin, *opciones_hora_inicio)
            entry_hora_inicio.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_hora_inicio.place(relx=0.697, rely=0.51, anchor="w")
            entry_fecha_inicio = tk.OptionMenu(ventanaPrincipal, hora_inicio, *opciones_fecha_inicio)
            entry_fecha_inicio.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_fecha_inicio.place(relx=0.697, rely=0.58, anchor="w")
            entry_dia_clase = tk.OptionMenu(ventanaPrincipal, dia_clase, *opciones_dia_clase)
            entry_dia_clase.config(font=("Helvetica", 9), bg="white", bd=1, relief="solid")
            entry_dia_clase.place(relx=0.697, rely=0.65, anchor="w")
            
            
            # Asociar la función validar_campos a cada campo de entrada para que se llame cada vez que se modifique un campo
            entry_numCuenta_profe.bind("<KeyRelease>", lambda event: validar_campos())
            entry_nombre_materia.bind("<KeyRelease>", lambda event: validar_campos())
            entry_hora_inicio.bind("<KeyRelease>", lambda event: validar_campos())
            entry_dia_clase.bind("<KeyRelease>", lambda event: validar_campos())
            entry_fecha_inicio.bind("<KeyRelease>", lambda event: validar_campos())
            
            boton_buscarAlumno = tk.Button(ventanaPrincipal, text="Buscar Materia", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=aceptar_modificacion)
            boton_buscarAlumno.place(relx=0.625, rely=0.82, anchor="center")

            boton_confirmarCambios = tk.Button(ventanaPrincipal, text="Confirmar cambios", width=47, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=actualizar_datos_de_base_de_datos, state="disabled", bg="gray")
            boton_confirmarCambios.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def mostrar_ventanaConsultas_Materia(ventanaPrincipal):
            
            def mostrarMateriaBusqueda():
                global entry_numCuenta_profe
                nombre = entry_numCuenta_profe.get()
                print(nombre)
                tree = ttk.Treeview(groupBox, columns=("ID", "Nombre", "FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "Día"), show='headings',height=5)
                tree.grid(row=0, column=0, sticky="nsew")

                # Configurar scrollbar horizontal
                scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")
                tree.configure(xscrollcommand=scroll_x.set)

                # Configurar scrollbar vertical
                scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")
                tree.configure(yscrollcommand=scroll_y.set)
                tree.configure(height=11)
                tree.column("#1", anchor="center", width=40)
                tree.heading("#1", text="ID")
                tree.column("#2", anchor="center", width=70)
                tree.heading("#2", text="Nombre")
                tree.column("#3", anchor="center", width=70)
                tree.heading("#3", text="FechaInicio")
                tree.column("#4", anchor="center", width=70)
                tree.heading("#4", text="FechaFin")
                tree.column("#5", anchor="center", width=70)
                tree.heading("#5", text="HoraInicio")
                tree.column("#6", anchor="center", width=60)
                tree.heading("#6", text="HoraFin")
                tree.column("#7", anchor="center", width=60)
                tree.heading("#7", text="Día")

                for row in CMateria.mostrarMateriaPorNombre(nombre):
                    tree.insert("","end", values=row)

                
                # Función para mostrar la información completa al hacer doble clic en una fila
                def mostrar_info_completa(event):
                    item = tree.item(tree.selection())
                    values = item['values']
                    messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))
                # Vincular evento de doble clic a la función mostrar_info_completa
                tree.bind("<Double-1>", mostrar_info_completa)
            
            global entry_numCuenta_profe
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de materias", padx=0, pady=1, bg="white")
            groupBox.place(relx=0.615, rely=0.65, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

            usuario_label7 = tk.Label(ventanaPrincipal, text="Nombre materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.225, anchor="w")
            entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_profe.place(relx=0.5, rely=0.225, anchor="w")

            tree = ttk.Treeview(groupBox, columns=("ID", "Nombre", "FechaInicio", "FechaFin", "HoraInicio", "HoraFin", "Día"), show='headings',height=5)
            tree.grid(row=0, column=0, sticky="nsew")

            # Configurar scrollbar horizontal
            scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")
            tree.configure(xscrollcommand=scroll_x.set)

            # Configurar scrollbar vertical
            scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=scroll_y.set)
            tree.configure(height=11)
            tree.column("#1", anchor="center", width=40)
            tree.heading("#1", text="ID")
            tree.column("#2", anchor="center", width=70)
            tree.heading("#2", text="Nombre")
            tree.column("#3", anchor="center", width=70)
            tree.heading("#3", text="FechaInicio")
            tree.column("#4", anchor="center", width=70)
            tree.heading("#4", text="FechaFin")
            tree.column("#5", anchor="center", width=70)
            tree.heading("#5", text="HoraInicio")
            tree.column("#6", anchor="center", width=60)
            tree.heading("#6", text="HoraFin")
            tree.column("#7", anchor="center", width=60)
            tree.heading("#7", text="Día")

            for row in CMateria.mostrarMateria():
                tree.insert("","end", values=row)
            
            # Función para mostrar la información completa al hacer doble clic en una fila
            def mostrar_info_completa(event):
                item = tree.item(tree.selection())
                values = item['values']
                messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

            # Vincular evento de doble clic a la función mostrar_info_completa
            tree.bind("<Double-1>", mostrar_info_completa)

            boton_aceptar = tk.Button(ventanaPrincipal, text="Buscar", width=10, bg=color_hex2, fg="white", font=("Helvetica", 9, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=mostrarMateriaBusqueda)
            boton_aceptar.place(relx=0.86, rely=0.225, anchor="center")

            ventanaPrincipal.mainloop()

        def pasar_datos_de_base_de_datos():
            global entry_nombre_materia
            global hora_inicio
            global hora_fin
            global dia_clase

            try:
                nombre = entry_nombre_materia.get()
                hora = hora_inicio.get()
                fecha = hora_fin.get()
                dia = dia_clase.get()


                if entry_nombre_materia is None or len(entry_nombre_materia.get()) < 2:
                    messagebox.showerror("Alumno", "¡Nombre inválido!")
                    return

                
                # Si todos los datos son válidos, ingresar el alumno
                CMateria.ingresarMateria(nombre, hora, fecha, dia)   
                messagebox.showinfo("Info", "Datos guardados correctamente")
                entry_nombre_materia.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos de materia en la función pasar_datos_de_base_de_datos {}".format(error))

        def actualizar_datos_de_base_de_datos():
            global entry_nombre_materia
            global hora_inicio
            global hora_fin
            global dia_clase
            global entry_numCuenta_profe

            try:
                nombreMateria = entry_nombre_materia.get()
                horarioInicio = hora_inicio.get()
                fechaInicio = hora_fin.get()
                diaClase = dia_clase.get()
                idMateria = entry_numCuenta_profe.get()  # Corregido aquí

                if nombreMateria is None or len(nombreMateria) < 2:  # Corregido aquí
                    messagebox.showerror("Materia", "¡Nombre inválido!")
                    entry_nombre_materia.delete(0, 'end')
                    return

                # Si todos los datos son válidos, actualizar la materia
                CMateria.actualizarMateria(idMateria, nombreMateria, fechaInicio, horarioInicio, diaClase)
                messagebox.showinfo("Info", "Datos guardados correctamente")

                # Borrar los campos de entrada
                entry_nombre_materia.delete(0, 'end')
                # Borrar otros campos si es necesario

            except ValueError as error:
                print("Error al ingresar datos de la materia en la función actualizar_datos_de_base_de_datos {}".format(error))
                
        #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.title("Modificación de Materia")
        
        imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil
        icono_perfil = ImageTk.PhotoImage(imagen_perfil)

        imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil2
        icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

        imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil3
        icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

        imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil4
        icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

        imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil5
        icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

        imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil6
        icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

        # Centrar la nueva ventanaInicioSesion en la pantalla
        ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
        altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
        x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
        y_pos = int((altura_ventanaInicioSesion - 400) / 2)
        ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

        # Crear el canvas para la nueva ventanaInicioSesion
        canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
        canvas2.pack()
        canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
        canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
        canvas2.place(x=0, y=0)

        #Botones
        boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPrincipal_profesor(ventanaPrincipal))
        canvas2.create_window(-26, 90, anchor="w", window=boton)
        boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_Materia(ventanaPrincipal))
        canvas2.create_window(-61, 120, anchor="w", window=boton2)
        boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_Materia(ventanaPrincipal))
        canvas2.create_window(-53, 150, anchor="w", window=boton3)
        boton4 = tk.Button(canvas2, text="Modificación", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificaciones_Materia(ventanaPrincipal))
        canvas2.create_window(-7, 180, anchor="w", window=boton4)
        boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_Materia(ventanaPrincipal))
        canvas2.create_window(-28, 210, anchor="w", window=boton6)
        boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
        canvas2.create_window(-6, 385, anchor="w", window=boton5)
        
        # Agregar la imagen
        imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
        imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
        label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
        label_imagen.place(x=530, y=0)

        preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
        preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

        ventanaPrincipal.mainloop()

      # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
   
    def mostrar_ventanaModificacionGrupos(ventanaPrincipal):
    
        def mostrar_ventanaAltas_Grupos(ventanaPrincipal):
            global entry_nombre_materia
            global entry_nombre_grupo
            

            ventanaPrincipal.title("Altas de Grupos")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Nuevo Grupo", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_labelG = tk.Label(ventanaPrincipal, text="Nombre de referencia del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.35, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Id de la materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.42, anchor="w")
            

            entry_nombre_materia = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_materia.place(relx=0.7, rely=0.35, anchor="w")
            entry_nombre_grupo = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_grupo.place(relx=0.7, rely=0.42, anchor="w")
            
            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def mostrar_ventanaBajas_Grupos(ventanaPrincipal):

            ventanaPrincipal.title("Bajas de Grupos")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar Grupo", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
            usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

            entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_profe.place(relx=0.7, rely=0.50, anchor="w")
            entry_CURP_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
            entry_CURP_profe.place(relx=0.7, rely=0.57, anchor="w")
            
            def eliminar_alumno():
                try:
                    numCuenta = entry_numCuenta_profe.get()

                    if not numCuenta or len(numCuenta) < 1:
                        messagebox.showerror("Alumno", "¡Id no encontrado!")
                        entry_nombre_profe.delete(0, 'end')
                        return
                    
                    # Si todos los datos son válidos, ingresar el alumno
                    cursorRowCount = CGrupo.borrarGrupoPorID(numCuenta)

                    if cursorRowCount == 0:
                        messagebox.showerror("Alumno", "¡Id no encontrado!")
                        entry_numCuenta_profe.delete(0, 'end')
                        return
                    messagebox.showinfo("Info", "Grupo eliminado exitosamente")
                    entry_numCuenta_profe.delete(0, 'end')
                
                except ValueError as error:
                    print("Error al ingresar datos en Bajas de profesores {}".format(error))


            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
            
            
            ventanaPrincipal.mainloop()

        def mostrar_ventanaModificaciones_Grupos(ventanaPrincipal):
            
            def validar_campos():
                if entry_nombre_materia.get() and entry_hora_inicio.get():
                    boton_confirmarCambios.config(state="normal", bg=color_hex2)
                else:
                    boton_confirmarCambios.config(state="disabled", bg="gray")

            def aceptar_modificacion():
                id_materia = entry_numCuenta_profe.get()
                resultados = CGrupo.buscarGrupoPorID(id_materia)
                if resultados:
                    llenar_campos_con_informacion_alumno(resultados[0]) 
                else:
                    messagebox.showerror("Error", "No se encontró ninguna materia con ese id")

            def llenar_campos_con_informacion_alumno(alumno):
                if alumno:
                    nombreReferencia, idMateria = alumno  # Desempaquetar los valores de la tupla
                    entry_nombre_materia.delete(0, 'end')
                    entry_nombre_materia.insert(0, nombreReferencia)
                    entry_hora_inicio.delete(0, 'end')
                    entry_hora_inicio.insert(0, idMateria)
                    validar_campos()  # Verificar si todos los campos están completos después de llenarlos
                else:
                    messagebox.showerror("Error", "No se encontró ninguna materia con ese ID")

            global entry_nombre_materia
            global entry_hora_inicio
            global hora_fin
            global dia_clase
            global entry_numCuenta_profe

            ventanaPrincipal.title("Modificación de Materias")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")
            
            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Modificación de información", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id de la materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Nombre de referencia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.43, anchor="w")
            usuario_labelG = tk.Label(ventanaPrincipal, text="Id materia: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.505, anchor="w")
            
            entry_numCuenta_profe = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_profe.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre_materia = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre_materia.place(relx=0.7, rely=0.44, anchor="w")
            entry_hora_inicio = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_hora_inicio.place(relx=0.7, rely=0.51, anchor="w")
            
            
            # Asociar la función validar_campos a cada campo de entrada para que se llame cada vez que se modifique un campo
            entry_numCuenta_profe.bind("<KeyRelease>", lambda event: validar_campos())
            entry_nombre_materia.bind("<KeyRelease>", lambda event: validar_campos())
            entry_hora_inicio.bind("<KeyRelease>", lambda event: validar_campos())
            
            boton_buscarAlumno = tk.Button(ventanaPrincipal, text="Buscar Materia", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=aceptar_modificacion)
            boton_buscarAlumno.place(relx=0.625, rely=0.82, anchor="center")

            boton_confirmarCambios = tk.Button(ventanaPrincipal, text="Confirmar cambios", width=47, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=actualizar_datos_de_base_de_datos, state="disabled", bg="gray")
            boton_confirmarCambios.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def mostrar_ventanaConsultas_Grupos(ventanaPrincipal):
            
            def mostrarMateriaBusqueda():
                global entry_numCuenta_GRUPO
                nombre = entry_numCuenta_GRUPO.get()
                print("ESTAS AQUI: " + nombre)
                tree = ttk.Treeview(groupBox, columns=("ID", "Nombre", "ID Materia", "ID Profesor"), show='headings',height=5)
                tree.grid(row=0, column=0, sticky="nsew")

                # Configurar scrollbar horizontal
                scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")
                tree.configure(xscrollcommand=scroll_x.set)

                # Configurar scrollbar vertical
                scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")
                tree.configure(yscrollcommand=scroll_y.set)
                tree.configure(height=11)
                tree.column("#1", anchor="center", width=110)
                tree.heading("#1", text="ID")
                tree.column("#2", anchor="center", width=120)
                tree.heading("#2", text="Nombre")
                tree.column("#3", anchor="center", width=110)
                tree.heading("#3", text="ID Materia")
                tree.column("#4", anchor="center", width=100)
                tree.heading("#4", text="ID Profesor")

                for row in CGrupo.mostrarGrupoPorNombre(nombre):
                    tree.insert("","end", values=row)

                # Función para mostrar la información completa al hacer doble clic en una fila
                def mostrar_info_completa(event):
                    item = tree.item(tree.selection())
                    values = item['values']
                    messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))
                # Vincular evento de doble clic a la función mostrar_info_completa
                tree.bind("<Double-1>", mostrar_info_completa)

            global entry_numCuenta_GRUPO
            ventanaPrincipal.title("Consultas de Grupos")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los Grupos", padx=0, pady=1, bg="white")
            groupBox.place(relx=0.615, rely=0.65, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

            usuario_label7 = tk.Label(ventanaPrincipal, text="Nombre de referencia del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.25, rely=0.225, anchor="w")
            entry_numCuenta_GRUPO = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_GRUPO.place(relx=0.62, rely=0.225, anchor="w")

            tree = ttk.Treeview(groupBox, columns=("ID", "Nombre", "ID Materia", "ID Profesor"), show='headings',height=5)
            tree.grid(row=0, column=0, sticky="nsew")

            # Configurar scrollbar horizontal
            scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")
            tree.configure(xscrollcommand=scroll_x.set)

            # Configurar scrollbar vertical
            scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=scroll_y.set)
            tree.configure(height=11)
            tree.column("#1", anchor="center", width=110)
            tree.heading("#1", text="ID")
            tree.column("#2", anchor="center", width=120)
            tree.heading("#2", text="Nombre")
            tree.column("#3", anchor="center", width=110)
            tree.heading("#3", text="ID Materia")
            tree.column("#4", anchor="center", width=100)
            tree.heading("#4", text="ID Profesor")

            for row in CGrupo.mostrarGrupos():
                tree.insert("","end", values=row)

            
            # Función para mostrar la información completa al hacer doble clic en una fila
            def mostrar_info_completa(event):
                item = tree.item(tree.selection())
                values = item['values']
                messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

            # Vincular evento de doble clic a la función mostrar_info_completa
            tree.bind("<Double-1>", mostrar_info_completa)

            boton_aceptar = tk.Button(ventanaPrincipal, text="Buscar", width=8, bg=color_hex2, fg="white", font=("Helvetica", 9, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=mostrarMateriaBusqueda)
            boton_aceptar.place(relx=0.92, rely=0.225, anchor="center")

            ventanaPrincipal.mainloop()

        def pasar_datos_de_base_de_datos():
            global entry_nombre_materia
            global entry_nombre_grupo
            global usuarioGeneral

            try:
                nombre = entry_nombre_materia.get()
                idMAteria = entry_nombre_grupo.get()



                if entry_nombre_materia is None or len(entry_nombre_materia.get()) < 2:
                    messagebox.showerror("Alumno", "¡Nombre inválido!")
                    return
                
                if entry_nombre_grupo is None or len(entry_nombre_grupo.get()) < 1:
                    messagebox.showerror("Alumno", "Id inválido!")
                    return
                
                # Si todos los datos son válidos, ingresar el alumno
                CGrupo.ingresarGrupo(nombre, idMAteria, usuarioGeneral)   
                messagebox.showinfo("Info", "Datos guardados correctamente")
                entry_nombre_profe.delete(0, 'end')
                entry_CURP_profe.delete(0, 'end')
                entry_FechaNac_profe.delete(0, 'end')
                contrasena_profesor.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos del profesor en la función pasar_datos_de_base_de_datos {}".format(error))

        def actualizar_datos_de_base_de_datos():
            global entry_nombre_profe
            global entry_hora_inicio
            global entry_FechaNac_profe
            global entry_numCuenta_profe
            global entry_nombre_materia
            global nacionalidad_seleccionada_profe

            try:
                idGrupo = entry_numCuenta_profe.get()
                nombreReferencia = entry_nombre_materia.get()
                idMateria = entry_hora_inicio.get()

                if entry_nombre_materia is None or len(entry_nombre_materia.get()) < 2:
                    messagebox.showerror("Alumno", "¡Nombre inválido!")
                    entry_nombre_profe.delete(0, 'end')
                    return
                
                # Si todos los datos son válidos, ingresar el alumno
                CGrupo.actualizarGrupo(idGrupo, nombreReferencia, idMateria)
                messagebox.showinfo("Info", "Datos actualizados correctamente")
                entry_numCuenta_profe.delete(0, 'end')
                entry_nombre_materia.delete(0, 'end')
                entry_hora_inicio.delete(0, 'end')
            
            except ValueError as error:
                print("Error al ingresar datos del profesor en la función pasar_datos_de_base_de_datos {}".format(error))

        #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.title("Modificación de Grupos")
        
        imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil
        icono_perfil = ImageTk.PhotoImage(imagen_perfil)

        imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil2
        icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

        imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil3
        icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

        imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil4
        icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

        imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil5
        icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

        imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil6
        icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

        # Centrar la nueva ventanaInicioSesion en la pantalla
        ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
        altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
        x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
        y_pos = int((altura_ventanaInicioSesion - 400) / 2)
        ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

        # Crear el canvas para la nueva ventanaInicioSesion
        canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
        canvas2.pack()
        canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
        canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
        canvas2.place(x=0, y=0)

        #Botones
        boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPrincipal_profesor(ventanaPrincipal))
        canvas2.create_window(-26, 90, anchor="w", window=boton)
        boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_Grupos(ventanaPrincipal))
        canvas2.create_window(-61, 120, anchor="w", window=boton2)
        boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_Grupos(ventanaPrincipal))
        canvas2.create_window(-53, 150, anchor="w", window=boton3)
        boton4 = tk.Button(canvas2, text="Modificación", width=121, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificaciones_Grupos(ventanaPrincipal))
        canvas2.create_window(-7, 180, anchor="w", window=boton4)
        boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_Grupos(ventanaPrincipal))
        canvas2.create_window(-28, 210, anchor="w", window=boton6)
        boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
        canvas2.create_window(-6, 385, anchor="w", window=boton5)
        
        # Agregar la imagen
        imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
        imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
        label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
        label_imagen.place(x=530, y=0)

        preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
        preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

        ventanaPrincipal.mainloop()

      # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
   
    def mostrar_ventanaModificacionAlumno_Grupo(ventanaPrincipal):
    
        def mostrar_ventanaAltas_alumno(ventanaPrincipal):

            global entry_nombre
            global entry_genero

            ventanaPrincipal.title("Altas de alumnos a grupos")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Asignar alumno a grupo", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label2 = tk.Label(ventanaPrincipal, text="Número de cuenta del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
            usuario_labelG = tk.Label(ventanaPrincipal, text="Id del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")

            entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre.place(relx=0.7, rely=0.35, anchor="w")
            entry_genero = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_genero.place(relx=0.7, rely=0.42, anchor="w")
            
            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def pasar_datos_de_base_de_datos():
            
            global entry_nombre
            global entry_genero

            try:
                nombre = entry_nombre.get()
                genero = entry_genero.get()
                
                if entry_nombre is None or len(entry_nombre.get()) < 1:
                    messagebox.showerror("Alumno", "Número de cuenta inválido!")
                    return
                
                if entry_genero is None or len(entry_genero.get()) < 1:
                    messagebox.showerror("Alumno", "Id inválido!")
                    return
                
                if CAlumno.validacion_alumno(nombre) is None:
                    messagebox.showerror("Alumno", "Número de cuenta inválido!")
                    return
                
                if CAlumno.validacion_Grupo_repetido(genero, nombre):
                    messagebox.showerror("Alumno", "Registro repetido!")
                    return
                # Si el alumno existe, ingresar los datos del alumno
                CAlumno.darAltaAlumno_Grupo(nombre, genero)   
                messagebox.showinfo("Información", "Alumno agregado al grupo correctamente")
                entry_nombre.delete(0, 'end')
                entry_genero.delete(0, 'end')
                
            except mysql.connector.Error as error:
                print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos: {}".format(error))

        def mostrar_ventanaBajas_alumno(ventanaPrincipal):

            ventanaPrincipal.title("Bajas de alumnos")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar alumno", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Número de cuenta del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Id del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.44, anchor="w")

            entry_numCuenta = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre.place(relx=0.7, rely=0.44, anchor="w")
            
            def eliminar_alumno():
                try:
                    numCuenta = entry_numCuenta.get()
                    idGrupo = entry_nombre.get()

                    if idGrupo is None or len(entry_nombre.get()) < 1:
                        messagebox.showerror("Alumno", "Id inválido!")
                        return
                    
                    if not numCuenta or len(numCuenta) < 1:
                        messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                        entry_numCuenta.delete(0, 'end')
                        entry_nombre.delete(0, 'end')
                        return
                    
                    if CAlumno.validacion_Grupo_repetido(idGrupo, numCuenta) == None:
                        messagebox.showerror("Alumno", "Registro no encontrado!")
                        return
                
                    # Si todos los datos son válidos, ingresar el alumno
                    

                    if CAlumno.validacion_alumno(numCuenta) == None:
                        messagebox.showerror("Alumno", "¡Número de cuenta no encontrado!")
                        entry_numCuenta.delete(0, 'end')
                        return
                    CAlumno.darBajaAlumno_Grupo(idGrupo, numCuenta)
                    messagebox.showinfo("Info", "Alumno eliminado exitosamente")
                    entry_numCuenta.delete(0, 'end')
                    entry_nombre.delete(0, 'end')
                
                except ValueError as error:
                    print("Error al ingresar datos en Bajas de alumnos {}".format(error))


            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
            
            
            ventanaPrincipal.mainloop()

        def mostrar_ventanaConsultas_alumno(ventanaPrincipal):
            
            def mostrarMateriaBusqueda():
                global entry_numCuenta_GRUPO
                idGrupo = entry_numCuenta_GRUPO.get()  
                tree = ttk.Treeview(groupBox, columns=("Id de grupo", "NC de alumno", "Nombre del alumno"), show='headings',height=5)
                tree.grid(row=0, column=0, sticky="nsew")

                # Configurar scrollbar horizontal
                scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")
                tree.configure(xscrollcommand=scroll_x.set)

                # Configurar scrollbar vertical
                scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")
                tree.configure(yscrollcommand=scroll_y.set)
                tree.configure(height=11)
                tree.column("#1", anchor="center", width=120)
                tree.heading("#1", text="Id de grupo")
                tree.column("#2", anchor="center", width=120)
                tree.heading("#2", text="NC de alumno")
                tree.column("#3", anchor="center", width=200)
                tree.heading("#3", text="Nombre del alumno")
                print(idGrupo)
                for row in CAlumno.mostrarGrupo_Alumno_Grupo(idGrupo):
                    tree.insert("", "end", values=row)


                # Función para mostrar la información completa al hacer doble clic en una fila
                def mostrar_info_completa(event):
                    item = tree.item(tree.selection())
                    values = item['values']
                    messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))
                
                # Vincular evento de doble clic a la función mostrar_info_completa
                tree.bind("<Double-1>", mostrar_info_completa)

            global entry_numCuenta_GRUPO
            ventanaPrincipal.title("Consultas de Grupos")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los Grupos", padx=0, pady=1, bg="white")
            groupBox.place(relx=0.615, rely=0.65, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.30, rely=0.225, anchor="w")
            entry_numCuenta_GRUPO = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_GRUPO.place(relx=0.50, rely=0.225, anchor="w")

            tree = ttk.Treeview(groupBox, columns=("Id de grupo", "NC de alumno","Nombre del alumno"), show='headings',height=5)
            tree.grid(row=0, column=0, sticky="nsew")

            # Configurar scrollbar horizontal
            scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")
            tree.configure(xscrollcommand=scroll_x.set)

            # Configurar scrollbar vertical
            scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=scroll_y.set)
            tree.configure(height=11)
            tree.column("#1", anchor="center", width=120)
            tree.heading("#1", text="Id de grupo")
            tree.column("#2", anchor="center", width=120)
            tree.heading("#2", text="NC de alumno")
            tree.column("#3", anchor="center", width=200)
            tree.heading("#3", text="Nombre del alumno")

            for row in CAlumno.mostrarAlumno_Grupo():
                tree.insert("","end", values=row)

            
            # Función para mostrar la información completa al hacer doble clic en una fila
            def mostrar_info_completa(event):
                item = tree.item(tree.selection())
                values = item['values']
                messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

            # Vincular evento de doble clic a la función mostrar_info_completa
            tree.bind("<Double-1>", mostrar_info_completa)

            boton_aceptar = tk.Button(ventanaPrincipal, text="Buscar", width=8, bg=color_hex2, fg="white", font=("Helvetica", 9, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=mostrarMateriaBusqueda)
            boton_aceptar.place(relx=0.80, rely=0.225, anchor="center")

            ventanaPrincipal.mainloop()

        def mostrar_lista_alumnos(ventanaPrincipal):
            ventanaPrincipal.title("Consultas de alumnos")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los alumnos", padx=0, pady=1, bg="white")
            groupBox.place(relx=0.615, rely=0.58, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

            tree = ttk.Treeview(groupBox, columns=("Nombre", "Género", "Nacionalidad", "CURP", "Fecha Nac", "NC"), show='headings',height=5)
            tree.grid(row=0, column=0, sticky="nsew")

            # Configurar scrollbar horizontal
            scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")
            tree.configure(xscrollcommand=scroll_x.set)

            # Configurar scrollbar vertical
            scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=scroll_y.set)
            tree.configure(height=14)
            tree.column("#1", anchor="center", width=110)
            tree.heading("#1", text="Nombre")
            tree.column("#2", anchor="center", width=50)
            tree.heading("#2", text="Género")
            tree.column("#3", anchor="center", width=80)
            tree.heading("#3", text="Nacionalidad")
            tree.column("#4", anchor="center", width=70)
            tree.heading("#4", text="CURP")
            tree.column("#5", anchor="center", width=70)
            tree.heading("#5", text="Fecha Nac")
            tree.column("#6", anchor="center", width=60)
            tree.heading("#6", text="NC")

            for row in CAlumno.mostrarAlumno():
                tree.insert("","end", values=row)

            
            # Función para mostrar la información completa al hacer doble clic en una fila
            def mostrar_info_completa(event):
                item = tree.item(tree.selection())
                values = item['values']
                messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

            # Vincular evento de doble clic a la función mostrar_info_completa
            tree.bind("<Double-1>", mostrar_info_completa)

            ventanaPrincipal.mainloop()

        
        #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.title("Modificación de alumnos")
        
        imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil
        icono_perfil = ImageTk.PhotoImage(imagen_perfil)

        imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil2
        icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

        imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil3
        icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

        imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil4
        icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

        imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil5
        icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

        imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil6
        icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

        imagen_perfil7 = Image.open("Imagenes\\lista.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil7 = imagen_perfil7.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil7
        icono_perfil7 = ImageTk.PhotoImage(imagen_perfil7)

        # Centrar la nueva ventanaInicioSesion en la pantalla
        ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
        altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
        x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
        y_pos = int((altura_ventanaInicioSesion - 400) / 2)
        ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

        # Crear el canvas para la nueva ventanaInicioSesion
        canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
        canvas2.pack()
        canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
        canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
        canvas2.place(x=0, y=0)

        #Botones
        boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPrincipal_profesor(ventanaPrincipal))
        canvas2.create_window(-26, 90, anchor="w", window=boton)
        boton2 = tk.Button(canvas2, text="Alta grupo", width=130, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_alumno(ventanaPrincipal))
        canvas2.create_window(-18, 120, anchor="w", window=boton2)
        boton3 = tk.Button(canvas2, text="Baja grupo", width=128, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_alumno(ventanaPrincipal))
        canvas2.create_window(-15, 150, anchor="w", window=boton3)
        boton4 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_alumno(ventanaPrincipal))
        canvas2.create_window(-28, 180, anchor="w", window=boton4)
        boton6 = tk.Button(canvas2, text="Lista alumnos", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil7, compound=tk.LEFT, padx=10, command=lambda: mostrar_lista_alumnos(ventanaPrincipal))
        canvas2.create_window(-6, 210, anchor="w", window=boton6)
        boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
        canvas2.create_window(-6, 385, anchor="w", window=boton5)
        
        # Agregar la imagen
        imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
        imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
        label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
        label_imagen.place(x=530, y=0)

        preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
        preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

        ventanaPrincipal.mainloop()

    def mostrar_ventanaModificacionCalif(ventanaPrincipal):
    
        def mostrar_ventanaAltas_Calif(ventanaPrincipal):

            global entry_nombre
            global entry_genero
            global entry_calif

            ventanaPrincipal.title("Alta de calificación")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Asignar calificación a alumno", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label2 = tk.Label(ventanaPrincipal, text="Número de cuenta del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.35, anchor="w")
            usuario_labelG = tk.Label(ventanaPrincipal, text="Id del grupo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelG.place(relx=0.3, rely=0.42, anchor="w")
            usuario_labelC = tk.Label(ventanaPrincipal, text="Calificación: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_labelC.place(relx=0.3, rely=0.49, anchor="w")

            entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre.place(relx=0.7, rely=0.35, anchor="w")
            entry_genero = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_genero.place(relx=0.7, rely=0.42, anchor="w")
            entry_calif = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_calif.place(relx=0.7, rely=0.49, anchor="w")
            
            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=pasar_datos_de_base_de_datos_Calif)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")

            ventanaPrincipal.mainloop()

        def pasar_datos_de_base_de_datos_Calif():
            global entry_nombre
            global entry_genero
            global entry_calif

            try:
                nombre = entry_nombre.get()
                genero = entry_genero.get()
                calif_str = entry_calif.get()

                if not nombre:
                    messagebox.showerror("Alumno", "¡Nombre inválido!")
                    return

                if not CAlumno.validacion_alumno(nombre):
                    messagebox.showerror("Alumno", "¡Nombre inválido!")
                    return
                
                if CCalificacion.validacion_Calif(genero, nombre):
                    messagebox.showerror("Calificación", "¡Ese alumno ya tiene calificación!")
                    entry_nombre.delete(0, 'end')
                    entry_genero.delete(0, 'end')
                    return
                
                try:
                    calif = float(calif_str)
                except ValueError:
                    messagebox.showerror("Calificación", "¡Calificación debe ser un número!")
                    return

                if calif < 0.1 or calif > 10.0:
                    messagebox.showerror("Calificación", "¡Calificación inválida!")
                    return

                # Si todos los datos son válidos, ingresar el alumno
                CCalificacion.ingresarCalif(genero, nombre, calif)
                messagebox.showinfo("Info", "Datos guardados correctamente")
                entry_nombre.delete(0, 'end')
                entry_genero.delete(0, 'end')
                entry_calif.delete(0, 'end')

            except ValueError as error:
                print("Error al ingresar datos del alumno en la función pasar_datos_de_base_de_datos_Calif: {}".format(error))

        def mostrar_ventanaBajas_Calif(ventanaPrincipal):

            ventanaPrincipal.title("Bajas de calificaciones")
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            texto_inicio_sesion = tk.Label(ventanaPrincipal, text="Eliminar calificación", font=("Helvetica", 16, "bold"), bg="white")
            texto_inicio_sesion.place(relx=0.6, rely=0.25, anchor="center")

            usuario_label7 = tk.Label(ventanaPrincipal, text="Id de la calificación: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.3, rely=0.37, anchor="w")
            usuario_label2 = tk.Label(ventanaPrincipal, text="Usuario administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label2.place(relx=0.3, rely=0.50, anchor="w")
            usuario_label3 = tk.Label(ventanaPrincipal, text="Contraseña de administrativo: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label3.place(relx=0.3, rely=0.57, anchor="w")

            entry_numCuenta = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta.place(relx=0.7, rely=0.37, anchor="w")
            entry_nombre = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_nombre.place(relx=0.7, rely=0.50, anchor="w")
            entry_CURP = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid", show="*")
            entry_CURP.place(relx=0.7, rely=0.57, anchor="w")
            
            def eliminar_alumno():
                try:
                    numCuenta = entry_numCuenta.get()

                    if not numCuenta or len(numCuenta) < 1:
                        messagebox.showerror("Alumno", "¡ID no encontrado!")
                        entry_nombre.delete(0, 'end')
                        return
                    
                    
                    # Si todos los datos son válidos, ingresar el alumno
                    cursorRowCount = CCalificacion.borrarCalifPorID(numCuenta)

                    if cursorRowCount == 0:
                        messagebox.showerror("Alumno", "¡ID no encontrado!")
                        entry_numCuenta.delete(0, 'end')
                        return
                    messagebox.showinfo("Info", "Alumno eliminado exitosamente")
                    entry_numCuenta.delete(0, 'end')
                
                except ValueError as error:
                    print("Error al ingresar datos en Bajas de alumnos {}".format(error))

            boton_aceptar = tk.Button(ventanaPrincipal, text="Aceptar", width=47, bg=color_hex2, fg="white", font=("Helvetica", 10, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=eliminar_alumno)
            boton_aceptar.place(relx=0.625, rely=0.9, anchor="center")
            
            
            ventanaPrincipal.mainloop()

        def mostrar_ventanaConsultas_Calif(ventanaPrincipal):
            
            def mostrarMateriaBusqueda():
                global entry_numCuenta_GRUPO
                idGrupo = entry_numCuenta_GRUPO.get()  
                tree = ttk.Treeview(groupBox, columns=("ID Calificación", "Materia", "NC Alumno","Nombre alumno", "Calificacion"), show='headings',height=5)
                tree.grid(row=0, column=0, sticky="nsew")

                # Configurar scrollbar horizontal
                scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
                scroll_x.grid(row=1, column=0, sticky="ew")
                tree.configure(xscrollcommand=scroll_x.set)

                # Configurar scrollbar vertical
                scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
                scroll_y.grid(row=0, column=1, sticky="ns")
                tree.configure(yscrollcommand=scroll_y.set)
                tree.configure(height=11)
                tree.column("#1", anchor="center", width=80)
                tree.heading("#1", text="ID Calificacion")
                tree.column("#2", anchor="center", width=100)
                tree.heading("#2", text="Materia")
                tree.column("#3", anchor="center", width=80)
                tree.heading("#3", text="NC del alumno")
                tree.column("#4", anchor="center", width=100)
                tree.heading("#4", text="Nombre del alumno")
                tree.column("#5", anchor="center", width=80)
                tree.heading("#5", text="Calificacion")
                for row in CCalificacion.buscarCalifPorID(idGrupo):
                    tree.insert("", "end", values=row)


                # Función para mostrar la información completa al hacer doble clic en una fila
                def mostrar_info_completa(event):
                    item = tree.item(tree.selection())
                    values = item['values']
                    messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))
                
                # Vincular evento de doble clic a la función mostrar_info_completa
                tree.bind("<Double-1>", mostrar_info_completa)

            global entry_numCuenta_GRUPO
            ventanaPrincipal.title("Consultas de Grupos")
            
            # Crear el rectángulo
            rectangulo = tk.Frame(ventanaPrincipal, width=500, height=400, bg="white")
            rectangulo.place(relx=0.644, rely=0.651, anchor="center")

            groupBox = tk.LabelFrame(ventanaPrincipal, text="Datos de los Grupos", padx=0, pady=1, bg="white")
            groupBox.place(relx=0.615, rely=0.65, anchor="center")  # Ajustado para colocar correctamente el LabelFrame

            usuario_label7 = tk.Label(ventanaPrincipal, text="NC del alumno: ", font=("Helvetica", 10, "bold"), fg="black", bg="white")
            usuario_label7.place(relx=0.30, rely=0.225, anchor="w")
            entry_numCuenta_GRUPO = tk.Entry(ventanaPrincipal, font=("Helvetica", 10), bd=1, relief="solid")
            entry_numCuenta_GRUPO.place(relx=0.50, rely=0.225, anchor="w")

            tree = ttk.Treeview(groupBox, columns=("ID Calificación", "ID Materia", "NC Alumno","Nombre alumno", "Calificacion"), show='headings',height=5)
            tree.grid(row=0, column=0, sticky="nsew")

            # Configurar scrollbar horizontal
            scroll_x = ttk.Scrollbar(groupBox, orient="horizontal", command=tree.xview)
            scroll_x.grid(row=1, column=0, sticky="ew")
            tree.configure(xscrollcommand=scroll_x.set)

            # Configurar scrollbar vertical
            scroll_y = ttk.Scrollbar(groupBox, orient="vertical", command=tree.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            tree.configure(yscrollcommand=scroll_y.set)
            tree.configure(height=11)
            tree.column("#1", anchor="center", width=80)
            tree.heading("#1", text="ID Calificacion")
            tree.column("#2", anchor="center", width=100)
            tree.heading("#2", text="ID Materia")
            tree.column("#3", anchor="center", width=80)
            tree.heading("#3", text="NC del alumno")
            tree.column("#4", anchor="center", width=100)
            tree.heading("#4", text="Nombre del alumno")
            tree.column("#5", anchor="center", width=80)
            tree.heading("#5", text="Calificacion")

            for row in CCalificacion.mostrarCalif():
                tree.insert("","end", values=row)

            
            # Función para mostrar la información completa al hacer doble clic en una fila
            def mostrar_info_completa(event):
                item = tree.item(tree.selection())
                values = item['values']
                messagebox.showinfo("Información específica", "\n".join([f"{key}: {value}" for key, value in zip(tree['columns'], values)]))

            # Vincular evento de doble clic a la función mostrar_info_completa
            tree.bind("<Double-1>", mostrar_info_completa)

            boton_aceptar = tk.Button(ventanaPrincipal, text="Buscar", width=8, bg=color_hex2, fg="white", font=("Helvetica", 9, "bold"), activebackground=color_hex3, bd=0, activeforeground="white", command=mostrarMateriaBusqueda)
            boton_aceptar.place(relx=0.80, rely=0.225, anchor="center")

            ventanaPrincipal.mainloop()
        

        #ventanaPrincipal = tk.Tk()  # Usamos Toplevel para crear una nueva ventanaInicioSesion dentro de la misma aplicación
        ventanaPrincipal.title("Modificación de calificaciones")
        
        imagen_perfil = Image.open("Imagenes\\icono_regreso.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil
        icono_perfil = ImageTk.PhotoImage(imagen_perfil)

        imagen_perfil2 = Image.open("Imagenes\\icono2_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil2 = imagen_perfil2.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil2
        icono_perfil2 = ImageTk.PhotoImage(imagen_perfil2)

        imagen_perfil3 = Image.open("Imagenes\\icono3_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil3
        icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

        imagen_perfil4 = Image.open("Imagenes\\icono4_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil4
        icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

        imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil5
        icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

        imagen_perfil6 = Image.open("Imagenes\\icono6_2.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
        imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
        # Crear un objeto PhotoImage
        global icono_perfil6
        icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

        # Centrar la nueva ventanaInicioSesion en la pantalla
        ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
        altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
        x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
        y_pos = int((altura_ventanaInicioSesion - 400) / 2)
        ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

        # Crear el canvas para la nueva ventanaInicioSesion
        canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
        canvas2.pack()
        canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
        canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
        canvas2.place(x=0, y=0)

        #Botones
        boton = tk.Button(canvas2, text="Regresar", width=140, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPrincipal_profesor(ventanaPrincipal))
        canvas2.create_window(-26, 90, anchor="w", window=boton)
        boton2 = tk.Button(canvas2, text="Altas", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil2, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaAltas_Calif(ventanaPrincipal))
        canvas2.create_window(-61, 120, anchor="w", window=boton2)
        boton3 = tk.Button(canvas2, text="Bajas", width=167, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaBajas_Calif(ventanaPrincipal))
        canvas2.create_window(-53, 150, anchor="w", window=boton3)
        boton6 = tk.Button(canvas2, text="Consultas", width=142, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaConsultas_Calif(ventanaPrincipal))
        canvas2.create_window(-28, 180, anchor="w", window=boton6)
        boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
        canvas2.create_window(-6, 385, anchor="w", window=boton5)
        
        # Agregar la imagen
        imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
        imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
        label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
        label_imagen.place(x=530, y=0)

        preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
        preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

        ventanaPrincipal.mainloop()

    
    global entry_nombre
    global entry_genero
    ventanaPrincipal.resizable(False, False)  # Bloquear la opción de maximizar
    ventanaPrincipal.title("Menú Principal")

    
    imagen_perfil = Image.open("Imagenes\\icono1.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil = imagen_perfil.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil
    icono_perfil = ImageTk.PhotoImage(imagen_perfil)

    imagen_perfil3 = Image.open("Imagenes\\icono3_3.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil3 = imagen_perfil3.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil3
    icono_perfil3 = ImageTk.PhotoImage(imagen_perfil3)

    imagen_perfil4 = Image.open("Imagenes\\grupo.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil4 = imagen_perfil4.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil4
    icono_perfil4 = ImageTk.PhotoImage(imagen_perfil4)

    imagen_perfil6 = Image.open("Imagenes\\config_alumno.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil6 = imagen_perfil6.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil6
    icono_perfil6 = ImageTk.PhotoImage(imagen_perfil6)

    imagen_perfil5 = Image.open("Imagenes\\icono5.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil5 = imagen_perfil5.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil5
    icono_perfil5 = ImageTk.PhotoImage(imagen_perfil5)

    imagen_perfil7 = Image.open("Imagenes\\materia.png")  # Reemplaza "perfil.png" con la ruta de tu imagen
    imagen_perfil7 = imagen_perfil7.resize((15, 15))  # Ajusta el tamaño según sea necesario
    # Crear un objeto PhotoImage
    global icono_perfil7
    icono_perfil7 = ImageTk.PhotoImage(imagen_perfil7)


    # Centrar la nueva ventanaInicioSesion en la pantalla
    ancho_ventanaInicioSesion = ventanaPrincipal.winfo_screenwidth()
    altura_ventanaInicioSesion = ventanaPrincipal.winfo_screenheight()
    x_pos = int((ancho_ventanaInicioSesion - 600) / 2)
    y_pos = int((altura_ventanaInicioSesion - 400) / 2)
    ventanaPrincipal.geometry(f"600x400+{x_pos}+{y_pos}")

    # Crear el canvas para la nueva ventanaInicioSesion
    canvas2 = tk.Canvas(ventanaPrincipal, width=ancho_ventanaInicioSesion, height=altura_ventanaInicioSesion, borderwidth=0, highlightthickness=0)
    canvas2.pack()
    canvas2.create_rectangle(0, 0, ancho_ventanaInicioSesion, 60, fill=color_hex2, outline="")
    canvas2.create_rectangle(0, altura_ventanaInicioSesion, 136, 60, fill=color_hex1, outline="")
    canvas2.place(x=0, y=0)
    #Botones
    boton = tk.Button(canvas2, text="Perfil", width=175, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaPerfil_profesor(ventanaPrincipal))
    canvas2.create_window(-61, 90, anchor="w", window=boton)
    boton4 = tk.Button(canvas2, text="Materia", width=158, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil7, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionMateria(ventanaPrincipal))
    canvas2.create_window(-46, 120, anchor="w", window=boton4)
    boton6 = tk.Button(canvas2, text="Grupos", width=158, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil4, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionGrupos(ventanaPrincipal))
    canvas2.create_window(-45, 150, anchor="w", window=boton6)
    boton7 = tk.Button(canvas2, text="Alumnos", width=152, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil6, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionAlumno_Grupo(ventanaPrincipal))
    canvas2.create_window(-38, 180, anchor="w", window=boton7)
    boton3 = tk.Button(canvas2, text="Calificacion", width=128, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil3, compound=tk.LEFT, padx=10, command=lambda: mostrar_ventanaModificacionCalif(ventanaPrincipal))
    canvas2.create_window(-14, 210, anchor="w", window=boton3)
    boton5 = tk.Button(canvas2, text="Cerrar Sesión", width=120, bg=color_hex1, fg="white", bd=0, font=("Helvetica", 12, "bold"), activebackground=color_hex3, activeforeground="white", image=icono_perfil5, compound=tk.LEFT, padx=10, command=lambda: destruye_ventanaPrincipal(ventanaPrincipal))
    canvas2.create_window(-6, 385, anchor="w", window=boton5)
    
    # Agregar la imagen
    imagen = Image.open(r"Imagenes\\LogoPAET_color.jpg")
    imagen = imagen.resize((50, 55))  # Ajustar el tamaño de la imagen si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear un widget Label para mostrar la imagen y superponerlo sobre los demás widgets
    label_imagen = tk.Label(ventanaPrincipal, image=imagen_tk, borderwidth=0, highlightthickness=0)
    label_imagen.place(x=530, y=0)

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaPrincipal, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")

    ventanaPrincipal.mainloop()

def borrar_texto(event):
    # Borra el texto actual en el cuadro de texto cuando se obtiene el foco
    if event.widget.get() == event.widget.placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black")  # Cambia el color del texto a negro

def restaurar_texto(event):
    # Restaura el texto predeterminado si el cuadro de texto está vacío al perder el foco
    if not event.widget.get():
        event.widget.insert(0, event.widget.placeholder)
        event.widget.config(fg="grey")  # Cambia el color del texto a gris

def on_enter(event, olvide_contrasena_label):
    olvide_contrasena_label.config(fg="blue")

def on_leave(event, olvide_contrasena_label):
    olvide_contrasena_label.config(fg="black")

def on_enter_Registrarse(event, registrarse_due):
    registrarse_due.config(fg=color_hex3)

def on_leave_Registrarse(event, registrarse_due):
    registrarse_due.config(fg="white")

def crear_widgets(ventanaInicioSesion):
    # Crear los widgets
    texto_inicio_sesion = tk.Label(ventanaInicioSesion, text="Iniciar sesión", font=("Helvetica", 16, "bold"))
    usuario_entry = tk.Entry(ventanaInicioSesion, fg="grey", width=40, font=("Helvetica", 10))  # Ajusta el ancho y la altura aquí
    contrasena_entry = tk.Entry(ventanaInicioSesion, show="*", fg="grey", width=40, font=("Helvetica", 10))  # Ajusta el ancho y la altura aquí

    # Configurar el texto predeterminado y eventos para el cuadro de usuario
    usuario_entry.placeholder = "000000"
    usuario_entry.insert(0, usuario_entry.placeholder)
    usuario_entry.bind("<FocusIn>", borrar_texto)
    usuario_entry.bind("<FocusOut>", restaurar_texto)

    # Configurar el texto predeterminado y eventos para el cuadro de contraseña
    contrasena_entry.placeholder = "Contraseña"
    contrasena_entry.insert(0, contrasena_entry.placeholder)
    contrasena_entry.bind("<FocusIn>", borrar_texto)
    contrasena_entry.bind("<FocusOut>", restaurar_texto)

    # Añadir un widget Label para el texto "Olvidé mi contraseña"
    olvide_contrasena_label = tk.Label(ventanaInicioSesion, text="¿Olvidaste tu contraseña?", font=("Helvetica", 10, "italic"), fg="black")

    preparatoria_autonoma_de_toluca_label = tk.Label(ventanaInicioSesion, text="Preparatoria \nAutónoma de \nToluca", font=("Helvetica", 9, "bold"), fg="white", bg=color_hex2, justify="left")
    
    usuario_label = tk.Label(ventanaInicioSesion, text="Número de cuenta", font=("Helvetica", 10, "bold"), fg="black")
    
    contrasenia_label = tk.Label(ventanaInicioSesion, text="Contraseña", font=("Helvetica", 10, "bold"), fg="black")

    iniciar_sesion_due = tk.Label(ventanaInicioSesion, text="Iniciar Sesión", font=("Helvetica", 10, "bold", "underline"), fg="white", underline=0, bg= color_hex1)
    
    registrarse_due = tk.Label(ventanaInicioSesion, text="Registrarse", font=("Helvetica", 10, "bold"), fg="white", bg= color_hex1)

    pie_pagina = tk.Label(ventanaInicioSesion, 
                          text="Universidad PAET\nBoulevard Toluca Metepec Norte #814, Col. Hípico, C.P. 52156. Metepec, México.\nTel: +52 (722) 3774311 Lada sin costo: 01 800 436 48 37 Correo: PAETOficial@gmail.com", 
                          font=("Helvetica", 6, "bold"), 
                          fg="white",
                          bg=color_hex1)

    iniciar_sesion_button = tk.Button(ventanaInicioSesion, text="Aceptar", command=lambda: iniciar_sesion(usuario_entry, contrasena_entry, ventanaInicioSesion), width=40, bg=color_hex1, fg="white", font=("Helvetica", 9, "bold"))

    return texto_inicio_sesion, usuario_entry, contrasena_entry, olvide_contrasena_label, preparatoria_autonoma_de_toluca_label, usuario_label, contrasenia_label, iniciar_sesion_due, registrarse_due, pie_pagina, iniciar_sesion_button

def configurar_eventos(olvide_contrasena_label, registrarse_due):
    # Configurar eventos para cambiar el color del texto al pasar el ratón sobre él
    olvide_contrasena_label.bind("<Enter>", lambda event: on_enter(event, olvide_contrasena_label))
    olvide_contrasena_label.bind("<Leave>", lambda event: on_leave(event, olvide_contrasena_label))

    registrarse_due.bind("<Enter>", lambda event: on_enter_Registrarse(event, registrarse_due))
    registrarse_due.bind("<Leave>", lambda event: on_leave_Registrarse(event, registrarse_due))

def colocar_widgets(texto_inicio_sesion, iniciar_sesion_due, registrarse_due, usuario_entry, contrasena_entry, iniciar_sesion_button, olvide_contrasena_label, preparatoria_autonoma_de_toluca_label, usuario_label, contrasenia_label, pie_pagina):
    # Posicionar los widgets en la ventanaInicioSesion usando place
    texto_inicio_sesion.place(relx=0.5, rely=0.33, anchor="center")
    iniciar_sesion_due.place(relx=0.75, rely=0.19, anchor="center")
    registrarse_due.place(relx=0.91, rely=0.19, anchor="center")
    usuario_entry.place(relx=0.5, rely=0.47, anchor="center")
    contrasena_entry.place(relx=0.5, rely=0.60, anchor="center")
    iniciar_sesion_button.place(relx=0.5, rely=0.78, anchor="center")
    olvide_contrasena_label.place(relx=0.39, rely=0.70, anchor="center")
    preparatoria_autonoma_de_toluca_label.place(relx=0.08, rely=0.07, anchor="center")
    usuario_label.place(relx=0.365, rely=0.41, anchor="center")
    contrasenia_label.place(relx=0.33, rely=0.54, anchor="center")
    pie_pagina.place(relx=0.5, rely=0.95, anchor="center")

def destruye_ventanaPrincipal(mostrar_ventanaPrincipal):
    mostrar_ventanaPrincipal.destroy()
    mostrar_inicio_sesion()
    pass

def main():
    #mostrar_ventanaModificacionAlumno()
    mostrar_inicio_sesion()
    
if __name__ == "__main__":
    color_hex1 = '#{:02x}{:02x}{:02x}'.format(235, 113, 36)
    color_hex2 = '#{:02x}{:02x}{:02x}'.format(235, 75, 33)
    color_hex3 = '#{:02x}{:02x}{:02x}'.format(235, 36, 203)

    global entry_nombre
    entry_nombre = None
    global entry_CURP
    entry_CURP = None
    global entry_FechaNac
    entry_FechaNac = None
    global entry_numCuenta
    entry_numCuenta = None
    global genero_seleccionado
    genero_seleccionado = None
    global nacionalidad_seleccionada
    nacionalidad_seleccionada = None

    global entry_nombre_admin
    entry_nombre_admin=None
    global entry_CURP_admin
    entry_CURP_admin=None
    global entry_FechaNac_admin
    entry_FechaNac_admin=None
    global entry_numCuenta_admin
    entry_numCuenta_admin=None
    global genero_seleccionado_admin
    genero_seleccionado_admin=None
    global nacionalidad_seleccionada_admin
    nacionalidad_seleccionada_admin=None

    global usuarioGeneral
    usuarioGeneral = None

    global contrasena_alumno
    contrasena_alumno = None
    global contrasena_profesor
    contrasena_profesor = None
    global contrasena_administrador
    contrasena_administrador = None

    global entry_nombre_grupo
    entry_nombre_grupo = None
    
    global entry_nombre_materia
    entry_nombre_materia = None
    global hora_inicio
    hora_inicio = None
    global hora_fin
    hora_fin = None
    global dia_clase
    dia_clase = None

    global entry_numCuenta_GRUPO
    entry_numCuenta_GRUPO = None

    global entry_genero
    entry_genero = None

    global entry_calif
    entry_calif = None

    global tree
    tree = None

    main()


