# Importar libreria math
from math import pi, pow

# Crear la clase figura
class figura:
    # Constructor con valores
    def __init__(self, nombre):
        self.nombre = nombre

    # Metodo area
    def area(self):
        pass

    # Metodo perimetro
    def perimentro(self):
        pass

    def __str__(self):
        return f"Nombre: {self.nombre}"

# Crear la clase rectangulo que hereda la clase figura
class rectangulo(figura):
    # Constructor con valores utilizando super
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    # Sobrescribir metodo area
    def area(self):
        area = self.altura * self.base
        return area
    
    # Sobrescibir metodo perimetro
    def perimetro(self):
        perimetro = self.altura * 2 + self.base * 2
        return perimetro
    
    def __str__(self):
        return super().__str__() + f"\nBase: {self.base}\nAltura: {self.altura}"
    
# Crar la clase circulo que hereda la clase figura 
class circulo(figura):
    # Constructor con valores utilizando super
    def __init__(self, nombre,  radio):
        super().__init__(nombre)
        self.radio = radio

    # Sobrescribir metodo area
    def area(self):
        area = pi * pow(self.radio, 2)
        return area
    
    # Sobrescibir metodo perimetro
    def perimetro(self):
        perimetro = (self.radio * 2) * pi
        return perimetro
    
    def __str__(self):
        return super().__str__() + f"\nRadio: {self.radio}"
    
    
# Funcion problar figura que recive un objeto como parametro    
def probar_figura(figura):
    print(figura)
    print("Area = {}".format(figura.area()))
    print("Perimietro = {}".format(figura.perimetro()))
