import math as m
from Ponto import *
import turtle

class Retangulo:
    
    """Representa um retângulo"""
    
    def __init__(self, largura=0, altura=0, canto = Ponto(0,0)):
        """ Inicializa o retângulo a partir do ponto canto e dos parâmetros largura e altura"""
        self.largura = largura
        self.altura = altura
        self.canto = canto
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.largura, self.altura, self.canto)

    def desenhar_ret(self, t):
        """Desenha um retângulo, com vértice inferior esquerdo na posição canto e com largura e altura fornecidos"""
        t.penup()
        t.goto(self.canto.x, self.canto.y)               # Posiciona o cursor no vértico inferior esquerdo
        t.pendown()
        t.forward(self.largura)                          # Desenha o retângulo
        t.left(90)
        t.forward(self.altura)
        t.left(90)
        t.forward(self.largura)
        t.left(90)
        t.forward(self.altura)
        
janela = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.speed(1)

Retangulo(200, 100, Ponto(50, 50)).desenhar_ret(tartaruga)

janela.mainloop()
        
    
