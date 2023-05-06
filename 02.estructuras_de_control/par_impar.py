
# Pedir al usuario un numero entero
num = int(input("Ingresa un numero entero: "))

# Ver si el numero es distinto de 0
if num != 0:
    # Ver si el numero es positivo
    if num > 0:
        # Condicional if para verificar si el numero es par positivo
        if (num % 2) == 0:
            print(f"El número {num} es PAR POSITIVO")
        # En caso de no ser par indicamos que es impar positivo
        else:
            print(f"El número {num} es IMPAR POSITIVO")
    # En caso de no ser positivo es negativo
    else:
        # Condicional if para verificar si el numero es par negativo
        if (num % 2) == 0:
            print(f"El número {num} es PAR NEGATIVO")
        # En caso de no ser par indicamos que es impar negativo
        else:
            print(f"El número {num} es IMPAR NEGATIVO")
# En caso de no ser distinto de 0 es igual a 0
else:
    print(f"El número {num} es NEUTRO")
