"""
Definir una clase Nota que tiene dos atributos: nombre del estudiante y su nota.
La  classe Nota debe contener el contructor y el siguiente método
"""


class Nota():

    def __init__(self, nota, nombre_estudiante):
        self.nota = nota
        self.nombre_estudiante = nombre_estudiante

    def ha_pasado(self):
        if self.nota > 75:
            print("El estudiante ha aprobado")
        else:
            print("El estudiante no ha aprobado")

    def __str__(self) -> str:
        return f"El estudiante se llama {self.nombre_estudiante} y su nota es {self.nota}"


nota_1 = Nota(80, "Julien")
nota_1.ha_pasado()
nota_2 = Nota(35, "Amélie")
print(nota_2)
nota_2.nota = 90
nota_2.ha_pasado()
