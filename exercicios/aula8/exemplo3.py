class Ponto:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe. """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def para_string(self):
        return "({0}, {1})".format(self.x, self.y)

def print_ponto(pt):                                 #Esta função não está dentro da definição da classe ponto. Por isso ela não necessita ser chamadas com print_ponto
    print("({0}, {1})".format(pt.x, pt.y))

p = Ponto(3, 4)
#print(p.para_string())
print(p)
