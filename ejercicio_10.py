"""
Definir una clase Empleado con 4 atributos: el nombre del empleado, su función, su salario y el número de horas trabajadas.
"""


class Empleado:
    """
    Clase Empleado con 4 atributos: el nombre del empleado, su función, su salario y el número de horas trabajadas.
    """

    def __init__(self, nombre, funcion, salario):
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario
        self.horas_trabajadas = 0

    def trabajar(self, numero_horas):
        """
        Método que suma las horas trabajadas por el empleado.
        """
        self.horas_trabajadas += numero_horas
        print(f"El empleado {self.nombre} ha trabajado {self.horas_trabajadas} horas.")

    def info_sueldo(self):
        """
        Método que muestra el salario del empleado.
        """
        print(f"El empleado {self.nombre} recibe un salario de {self.salario} euros.")

    def dar_aumento(self, cantidad):
        """
        Método que aumenta el salario del empleado.
        """
        self.salario += cantidad
        print(f"El empleado {self.nombre} ha recibido un aumento de {cantidad} euros, lo que le da un salario de {self.salario} euros.")

    def info_funcion(self):
        """
        Método que muestra la función del empleado.
        """
        print(f"El empleado {self.nombre} trabaja como {self.funcion}")


# Crear un objeto de la clase Empleado y probar sus métodos.
empleado_01 = Empleado("Julen", "Ingeniero", 4000)
empleado_01.trabajar(8)
empleado_01.info_sueldo()
empleado_01.dar_aumento(600)
empleado_01.info_funcion()
