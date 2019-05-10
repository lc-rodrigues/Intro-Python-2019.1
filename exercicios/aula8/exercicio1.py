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

p = Ponto(5,5)
q = Ponto(4,4)

print(q.distancia(p))

