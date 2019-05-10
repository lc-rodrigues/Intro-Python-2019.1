class Ponto:
    """ A classe Ponto representa e manipula as coordenadas x,y . """

    def __init__(self):
        """ Cria um novo ponto posicionado na origem. """
        self.x = 0
        self.y = 0

p = Ponto()         # Instanciar um objeto do tipo Ponto
q = Ponto()         # Fazer um segundo objeto do tipo Ponto

print(p.x, p.y, q.x, q.y)  # Cada objeto do tipo ponto tem seu próprio x e y

p = Ponto()
p.x = 3
p.y = 4
print(p.x, p.y)
print(type(p))
print(type(p.x))

