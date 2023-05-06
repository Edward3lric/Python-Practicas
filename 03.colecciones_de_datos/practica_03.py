from random import randint

pares = []
impar = []

numeros = (range(1, 10))

for numero in numeros:
    aleatorio = randint(1, 100)
    num_fin = numero * aleatorio

    print(f"{numero} x {aleatorio} = {num_fin}")

    if (num_fin % 2) == 0:
        pares.append(num_fin)
    else:
        impar.append(num_fin)

print("Lista de pares: ", pares)
print("Lista de impares: ", impar)
