import math

def IMC(peso, altura):
    x = peso/(altura**2)
    return x

def vol_esfera(r):
    v = (4*math.pi*r**3)/3
    return v

def dist_max(comp, dist_fendas, dist_anteparo):
    d_max = comp*dist_anteparo/dist_fendas
    return d_max

print('Meu IMC é', round(IMC(105,1.8), 1), 'e o IMC do bebê gorducho é', round(IMC(11,0.7), 1), '.')
print(' ')
print('O volume da esfera de raio 5 é', round(vol_esfera(5), 0),'.')
print(' ')
print('A distância entre 2 máximos de interferência criados por uma onda de comprimento 632.8 nm interagindo com duas fendas distantes 0.25 mm entre si e 1.98 m de um anteparo é', round(1000*dist_max(632.8*0.000000001, 0.25*0.001, 1.98), 1), 'mm.')
