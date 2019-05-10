import math as m
from Ponto import *
import turtle

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

    def desenhar_circulo(self, t):
        """Desenha um círculo definido dos parâmetros fornecidos"""
        t.penup()
        t.goto(self.centro.x, self.centro.y)               # Posiciona o cursor no centro do círculo
        t.forward(self.raio)
        t.pendown()
        t.left(90)
        for i in range(90):                                # Desenha o círculo
            t.forward(2*m.pi*self.raio/90)
            t.left(4)

janela = turtle.Screen()
tartaruga = turtle.Turtle()

Circulo(75, Ponto(150, 100)).desenhar_circulo(tartaruga)

janela.mainloop()


#print(Circulo(1, Ponto(1,1)).area())                       #teste da função teste
        
    
