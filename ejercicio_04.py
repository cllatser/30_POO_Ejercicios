"""
Definir una clase Circulo que tiene tres atributos: su radio, la posición de su centro O(x,y)
"""
from math import pi


class Circulo():
    """
    Contructor de la clase Circulo que recibe como parámetros:
    x: posición en el eje x
    y: posición en el eje y    
    radio: radio del círculo
    """

    def __init__(self, x, y, radio):
        self.x = x
        self.y = y
        self.radio = radio

    def area(self):
        """
        Este método calcula el área del círculo
        """
        return pi * self.radio**2

    def perimetro(self):
        """
        Este método calcula el perímetro del círculo
        """
        return pi * 2 * self.radio

    def mostrar_propiedades(self):
        """
        Este método muestra las propiedades del círculo
        """
        return f"El círculo tiene un radio {self.radio} cm, y su centro es O({self.x, self.y} \nEl perímetro del circulo es: {round(self.perimetro(), 2)} \nEl área del circulo es: {round(self.area(), 2)} "


circulo_01 = Circulo(3, 4, 5)

print(circulo_01.perimetro())
print(circulo_01.mostrar_propiedades())
