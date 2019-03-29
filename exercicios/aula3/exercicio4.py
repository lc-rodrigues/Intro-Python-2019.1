def milha_metro (milha):                     #função que converte milhas em metros
    x = milha*1609
    return x

def metro_milha (metro):                    #função que converte metros em milhas
    y = metro/1609
    return y

def hora_seg (hora):                        #função que converte horas em segundos
    w = hora*3600
    return w

def seg_hora (segundo):                    #função que converte segundos em horas
    z = segundo/3600
    return z


print('Exercício 1 da aula 1:')
print(' ')

t = 43.5/(metro_milha(10000))
v = (metro_milha(10000))/seg_hora(43.5*60)
print('O tempo médio por milha é,', round(t,2), 'minutos')
print('A velocidae média é', round(v,1), 'milhas/hora')
print(' ')

print(' ')
print('Exercício 4 da aula 3:')
print(' ')

v2 = (milha_metro(4)/1000)/(seg_hora(30*60))
t2 = 30/(milha_metro(4)/1000)

print(' A velocidae média é', round(v2,1), 'km/h e o tempo médio por Km é', round(t2,2), 'minutos')
