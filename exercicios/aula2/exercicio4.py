comprimento = 632.8*0.000000001       # comprimento de onda em metros
D = 1.98                         # distância entre a fenda e o anteparo
d = 0.25 * 0.001                 # distância entre as duas fendas
dY = comprimento*D/d

print(' ')
print ('A distância entre dois máximos consecutivos de interferência, em milímetros, é', round(dY*1000, 1))
print(' ')
