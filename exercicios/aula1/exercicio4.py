import math

altura = 5                   #altura do poste
sombra = 0.5                 #sombra do poste
angulo_rad = math.atan(sombra/altura)
angulo_grau = math.degrees(angulo_rad)

print(' ')
print('O ângulo zenital do sol, em radianos, é',round(angulo_rad, 4))
print(' ')
print('E, em graus, é', round(angulo_grau, 1))
print(' ')
