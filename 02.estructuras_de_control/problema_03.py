# Obtener datos del usuario
ni = int(input("Cual es el numero inicial? "))
nf = int(input("Cual es el numero final? "))

# Iniciar contadores
cp = 0
cn = 0

# Ciclo para ir contando los numeros dentro del rango
for a in range(ni, nf):
    if a >= 0:
        cp += 1
    else:
        cn += 1

# Imprimir el resultado
print(f"Numeros positivos: {cp}\nNumeros negativos: {cn}")