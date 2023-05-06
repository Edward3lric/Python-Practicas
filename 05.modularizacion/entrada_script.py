import sys

# Este programa recibe argumento desde el el script como args con Java

if len(sys.argv) == 3:
    # Recibir el primer argumento desde la ejecucion del scrip
    texto = sys.argv[1]
    cantidad = int(sys.argv[2])

    for n in range(cantidad):
        print(texto)
else:
    print("Error, Ingrese los argumentoss correctamente")
    print("Ejemplo: script.py \"texto\" 5")