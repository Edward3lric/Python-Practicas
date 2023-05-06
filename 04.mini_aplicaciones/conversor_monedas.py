import requests
API_KEY = "ae552440bc4546e5b3bf14d13b5e7b21"

def obtener_valor(moneda_base, moneda_objetivo):
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}&base={moneda_base}&symbols={moneda_objetivo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["rates"][moneda_objetivo]
    else:
        return None

def conversor(valor_dolar, pais):
    contidad_moneda = float(input(f"Ingrese la contidad de {pais}: "))

    dolares = contidad_moneda / valor_dolar
    dolares = round(dolares, 2)

    input(f"Tienes ${dolares} Dolares")

def main():
    
    menu = """
    [1]Mexico
    [2]Argentina
    [3]Brasil
    [4]Otra
    [5]Salir
    De que pais es tu divisa: 
    """
    option = 0
    while option != 5:
        moneda_base = "USD"
        moneda_objetivo = None
        option = int(input(menu))
        if option == 1:
            moneda_objetivo = "MXN"
        elif option == 2:
            moneda_objetivo = "ARS"
        elif option == 3:
            moneda_objetivo = "BRL"
        elif option == 4:
            moneda_objetivo = input("Ingresa la clave de tu moneda")
        elif option == 5:
            print("Saliendo")
            continue

        conversor(obtener_valor(moneda_base, moneda_objetivo), moneda_objetivo)
        
if __name__ == "__main__":
    main()
