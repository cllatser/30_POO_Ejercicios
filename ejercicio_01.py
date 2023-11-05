"""
Difinir una clase Galleta que tiene dos atributos: nombre de la galleta y su forma.
La clase Galleta debe contener el contructor y el siguiente método:
    - __init__(self, nombre, forma): un constructor que permite inicializar los atributos de la clase
    Galleta.
    - hornear(self): un método que simplemente permite mostrar dos frases en la consola:
"""


class Galleta:
    def __init__(self, nombre, forma):
        self.nombre = nombre
        self.forma = forma

    def hornear(self):
        print(f"Esta {self.nombre} ha sido horneada en forma de {self.forma}")
        print("¡Buen provecho!")


galleta01 = Galleta("Galleta de chocolate", "corazón")
galleta02 = Galleta("Galleta de vainilla", "estrella")
galleta03 = Galleta("Galleta de limón", "círculo")

galleta01.hornear()
galleta02.hornear()
galleta03.hornear()
