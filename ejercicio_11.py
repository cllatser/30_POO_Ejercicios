"""
Definir una clase Calculo_Numerico que nos permita llevar a cabo varias operaciones numéricas. Esta clase tiene un solo atributo: un número entero.
"""

class Calculo_Numerio:
    """"
    Clase Calculo_Numerico que nos permita llevar a cabo varias operaciones numéricas. Esta clase tiene un solo atributo: un número entero.
    """
    def __init__(self, numero):
        self.numero = numero
        
    def calculo_factorial(self):
        """
        Método que calcula el factorial del número.
        """
        factorial = 1
        for i in range(1, self.numero + 1):
            factorial *= i
        print(f"El factorial de {self.numero} es {factorial}")
        
    def lista_divisores(self) -> list:
        """
        Método que calcula los divisores del número.
        """
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        print(f"Los divisores de {self.numero} son {divisores}")
        
    def es_primo(self) -> bool:
        """
        Método que comprueba si el número es primo.
        """
        if self.numero < 2:
            return False
        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False
        print(f"{self.numero} es primo")
    
    def es_par(self) -> bool:
        """
        Método que comprueba si el número es par.
        """
        if self.numero % 2 == 0:
            return True
        print(f"{self.numero} es impar")
       
# Crear un objeto de la clase Calculo_Numerico y probar sus métodos.         
calculo = Calculo_Numerio(55)
calculo.calculo_factorial()
calculo.lista_divisores()
calculo.es_primo()
calculo.es_par()
