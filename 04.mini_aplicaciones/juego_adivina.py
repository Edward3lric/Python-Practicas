import random


def jugar(vidas):
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = None

    while numero_aleatorio != numero_elegido:
        if vidas > 0:
            numero_elegido = int(input("Ingresa un numero entre 1 y 100: "))
            if numero_aleatorio < numero_elegido:
                print("Elige un numero mas pequeño")
            elif numero_aleatorio > numero_elegido:
                print("Elige un numero mas grande")
            vidas -= 1
        else:
            print("Game Over")
            break

        print(f"Te quedan {vidas} vidas")
    
    input("Felicidades")


def main():
    menu = """
    ADIVINA EL NÚMERO ALEATORIO
    1 - Nivel Facil
    2 - Nivel Intermedio
    3 - Nivel Dificil
    4 - Salir
    INGRESE UNA OPCIÓN: """

    opcion = None
    while opcion != 4:
        opcion = int(input(menu))
        if opcion == 1:
            jugar(15)
        elif opcion == 2:
            jugar(10)
        elif opcion == 3:
            jugar(5)
        elif opcion == 4:
            print("Adios")
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()
