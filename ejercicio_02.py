"""
Definir una clase Libro que tiene tres atributos: título del libro, nombre del autor y precio del libro.
La clase Libro debe contener el contructor y el siguiente método
"""


class Libro:

    def __init__(self, titulo: str, autor: str, precio: float):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def mostrar_informacion(self):
        print(f"El libro titulado {self.titulo}, escrito por {self.autor}, se vende a {self.precio} euros")


libro_1 = Libro("100 Ejercicios Python para practicar", "Laurentine K.Masson", 9.99)

libro_1.mostrar_informacion()
