
# Ingresar numero
numeros = [0, 0, 0]
for n in range(len(numeros)):
    numeros[n] = int(input(f"Dime el numero {n + 1}: "))

# Declarar variables
numero_mayor = numeros[0]
numero_menor = numeros[0]
suma = 0

# Ciclo for para detectar los numero mayor y menor ademas de sumarlos
for n in numeros:
    if numero_mayor < n:
        numero_mayor = n
    if numero_menor > n:
        numero_menor = n
    suma += n

# Calcular el numero intermedio
numero_int = suma - (numero_mayor + numero_menor)

# Imprimir el resultado
print(f"Menor: {numero_menor}\nIntermedio: {numero_int}\nMayor {numero_mayor}")    
