"""
Definir una clase Operacion que tiene dos atributos: dos números enteres x y y. Esta clase nos permitirá realizar operaciones aritméticas
entre estos dos atributos
"""


class Operacion():
    """
    Contructor de la clase Operacion que recibe como parámetros:
    num_01: primer número
    num_02: segundo número    
    """

    def __init__(self, num_01: int, num_02: int):
        self.num_01 = num_01
        self.num_02 = num_02

    def suma(self):
        """
        Este método calcula la suma de los dos números
        """
        return self.num_01 + self.num_02

    def multiplicacion(self):
        """
        Este método calcula la multiplicación de los dos números
        """
        return self.num_01 * self.num_02

    def division(self):
        """
        Este método calcula la división de los dos números
        """
        if self.num_02 == 0:
            return "¡Division de num_01 por num_02 es imposible!"
        else:
            return self.num_01 / self.num_02


operacion_1 = Operacion(15, 0)

print(operacion_1.suma())
print(operacion_1.multiplicacion())
print(operacion_1.division())
