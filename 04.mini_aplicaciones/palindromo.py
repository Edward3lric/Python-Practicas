
def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()

    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


# Funcion principal
def main():
    palabra = input("Ingresa una palabra: ")

    if palindromo(palabra):
        print("Es palindromo")
    else:
        print("No es palindromo")


# Punto de entrada de la aplicacion
if __name__ == "__main__":
    main()
