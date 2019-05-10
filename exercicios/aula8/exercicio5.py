from Ponto import *

class Retangulo:
    
    """Representa um retângulo"""
    
    def __init__(self, largura=0, altura=0, canto = Ponto(0,0)):
        """ Inicializa o retângulo a partir do ponto canto e dos parãmetros largura e altura"""
        self.largura = largura
        self.altura = altura
        self.canto = canto
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.largura, self.altura, self.canto)

    def vertices(self):                                         #função teste
        """Retorna os quatro vértices do triângulo"""
        v0 = (self.canto.x, self.canto.y)
        v1 = (self.canto.x + self.largura, self.canto.y)
        v2 = (self.canto.x + self.largura, self.canto.y + self.altura)
        v3 = (self.canto.x, self.canto.y + self.altura)
        return v0, v1, v2, v3

print(Retangulo(5, 5, Ponto(1,1)).vertices())
        

    
