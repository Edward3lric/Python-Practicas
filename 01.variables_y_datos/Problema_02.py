# Mostrar mensaje
print("Convertir segundos a horas, minutos y segundos ")

# Entrar datos al programa
segundos = int(input("Ingrese la cantidad de segundos a convertir: "))

# Realizar operaciones
horas = segundos // (60 * 60)
minutos = (segundos // 60) - (horas * 60)
segundos = segundos - (minutos * 60) - (horas * (60 * 60)) 

# Mostrar salida
print(f"Horas: {horas}\nMinutos: {minutos}\nSegundos: {segundos}")
