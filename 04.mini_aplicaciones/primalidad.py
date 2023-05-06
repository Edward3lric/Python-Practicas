
def primalidad(numero):
    for n in range(1, numero + 1):
        if n == 1 or n == numero:
            continue
        if numero % n == 0:
            return False
    else:
        return True

def main():
    numero = int(input("Ingrese un numero: "))

    if primalidad(numero):
        print("El numero es primo")
    else:
        print("No es primo")

if __name__ == "__main__":
    main()
