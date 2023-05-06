
# Contador inicializado en 0
c = 0

# Ciclo while para iteracion del programa
while c < 10:
    c += 1
    print(c)

    if c == 5:
        # Terminar el bucle al llegar a 5
        # print("Termina el bucle")
        # break
        # Terminar aqui la iteracion 5
        print("Salta a la siguiente iteración")
        continue

    print("hola")

else:
    print("Termina el ciclo")