
# Entrada de datos
consumo = 0
while consumo <= 0:
    consumo = float(input("Cual es el consumo: $"))

# Calcular
if consumo <= 100:
    # Descuendo del 10%
    dato_descuento = "10%"
    descuento = consumo * 0.10
elif consumo > 100 and consumo <= 200:
    # Descuendo del 20%
    dato_descuento = "20%"
    descuento = consumo * 0.20
elif consumo > 200:
    # Descuendo del 30%
    dato_descuento = "30%"
    descuento = consumo * 0.30

total_sin_impuesto = consumo - descuento
impuesto = total_sin_impuesto * 0.19
total = total_sin_impuesto + impuesto

# Salida
print("="*30)
print("----------- Ticket -----------")
print(f"Consumo: ${consumo}")
print(f"Descuento: {dato_descuento} - ${descuento}")
print(f"Importe sin impuesto: ${total_sin_impuesto}")
print(f"Impuesto: ${impuesto}")
print(f"Importe a pagar: ${total}")
print("="*30)
