class Ponto:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe. """
        self.x = x
        self.y = y

    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def print_ponto(pt):                                 #Esta função e a seguinte não estão dentro da definição da classe ponto. Por isso elas não necessitam ser chamadas com p.print_ponto ou p.ponto_medio
    print("({0}, {1})".format(pt.x, pt.y))
        
def ponto_medio(p1, p2):
    """ Retorna o ponto médio dos pontos p1 e p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Ponto(mx, my)


p = Ponto(4, 2)
q = Ponto(6, 3)
r = Ponto()       # r representa a origem (0, 0)
#print(p.x, q.y, r.x)

p = Ponto(3, 4)                   # instanciando um objeto do tipo Ponto
print(p.x)                        # acessando seus atributos
print(p.y)
print("distancia da origem para p: ", p.distancia_da_origem())    # distância da origem

r = Ponto()
print(r.x)
print(r.y)
print("distancia da origem para r: ", r.distancia_da_origem())

p = Ponto(3, 4)
q = Ponto(5, 12)
r = ponto_medio(p, q)
print_ponto(r)
