"""
Definir una clase Vehiculo y una clase Coche que herede de la clase Vehiculo. La clase Vehiculo contiene 2 atributos: marca del vehiculo una velocidad inicial con un valor predeterminado = 0. 
La subclase Coche tiene un atributo adicional llamado bocina con un valor predeterminado = "¡tuuut!"
"""


class Vehiculo:
    """
    Clase Vehiculo con 2 atributos: marca del vehiculo una velocidad inicial con un valor predeterminado = 0.
    """

    def __init__(self, marca, velocidad_inicial=0):
        self.marca = marca
        self.velocidad_inicial = velocidad_inicial
        print(f"La velocidad inicial del coche es: {self.velocidad_inicial} km/h")

    def acelerar(self, v):
        """
        Método que acelera el coche.
        """
        self.velocidad = v
        self.velocidad_inicial += self.velocidad

    def desacelerar(self, v):
        """
        Método que desacelera el coche.
        """
        self.velocidad = v
        self.velocidad_inicial -= self.velocidad

    def mostrar_velocidad(self):
        """"
        Método que muestra la velocidad actual del coche.
        """
        return f"Tu velocidad actual es: {round(self.velocidad_inicial, 2)} km/h"


class Coche(Vehiculo):
    """
    Clase Coche que hereda de la clase Vehiculo. La clase Coche tiene un atributo adicional llamado bocina con un valor predeterminado = "¡tuuut!"
    """

    def __init__(self, marca, velocidad_inicial=0, bocina="¡tuuut!"):
        super().__init__(marca, velocidad_inicial)
        self.bocina = bocina

    def tocar_claxon(self):
        """
        Método que hace sonar el claxon del coche.
        """
        print(self.bocina)


coche_01 = Coche("Peugeot", 10.6)
coche_01.acelerar(60)
coche_01.desacelerar(15)
print(coche_01.mostrar_velocidad())
coche_01.tocar_claxon()
