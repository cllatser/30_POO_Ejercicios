"""
Definir una clase Dado con un atributo "resultado" que corresponde al resultado obtenido depués de lanzar el dado.
"""

# Importamos la librería random para generar números aleatorios
from random import randint


class Dado():
    """
    Clase Dado con un atributo "resultado" que corresponde al resultado obtenido depués de lanzar el dado.
    """
    def __init__(self):
        self.resultado = 0

    def lanzar_dado(self):
        """
        Método que genera un número aleatorio entre 1 y 6 y lo guarda en el atributo "resultado".
        """
        self.resultado = randint(1, 6)

    def mostrar_puntos(self):
        """
        Método que muestra el número de puntos obtenidos.
        """
        return f"El número de puntos obtenidos es: {self.resultado}"
    

lanzamiento_1 = Dado()
lanzamiento_1.lanzar_dado()
print(lanzamiento_1.mostrar_puntos())
