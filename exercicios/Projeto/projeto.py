
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def breitwigner(m, gamma, M, a, b, A):
    """ m é a variável independente;
    gamma é a largura à meia altura (FWHM);
    M é valor máximo de m;
    a e b são, respectivamente, os coeficientes angular e linear da reta que parametriza o ruído de fundo dos dados;
    A é uma constante multiplicativa da função breitwigner"""
    return a*m+b+A*( (2*np.sqrt(2)*M*gamma*np.sqrt(M**2*(M**2+gamma**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gamma**2)))) )/((m**2-M**2)**2+M**2*gamma**2)

ds = pd.read_csv('DoubleMuRun2011A.csv')

invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1 - ds.eta2) - np.cos(ds.phi1 - ds.phi2)))

plt.hist(x = invariant_mass, bins = 200, range = (0, 115))          # 1° plot: dados em escala linear

plt.xlabel('Massa Invariante [GeV]')
plt.ylabel('Número de eventos')
plt.title('Histograma dos valores de massa invariante de 2 múons.\n')
plt.show()

invariant_mass_1 = ds['M']                                         # 2° plot: dados em escala logarítmica. Aqui é possível visualizar os picos

no_bins = 500
# Cálculo do logaritmo das massas e frequências.
inv_mass_log = np.log10(invariant_mass_1)
weights = []
for a in invariant_mass_1:
    weights.append(no_bins/np.log(10)/a)

# Plot do histograma em escala logarítmica.
plt.hist(inv_mass_log, no_bins, range=(-0.5,2.5), weights=weights, lw=0, color="darkgrey")
plt.yscale('log')

# Formata o novo histograma.
plt.xlabel('log10(invariant mass) [log10(GeV)]')
plt.ylabel('Number of the events')
plt.title('The histogram of the invariant masses of two muons \n')
plt.show()

# Pergunta ao usuário qual pico ele deseja analisar

print(" ")
print("Olhando o gráfico em escala logarítimica, é possível observar alguns picos.")
print(" ")
print("Da esquerda para direita, os picos observados são:")
print(" ")
print("pico 1 = ρ,ω")
print("pico 2 = Φ")
print("pico 3 = J/Ψ")
print("pico 4 = Ψ'")
print("pico 5 = Υ")
print("pico 6 = Z")
print(" ")

pico = int(input("Digite o número do pico que deseja analisar:   "))
print(" ")

if pico > 7 or pico < 1:
    print("Valor de pico inválido")

elif pico == 6:
      
# Limitação do espectro na região do pico 6.
    lowerlimit = 70
    upperlimit = 110
    bins = 100

# Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# NÃO SEI O QUE ISSO FAZ
# In y-axis the number of the events per each bin (can be got from the variable histogram).
# In x-axis the centers of the bins.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )

    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    centro = float(input(" Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gamma - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials = [gama, centro, -2, 200, 13000]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(breitwigner, x, y, p0=initials, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
# Impressão dos valores e incertezas dos parâmtros do fit.
    print("Valores e incertezas do fit da função")
    print("")
    first = "Largura à meia altura: gama = {} +- {}".format(best[0], error[0])
    second = "Valor do máximo da distribuição: M = {} +- {}".format(best[1], error[1])
    third = "a = {} +- {}".format(best[2], error[2])
    fourth = "b = {} +- {}".format(best[3], error[3])
    fifth = "A = {} +- {}".format(best[4], error[4])
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)

    plt.plot(x, breitwigner(x, *best), 'r-', label='gamma = {}, M = {}'.format(best[0], best[1]))
    plt.xlabel('Invariant mass [GeV]')
    plt.ylabel('Number of event')
    plt.title('The Breit-Wigner fit')
    #plt.legend()
    plt.show()
