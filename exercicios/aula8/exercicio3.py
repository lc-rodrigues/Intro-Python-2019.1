import math as m

class Ponto:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe. """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def distancia (self, segundo):
        d = ((self.x - segundo.x)**2 + (self.y - segundo.y)**2)**0.5
        return d

    def reflexao_x (self):
        self.y = -self.y
        return self

    def inclinacao_da_origem(self):
        if self.x == 0:
            if self.y == 0:
                print("O ponto informado deve ser diferente da origem")
            else:
                print("O ponto está sobre o eixo y")
        else:
            tan = self.y/self.x
            return tan
        
p = Ponto(4,-10)

print(p.inclinacao_da_origem())



