import random

def generar_contrasenia(tamanio=15):
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    simbolos = ["!", "·", "$", "%", "&", "/", "(", ")", "=", "?", "¿"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    caracteres = mayusculas + minusculas + simbolos + numeros
    contrasenia = []

    for i in range(tamanio):
        contrasenia.append(random.choice(caracteres))

    contrasenia = "".join(contrasenia)
    return contrasenia

def main():
    contrasenia = generar_contrasenia()
    print("Tu nueva contasenia es: " + contrasenia)

if __name__ == "__main__":
    main()