from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = """
    CREATE TABLE peliculas(
        id_pelicula INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        duracion REAL NOT NULL,
        genero TEXT NOT NULL,
        PRIMARY KEY (id_pelicula AUTOINCREMENT)
    )"""
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as error:
        titulo = "Crear Tabla"
        mensaje = f"Error: {error}"
        messagebox.showwarning(titulo, mensaje)
    else:
        titulo = "Crear Tabla"
        mensaje = "Se creo la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)

def eliminar_tabla():
    conexion = ConexionDB()

    sql = "DROP TABLE peliculas"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as error:
        titulo = "Eliminar Tabla"
        mensaje = f"Error: {error}"
        messagebox.showwarning(titulo, mensaje)
    else:
        titulo = "Eliminar Tabla"
        mensaje = "Se elimino la tabla en la base de datos"
        messagebox.showinfo(titulo, mensaje)

def agregar_pelicula(nom, dur, gen):
    conexion = ConexionDB()
    sql = "INSERT INTO peliculas (nombre, duracion, genero) VALUES ('{}', {}, '{}')".format(nom, dur, gen)

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as error:
        titulo = "Agregar pelicula"
        mensaje = f"Error: {error}"
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    lista_peliculas = []
    sql = "SELECT * FROM peliculas"

    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except Exception:
        pass

    return lista_peliculas

def editar(nom, dur, gen, id_pelicula):
    conexion = ConexionDB()

    sql = f"UPDATE peliculas SET nombre = '{nom}', duracion = {dur}, genero = '{gen}' WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as error:
        titulo = "Editar pelicula"
        mensaje = f"Error: {error}"
        messagebox.showinfo(titulo, mensaje)

def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f"DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as error:
        titulo = "Eliminar pelicula"
        mensaje = f"Error: {error}"
        messagebox.showinfo(titulo, mensaje)
