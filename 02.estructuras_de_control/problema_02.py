# Obtener datos del usuario
ni = int(input("Cual es el numero inicial? "))
nf = int(input("Cual es el numero final? "))

# Iniciar contadores
c = 0

# Ciclo para ir contando los numeros dentro del rango
for a in range(ni, nf):
    c += 1

# Imprimir el resultado
print(f"Cantidad de numeros: {c}")