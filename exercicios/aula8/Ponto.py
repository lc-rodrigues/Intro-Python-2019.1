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
        tangente = self.y/self.x
        return tangente

    def parametros_reta(self, segundo):
        if segundo.x == self.x:
            if segundo.y == self.y:
                print("Os pontos informados devem ser diferentes")
                return ""
            else:
                print("A equação da reta x = ", self.x)
                return ""
        else:
            a = (segundo.y - self.y)/(segundo.x - self.x)
            b = self.y - a*self.x
            return a, b



