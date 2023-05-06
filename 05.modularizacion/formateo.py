from sys import argv

if len(argv) == 4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])

    print(f"Nombre: {nombre}\nEdad: {edad}\nAltura: {altura}")
    print("Nombre: {}\nEdad: {}\nAltura: {}".format(nombre, edad, altura))
    print("Nombre: {n}\nEdad: {e}\nAltura: {a}".format(a=altura, e=edad, n=edad))
    print("Nombre: %s\nEdad: %d\nAltura: %f"%(nombre, edad, altura))
    
else:
    print("Error, Ingrese los argumentoss correctamente")
    print("Ejemplo: script.py \"texto\" 20 1.67")
