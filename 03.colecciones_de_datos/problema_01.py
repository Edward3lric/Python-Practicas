
# Crear la lista
numeros = []

# Preguntar 6 veces un numero al usuario
for n in range(6):
    numeros.append(int(input("Ingresa un numero: ")))

# Definir variables
numero_mayor = numeros[0]
numero_menor = numeros[0]

# Recorrer la lista para encontrar el numero mayor y el menor
for numero in numeros:
    if numero_mayor < numero:
        numero_mayor = numero
    if numero_menor > numero:
        numero_menor = numero

# Imprimir el resultado
print(f"El numero mayor es: {numero_mayor}\nEl numero menor es: {numero_menor}")
