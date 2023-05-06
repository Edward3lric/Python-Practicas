import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.pelicula_dao import crear_tabla, eliminar_tabla, agregar_pelicula, listar, editar, eliminar

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        # self.config( bg="sky blue")
        self.id_pelicula = None

        self.campos_de_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    def campos_de_pelicula(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text = "Nombre: ")
        self.label_nombre.config(font= ("Arial", 12, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text = "Duración: ")
        self.label_duracion.config(font= ("Arial", 12, "bold"))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text = "Genero: ")
        self.label_genero.config(font= ("Arial", 12, "bold"))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        # Entrys de cada campo
        self.in_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.in_nombre)
        self.entry_nombre.config(width = 50, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.in_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.in_duracion)
        self.entry_duracion.config(width = 50, font=("Arial", 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.in_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.in_genero)
        self.entry_genero.config(width = 50, font=("Arial", 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Botones
        self.boton_nuevo = tk.Button(self, text="Nuevo", command = self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=("Arial", 12), fg="white", bg="#07552e", cursor="hand2",
                                activebackground="#07552e", activeforeground="white")
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command = self.guardar_datos)
        self.boton_guardar.config(width=20, font=("Arial", 12), fg="white", bg="#163558", cursor="hand2",
                                activebackground="#163558", activeforeground="white")
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command = self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=("Arial", 12), fg="white", bg="#d04500", cursor="hand2",
                                activebackground="#d04500", activeforeground="white")
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.in_nombre.set("")
        self.in_duracion.set("")
        self.in_genero.set("")

        self.entry_nombre.config(state = "normal")
        self.entry_duracion.config(state = "normal")
        self.entry_genero.config(state = "normal")

        self.boton_guardar.config(state = "normal")
        self.boton_cancelar.config(state = "normal")

    def deshabilitar_campos(self):
        self.id_pelicula = None
        
        self.in_nombre.set("")
        self.in_duracion.set("")
        self.in_genero.set("")

        self.entry_nombre.config(state = "disable")
        self.entry_duracion.config(state = "disable")
        self.entry_genero.config(state = "disable")

        self.boton_guardar.config(state = "disable")
        self.boton_cancelar.config(state = "disable")
    
    def guardar_datos(self):
        nombre = self.in_nombre.get()
        duracion = self.in_duracion.get()
        genero = self.in_genero.get()

        if self.id_pelicula:
            editar(nombre, duracion, genero, self.id_pelicula)
        else:
            agregar_pelicula(nombre, duracion, genero)

        self.deshabilitar_campos()
        self.tabla_peliculas()

    def tabla_peliculas(self):
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()

        self.tabla = ttk.Treeview(self, columns=("Nombre", "Duración", "Genero"))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky="nse")

        # Scrollbar para la tabla si exede 10 registros
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row = 4, column = 4, sticky= "nse") 
        self.tabla.config(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="Id")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Duración")
        self.tabla.heading("#3", text="Genero")

        for pelicula in self.lista_peliculas:
            self.tabla.insert("", 0, text=pelicula[0], values= (pelicula[1], pelicula[2], pelicula[3]))

        # Boton de editar
        self.boton_editar = tk.Button(self, text="Editar", command = self.editar_datos)
        self.boton_editar.config(width=20, font=("Arial", 12), fg="white", bg="#07552e", cursor="hand2",
                                activebackground="#07552e", activeforeground="white")
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        # Boton de eliminar
        self.boton_eliminar = tk.Button(self, text="Eliminar", command = self.eliminar_datos)
        self.boton_eliminar.config(width=20, font=("Arial", 12), fg="white", bg="#d04500", cursor="hand2",
                                activebackground="#d04500", activeforeground="white")
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    
    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())["values"][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())["values"][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())["values"][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)

        except Exception as error:
            titulo = "Seleccion registro Editar"
            mensaje = f"Error: {error}"
            messagebox.showinfo(titulo, mensaje)

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())["text"]
            eliminar(self.id_pelicula)
            self.tabla_peliculas()
            self.id_pelicula = None

        except Exception as error:
            titulo = "Seleccion registro Eliminar"
            mensaje = f"Error: {error}"
            messagebox.showinfo(titulo, mensaje)

class limpiar():
    def __init__(self, app):
        self.app = app

    def borrar_tabla(self):
        eliminar_tabla()
        self.app.tabla_peliculas()
        

def barra_menu(root, limpiar):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

    menu_inicio.add_command(label = "Crear Registro en DB", command = crear_tabla)
    menu_inicio.add_command(label = "Eliminar Registro en DB", command = limpiar.borrar_tabla)
    menu_inicio.add_command(label = "Salir", command = root.destroy)

    barra_menu.add_cascade(label = "Consultas")
    barra_menu.add_cascade(label = "Configuraciòn")
    barra_menu.add_cascade(label = "Ayuda")

