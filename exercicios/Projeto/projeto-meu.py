
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chisquare


def breitwigner(m, gama, M, a, b, A):
    """ m é a variável independente;
    gamma é a largura à meia altura (FWHM);
    M é a posição do pico;
    a e b são, respectivamente, os coeficientes angular e linear da reta que parametriza o ruído de fundo dos dados;
    A é uma constante multiplicativa da função breitwigner"""
    return a*m + b + A*( (2*np.sqrt(2)*M*gama*np.sqrt(M**2*(M**2+gama**2)))/(np.pi*np.sqrt(M**2+np.sqrt(M**2*(M**2+gama**2)))) )/((m**2-M**2)**2+M**2*gama**2)

def gaussiana(m, gama, M, a, b, A):
    """ m é a variável independente;
    gama é a largura à meia altura;
    M é a posição do pico;
    a e b são, respectivamente, os coeficientes angular e linear da reta que parametriza o ruído de fundo dos dados;
    A é uma constante multiplicativa"""
    
    sigma = gama/2
    return a*m + b + A*np.exp(-(m-M)**2/(2*sigma**2))

"""def c_ball(m, gama, M, n, alfa, a, b, A1):
    m é a variável indepentende;
    gamma é a largura à meia altura;
    M é a posição do pico;
    n e alfa são parâmetros livres da função;
    a e b são, respectivamente,os coeficientes angular e linear da reta que parametriza o ruído de fundo dos dados;
    A é uma constante multiplicativa da função breitwigner
    
    A = (n/abs(alfa))**n*np.exp(-1*(alfa**2/2))
    B = n/abs(alfa) - abs(alfa)
    C = (n/abs(alfa))*(1/(n-1))*np.exp(-1*alfa**2/2)
    D = np.sqrt(np.pi/2)*(1+erf(abs(alfa)/2**0.5))
    N = 1/((gama/2)*(C + D))
     
    if (m - M)/(gama/2) > -alfa:
        return N*np.exp(-1*(m-M)**2/(gama/2))
    else:
        return N*A*(B - ((m-M)/gama/2))**-n"""


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

print(" ")
print("Observando o gráfico em escala logarítimica a seguir, é possível observar alguns picos.")
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

# Formata o novo histograma.
plt.xlabel('log10(massa invariante) [log10(GeV)]')
plt.ylabel('Número de eventos')
plt.title('Histograma da massa invariante dos múons \n')
plt.show()

# Pergunta ao usuário qual pico ele deseja analisar

pico = float(input("Digite o número do pico que deseja analisar:   "))
print(" ")
while pico > 6 or pico < 1:
    print("Valor de pico inválido")
    pico = float(input("Digite o número do pico que deseja analisar:   "))
    
print("Você pode escolher uma das funções abaixo para descrever o pico:   ")
print(" ")
print("1 - Gaussiana")
print("2 - Breitwigner")
print(" ")
funcao = float(input("Digite o número da função que deseja utilizar na análise:   "))
while funcao > 2 or funcao < 1:
    print("Valor de função inválida")
    funcao = float(input("Digite o número da função que deseja utilizar na análise:   "))
if funcao == 1:
    fit = gaussiana
else:
    fit = breitwigner



if pico == 1:
    
# Limitação do espectro na região do pico 6.
    lowerlimit = 0.65
    upperlimit = 0.85
    bins = 100
    
# Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 0.7 or centro > 0.8:
        if centro < 0.7:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 0.8:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 1 or gama < 0.05:
        if gama < 0.05:
#            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 1:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials1 = [gama, centro, -7, 58, 37]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials1, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama - best[0]) > 0.1 or abs(centro - best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials1, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))

elif pico == 2:
    
        # Limitação do espectro na região do pico 6.
    lowerlimit = 0.8
    upperlimit = 1.2
    bins = 100
    
    # Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 0.95 or centro > 1.05:
        if centro < 0.8:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 1.04:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 1 or gama < 0.05:
        if gama < 0.05:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 1:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials2 = [gama, centro, 8, 99, 92]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials2, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama-best[0]) > 0.1 and abs(centro-best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials2, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))
    
elif pico == 3:
    
        # Limitação do espectro na região do pico 6.
    lowerlimit = 2.9
    upperlimit = 3.3
    bins = 100
    
    # Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 2.99 or centro > 3.15:
        if centro < 2.99:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 3.15:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 1 or gama < 0.02:
        if gama < 0.02:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 1:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials3 = [gama, centro, -91, 316, 870]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials3, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama-best[0]) > 0.1 and abs(centro-best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials3, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))

