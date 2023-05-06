
# Entrada de datos
consumo = float(input("Cual es el consumo: $"))
descuento = 0

# Calcular
if consumo <= 100 and consumo > 0:
    dato_descuento = "10%"
    descuento = consumo * 0.10
elif consumo > 100:
    dato_descuento = "20%"
    descuento = consumo * 0.20

impuesto = (consumo - descuento) * 0.19
total = consumo - descuento + impuesto

# Salida
print("="*30)
print("----------- Ticket -----------")
print(f"Consumo: ${consumo}")
print(f"Descuento: {dato_descuento} - ${descuento}")
print(f"Impuesto: ${impuesto}")
print(f"Importe a pagar: ${total}")
print("="*30)
