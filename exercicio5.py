
#Alturas estão em metros e pesos estão em kilogramas

minha_altura = 1.8
meu_peso = 105
altura_bebe = 0.7
peso_bebe = 11

meu_imc = meu_peso/minha_altura**2
imc_bebe = peso_bebe/altura_bebe**2

print(' ')
print('O meu IMC é:', round(meu_imc, 1))
print(' ')
print('O IMC do bebê gorducho é:', round(imc_bebe, 1))
print(' ')