elif pico == 4:
    
    # Limitação do espectro na região do pico 6.
    lowerlimit = 3.2
    upperlimit = 4.0
    bins = 100
    
    # Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 3.6 or centro > 3.75:
        if centro < 3.6:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 3.75:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 1.0 or gama < 0.01:
        if gama <= 0.01:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 1.0:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials4 = [gama, centro, -60, 275, 70]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials4, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama-best[0]) > 0.1 and abs(centro-best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials4, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))
        
elif pico == 5:
    
    # Limitação do espectro na região do pico 6.
    lowerlimit = 9
    upperlimit = 9.8
    bins = 100
    
    # Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 9.25 or centro > 9.6:
        if centro < 9.25:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 9.8:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))    
   
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 0.9 or gama < 0.1:
        if gama < 0.2:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 0.9:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))  

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials5 = [gama, centro, 50, -360, 215]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials5, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama-best[0]) > 0.1 and abs(centro-best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials5, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))

elif pico == 6:
      
# Limitação do espectro na região do pico 6.
    lowerlimit = 75
    upperlimit = 105
    bins = 100

# Seleção dos valores de massa dentro da região delimitada.
    limitedmasses = invariant_mass[(invariant_mass > lowerlimit) & (invariant_mass < upperlimit)]

# Plot do histograma com os valores selecionados.
    histogram = plt.hist(limitedmasses, bins=bins, range=(lowerlimit,upperlimit))
    
# No eixo y, tem-se o número de eventos em cada bin (é lido a partir da variável histogram).
# No eixo x, o centro de cada bin.
    y = histogram[0]
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:] )
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico?   "))
    print(" ")
    while centro < 83.0 or centro > 98.0:
        if centro < 83.0:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 98.0:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))   
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico?   "))
    print(" ")
    while gama > 7.0 or gama < 1.0:
        if gama < 1.0:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
        elif gama > 7.0:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))

# Palpites iniciais para o fit da função, na ordem da esquerda para direita:
# gama - largura à meia altura (FWHM) da distribuição.
# M - valor máximo (altura do pico) da distribuição.
# a - coeficiente angular da função linear de parametrização do ruído.
# b - coeficiente linear da função linear de parametrização do ruído.
# A - constante multiplicativa (altura da função) da função brewitwigner.
    initials6 = [gama, centro, -2, 200, 13000]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials6, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(gama-best[0]) > 0.1 and abs(centro-best[1]) > 0.1:
        gama = best[0]
        centro = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials6, sigma=np.sqrt(y))
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

plt.plot(x, fit(x, *best), 'r-', label='gama = {}, M = {}'.format(best[0], best[1]))
plt.xlabel('Massa Invariante [GeV]')
plt.ylabel('Número de eventos')
plt.title('Fit da Função')
#plt.legend()
plt.show()

#Realização do teste estatístico chi-quadrado

z = [fit(lowerlimit, best[0], best[1], best[2], best[3], best[4])]

for i in range(bins - 1):
    
    k = lowerlimit + i*(upperlimit - lowerlimit)/bins
    l = fit(k, best[0], best[1], best[2], best[3], best[4])
    z.append(l)
    
divergencia, valorp = chisquare(f_obs = y, f_exp = z)
    
print(" ")
print("Uma maneira de avaliar o fit realizado é através do valor do teste de estatística chi-quadrado.")
print("Quanto menor seu valor, maior é a qualidade do fit realiado.")
print("Neste caso, o valor encontrado é: ", divergencia)
print(" ")
print(" ")


#Comparação com dados da literatura
print("Comparando com dados disponíveis na literatura, tem-se")

#ρ_ω_ref =
#ρ_ω_ref_error = 
#Φ_ref = 
#Φ_ref_error = 
#J_Ψ_ref =
#J_Ψ_ref_error = 
#Ψ1_ref =
#Ψ1_ref_error = 
#Y_ref =
#Y_ref_error = 
Z_ref = 91.1876                   #[1]
Z_ref_error = 0.0021

"""if pico == 1:
    print("A massa do bóson Z esperada é (", ρ_ω_ref, "±", ρ_ω_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*ρ_ω_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        
if pico == 2:
    print("A massa do bóson Z esperada é (", Φ_ref, "±", Φ_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Φ_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        
if pico == 3:
    print("A massa do bóson Z esperada é (", J_Ψ_ref, "±", J_Ψ_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*J_Ψ_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        
if pico == 4:
    print("A massa do bóson Z esperada é (", Ψ1_ref, "±", Ψ1_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Ψ1_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        
if pico == 5:
    print("A massa do bóson Z esperada é (", Y_ref, "±", Y_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Y_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")"""

if pico == 6:
    print("A massa do bóson Z esperada é (", Z_ref, "±", Z_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", best[1], "±", error[1],") GeV/c²")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Z_ref_error:
        print("Ou seja, considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
    else:
        print("Ou seja, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        



# [1] http://pdg.lbl.gov/2018/listings/rpp2018-list-z-boson.pdf
    
