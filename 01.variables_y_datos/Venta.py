# Mostrar mensaje
print("Encontrar el IGV y el precio de venta")

# Entrar datos al programa
valor_venta = float(input("Ingrese el valor de venta del producto: "))

# Realizar operaciones
igv = valor_venta * 0.18
precio_venta = valor_venta + igv

# Mostrar salida
print("-" * 30)
print("----------- Ticket -----------")
print(f"Valor de venta = {valor_venta}\nIGV(16%) = {igv}\nPrecio de venta = {precio_venta}")
print("-" * 30)
