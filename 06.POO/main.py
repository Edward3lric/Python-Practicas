# Importar las cleses y los metodos del archivo figuras
from figuras import *

# Funcion principal
def main():
    opcion = 0
    # Bucle infinito
    while (opcion != 3):
        # Menu principal
        opcion = int(input("Calcular Area y perimetro\n1. Rectangulo\n2. Circulo\n3. Salir\n"))
        # Opcion rectangulo
        if opcion == 1:
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            rec = rectangulo("Rectangulo", base, altura)
            probar_figura(rec)
            input("\nEnter para continuar")
        # Opcion radio
        elif opcion == 2:
            radio = float(input("Ingrese el radio del circulo: "))
            cir = circulo("Circulo", radio)
            probar_figura(cir)
            input("\nEnter para continuar")
        # Opcion salir
        elif opcion == 3:
            print("Saliendo del programa")
        # Opcion por defecto
        else:
            print("Opcion no valida")

# punto de entrada
if __name__ == "__main__":
    main()
