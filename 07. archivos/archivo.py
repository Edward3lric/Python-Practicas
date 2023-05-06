from io import open
from os import path

def escribir_archivo():
    archivo = open("text.txt", "w")
    archivo.write("Hello World\nHola Mundo")
    archivo.close()

def leer_archivo():
    try:
        archivo = open("text.txt", "r")
        #texto  = archivo.read()
        texto = archivo.readlines()
        archivo.close()
        print(texto)
        
    except FileNotFoundError:
        print("No existe el archivo")

def agregar_datos():
    if path.isfile("text.txt"):
        archivo = open("text.txt", "a")
        archivo.write("\nXdXdXd")
        archivo.close
    else:
        print("No existe el archivo")

def modificar_datos():
    try:
        archivo = open("text.txt", "r+")
        texto = archivo.readlines()
        print(texto)
        texto[1] = "esta\n"
        print(texto)
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()
        
    except FileNotFoundError:
        print("No existe el archivo")

def eliminar_datos():
    try:
        archivo = open("text.txt", "w")
        archivo.close
        
    except FileNotFoundError:
        print("No existe el archivo")
    
eliminar_datos()