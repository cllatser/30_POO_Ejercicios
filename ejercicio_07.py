"""
Este ejercicio requirer el uso de la clase Persona del ejercicio 6.
Definir una clase Estudiante que herede de la clase Persona del ejercicio 6.
"""


from ejercicio_06 import Persona


class Estudiante(Persona):
    """
    Clase Estudiante que hereda de la clase Persona del ejercicio 6.
    """
    def __init__(self, nombre, edad, genero, nivel):
        super().__init__(nombre, edad, genero)
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nivel = nivel
        
    def inscripcion(self):
        """
        Método que añade a la lista estudiantes_instritos los datos del estudiante.
        """
        estudiantes_instritos.append((self.nombre, self.edad, self.genero, self.nivel))
        
# Lista que almacena los datos de los estudiantes inscritos.
estudiantes_instritos: list = []

estudiante01= Estudiante("Carlos", 43, "hombre", "Alto")
print(estudiantes_instritos)
estudiante01.inscripcion()
print(estudiantes_instritos)