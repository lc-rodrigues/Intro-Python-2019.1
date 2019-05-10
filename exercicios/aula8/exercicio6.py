import math as m
from Ponto import *

class Circulo:
    
    """Representa um circulo"""
    
    def __init__(self, raio=0, centro = Ponto(0,0)):
        """ Inicializa o círculo a partir do ponto centro e do parâmetro raio"""
        self.raio = raio
        self.centro = centro
        
    def __str__(self):
        return "({0}, {1})".format(self.raio, self.centro)

    def area(self):                                         #função teste
        """Retorna a área do círculo"""
        a = m.pi*((self.raio)**2)
        return a
    
    def ponto_no_circulo(self, p = Ponto()):
        d = ((self.centro.x - p.x)**2 + (self.centro.y - p.y)**2)**1/2
        if d <= self.raio:
            return "True"
        else:
            return "False"

#print(Circulo(1, Ponto(1,1)).area())                       #teste da função teste
        
redondo = Circulo(75, Ponto(150, 100))

print(redondo.centro)

print(redondo.ponto_no_circulo(Ponto(150, 88)))
    
