
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

ds = pd.read_csv('DoubleMuRun2011A.csv')

invariant_mass = np.sqrt(2*ds.pt1*ds.pt2*(np.cosh(ds.eta1 - ds.eta2) - np.cos(ds.phi1 - ds.phi2)))

plt.hist(x = invariant_mass, bins = 200, range = (0, 110))          # 1° plot: dados em escala linear

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

# Apresentação dos picos
print(" ")
print("Observando o gráfico em escala logarítimica a seguir, é possível observar alguns picos.")
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
pico = int(input("Digite o número do pico que deseja analisar: "))
print(" ")
while pico > 6 or pico < 1:
    print("Valor de pico inválido")
    pico = int(input("Digite o número do pico que deseja analisar: "))
    print(" ")

# Escolha da função para análise do pico escolhido
print("Você pode escolher uma das funções abaixo para descrever o pico: ")
print(" ")
print("1 - Gaussiana")
print("2 - Breitwigner")
print(" ")
funcao = float(input("Digite o número da função que deseja utilizar na análise: "))
print(" ")
while funcao > 2 or funcao < 1:
    print("Valor de função inválida")
    funcao = int(input("Digite o número da função que deseja utilizar na análise: "))
    print(" ")
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
    x = 0.5*( histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    print(" ")
    while centro < 0.7 or centro > 0.8:
        if centro < 0.7:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 0.8:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    initials1 = [gama, centro, -7, 58, 37]

# Otimização para realizar o fit da função a partir dos dados e palpites iniciais e cálculo da incerteza e dos parâmetros da função.
    best, covariance = curve_fit(fit, x, y, p0=initials1, sigma=np.sqrt(y))
    error = np.sqrt(np.diag(covariance))
    
    while abs(initials1[0]-best[0]) > 0.00001 or abs(initials1[1]-best[1]) > 0.00001:
        initials1[0] = best[0]
        initials1[1] = best[1]
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
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    print(" ")
    while centro < 0.95 or centro > 1.05:
        if centro < 0.8:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 1.04:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    
    while abs(initials2[0]-best[0]) > 0.00001 or abs(initials2[1]-best[1]) > 0.00001:
        initials2[0] = best[0]
        initials2[1] = best[1]
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
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    print(" ")
    while centro < 2.99 or centro > 3.15:
        if centro < 2.99:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 3.15:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    
    while abs(initials3[0]-best[0]) > 0.00001 or abs(initials3[1]-best[1]) > 0.00001:
        initials3[0] = best[0]
        initials3[1] = best[1]
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
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    print(" ")
    while centro < 3.6 or centro > 3.75:
        if centro < 3.6:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 3.75:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    
    while abs(initials4[0]-best[0]) > 0.00001 or abs(initials4[1]-best[1]) > 0.00001:
        initials4[0] = best[0]
        initials4[1] = best[1]
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
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    print(" ")
    while centro < 9.25 or centro > 9.6:
        if centro < 9.25:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 9.8:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))    
   
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    
    while abs(initials5[0]-best[0]) > 0.00001 or abs(initials5[1]-best[1]) > 0.00001:
        initials5[0] = best[0]
        initials5[1] = best[1]
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
    x = 0.5*(histogram[1][0:-1] + histogram[1][1:])
    
    centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
    while centro < 83.0 or centro > 98.0:
        if centro < 83.0:
            print('Que pena, não foi dessa vez. Tente um número MAIOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))
        elif centro > 98.0:
            print('Que pena, não foi dessa vez. Tente um número MENOR!')
            centro = float(input("Qual o seu palpite inicial para a posição do pico? "))   
            
    gama = float(input("Qual o seu palpite inicial para a largura à meia altura do pico? "))
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
    
    while abs(initials6[0]-best[0]) > 0.00001 or abs(initials6[1]-best[1]) > 0.00001:
        initials6[0] = best[0]
        initials6[1] = best[1]
        best, covariance = curve_fit(fit, x, y, p0=initials6, sigma=np.sqrt(y))
        error = np.sqrt(np.diag(covariance))
    
# Impressão dos valores e incertezas dos parâmtros do fit.
print("Valores e incertezas do fit da função:")
print("")
first = "Largura à meia altura: gama = {} +- {}".format(round(best[0], 4), round(error[0], 4))
second = "Valor do máximo da distribuição: M = {} +- {}".format(round(best[1], 5), round(error[1], 5))
third = "a = {} +- {}".format(round(best[2], 2), round(error[2], 2))
fourth = "b = {} +- {}".format(round(best[3], 4), round(error[3], 4))
fifth = "A = {} +- {}".format(round(best[4], 4), round(error[4], 4))
print(first)
print(second)
print(third)
print(fourth)
print(fifth)

plt.plot(x, fit(x, *best), 'r-', label='gama = {}, M = {}'.format(best[0], best[1]))
plt.xlabel('Massa Invariante [GeV]')
plt.ylabel('Número de eventos')
plt.title('Fit da Função')
plt.show()

#Realização do teste estatístico qui-quadrado

z = [fit(lowerlimit, best[0], best[1], best[2], best[3], best[4])]

for i in range(bins - 1):
    
    k = lowerlimit + (i+1)*(upperlimit - lowerlimit)/bins
    l = fit(k, best[0], best[1], best[2], best[3], best[4])
    z.append(l)
    
divergencia, valorp = chisquare(f_obs = y, f_exp = z)
div = divergencia/(bins - 5)                           # (bins - 5) é o número de graus de liberdade, sendo 5 o número de parâmatros da função de fit.
    
print(" ")
print("Uma maneira de avaliar o fit realizado é através do valor do teste de estatística qui-quadrado.")
print("Quanto menor seu valor, maior é a qualidade do fit realizado.")
print("Neste caso, o qui-quadrado encontrado, por grau de liberdade, é: ", round(div, 4))
print(" ")

#Comparação com dados da literatura (referências ao fim do script)
print("Comparando com dados disponíveis na literatura, tem-se:")
print(" ")

ρ_ω_ref = 0.778955                # [1,2]
ρ_ω_ref_error = 0.00028           # [1,2]
Φ_ref = 1.019461                  # [3]
Φ_ref_error = 0.000016            # [3]
J_Ψ_ref = 3.096900                # [4]
J_Ψ_ref_error = 0.000006          # [4]
Ψ1_ref = 3.686097                 # [5]
Ψ1_ref_error = 0.000025           # [5]
Y_ref = 9.46030 		  # [6]	
Y_ref_error = 0.00026             # [6]
Z_ref = 91.1876                   # [7]
Z_ref_error = 0.0021              # [7]

if pico == 1:
    print("A massa de ρ,ω esperada é (", ρ_ω_ref, "±", ρ_ω_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 5), "±", round(error[1], 5),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(ρ_ω_ref - best[1])/ρ_ω_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*ρ_ω_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")

if pico == 2:
    print("A massa de Φ esperada é (", Φ_ref, "±", Φ_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 5), "±", round(error[1], 5),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(Φ_ref - best[1])/Φ_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Φ_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")

if pico == 3:
    print("A massa de J/Ψ esperada é (", J_Ψ_ref, "±", J_Ψ_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 5), "±", round(error[1], 5),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(J_Ψ_ref - best[1])/J_Ψ_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*J_Ψ_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")
        
if pico == 4:
    print("A massa de Ψ' esperada é (", Ψ1_ref, "±", Ψ1_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 4), "±", round(error[1], 4),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(Ψ1_ref - best[1])/Ψ1_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Ψ1_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")
        
if pico == 5:
    print("A massa de Y esperada é (", Y_ref, "±", Y_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 4), "±", round(error[1], 4),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(Y_ref - best[1])/Y_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Y_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")

if pico == 6:
    print("A massa de Z esperada é (", Z_ref, "±", Z_ref_error, ") GeV/c²")
    print("A presente análise forneceu o valor de (", round(best[1], 3), "±", round(error[1], 3),") GeV/c²")
    print("A discrepância encontrada foi de", round(100*abs(Z_ref - best[1])/Z_ref, 2), "%")
    if abs(Z_ref - best[1]) <= 3*error[1] + 3*Z_ref_error:
        print("E considerando o intervalo de incerteza, o resultado é compatível com o esperado.")
        print(" ")
    else:
        print("E, mesmo considerando o resultado das incertezas, o resultado encontrado não é compatível com o esperado.")
        print(" ")
        

# [1] http://pdg.lbl.gov/2018/listings/rpp2018-list-rho-770.pdf
# [2] http://pdg.lbl.gov/2018/listings/rpp2018-list-omega-782.pdf
# [3] http://pdg.lbl.gov/2018/listings/rpp2018-list-phi-1020.pdf
# [4] http://pdg.lbl.gov/2018/listings/rpp2018-list-J-psi-1S.pdf
# [5] http://pdg.lbl.gov/2018/listings/rpp2018-list-psi-2S.pdf
# [6] http://pdg.lbl.gov/2018/listings/rpp2018-list-upsilon-1S.pdf
# [7] http://pdg.lbl.gov/2018/listings/rpp2018-list-z-boson.pdf
