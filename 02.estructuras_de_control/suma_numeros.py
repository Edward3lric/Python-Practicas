"""
c = 0
while c < 5:
    print(f"El valor de c = {c}")
    
"""

# pedir un numero entero al usuario
num = int(input("Dime un numero entero: "))

# Declarar variables
menores_num = 1
sum = 0

# Ciclo while para ir sumando todos los numero menores
while menores_num < num:
    sum += menores_num
    menores_num += 1

# Imprimir resultado por consola
print("La suma es igual a {}".format(sum))