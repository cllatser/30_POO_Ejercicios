"""
Escribir una clase Persona que tiene tres atributos: el nombre de la persona, su edad y su género
"""


class Persona():
    """
    Clase Persona inicializada con nombre, edad y género
    """

    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self. genero = genero

    def presentarse(self):
        """
        Método que devuelve una cadena con el nombre, edad y género de la persona
        """
        return f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}."

    def es_adulto(self):
        """
        Método que devuelve True si la persona es mayor de edad y False si no lo es
        """
        if self.edad >= 18:
            return True
        else:
            return False


persona1 = Persona("Carlos", 43, "hombre")

print(persona1.presentarse())
print(persona1.es_adulto())
