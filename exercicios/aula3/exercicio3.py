import math

def zenite(tam_obj, tam_sombra):
    angulo_rad = math.atan(tam_sombra/tam_obj)
    angulo_grau = math.degrees(angulo_rad)
    print(' Se um objeto de altura', tam_obj, 'm possuir uma sombra =', tam_sombra, 'm, o ângulo zenital do sol é', round(angulo_rad, 2), ' em radianos e', round(angulo_grau, 2), 'em graus')

zenite(12, 1)
    
