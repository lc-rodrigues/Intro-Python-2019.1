import math
import time

tempo = time.time()

dia = 24*60*60               # número de segundos em 1 dia
ano = 365*dia                # número de segundos em um ano

ano_atual = 1970 + tempo//ano                                           # Cálculo do ano atual
n_bissextos = (ano_atual - 1968)//4  - 1                                # Cálculo do número de anos bissextos de 1970 até o presente, menos o ano 2000 que não foi bissexto
dias_deste_ano = (tempo - ((tempo//ano)*ano))//dia - n_bissextos        # Cálculo do números de dias passados no ano atual
hora_atual = (tempo - (tempo//(dia)*(dia)))//3600 - 3                   # Cálculo do número de horas passadas no dia atual
minuto_atual = (tempo - (tempo//3600)*3600)//60                         # Cálculo do número de minutos passados na hora atual
segundo_atual = (tempo - (tempo//60)*60)                                # Cálculo do número de segundos passados no minuto atual

mes_atual
dia_atual = 0

if ((ano_atual - 1968) % 4) == 0:                               # Condicionais para aferir mês e dia do mês para quando o ano é bissexto
    if dias_deste_ano < 31:
        mes_atual = "janeiro"
        dia_atual = dias_deste_ano
    elif dias_deste_ano > 31 and dias_deste_ano <= 60:
        mes_atual = "fevereiro"
        dia_atual = dias_deste_ano - 31
    elif dias_deste_ano > 60 and dias_deste_ano <=91:
        mes_atual = "março"
        dia_atual = dias_deste_ano - 60
    elif dias_deste_ano > 91 and dias_deste_ano <=121:
        mes_atual = "abril"
        dia_atual = dias_deste_ano - 91
    elif dias_deste_ano > 121 and dias_deste_ano <=152:
        mes_atual = "maio"
        dia_atual = dias_deste_ano - 121
    elif dias_deste_ano > 152 and dias_deste_ano <=182:
        mes_atual = "junho"
        dia_atual = dias_deste_ano - 152        
    elif dias_deste_ano > 182 and dias_deste_ano <=213:
        mes_atual = "julho"
        dia_atual = dias_deste_ano - 182
    elif dias_deste_ano > 213 and dias_deste_ano <=244:
        mes_atual = "agosto"
        dia_atual = dias_deste_ano - 213
    elif dias_deste_ano > 244 and dias_deste_ano <=274:
        mes_atual = "setembro"
        dia_atual = dias_deste_ano - 244
    elif dias_deste_ano > 274 and dias_deste_ano <=305:
        mes_atual = "outubro"
        dia_atual = dias_deste_ano - 274
    elif dias_deste_ano > 305 and dias_deste_ano <=335:
        mes_atual = "novembro"
        dia_atual = dias_deste_ano - 305
    elif dias_deste_ano > 335:
        mes_atual = "dezembro"
        dia_atual = dias_deste_ano - 335
    
    
else:
    if dias_deste_ano < 31:                                               # Condicionais para aferir mês e dia do mês para quando o ano não é bissexto
        mes_atual = "janeiro"
        dia_atual = dias_deste_ano
    elif dias_deste_ano > 31 and dias_deste_ano <=59:
        mes_atual = "fevereiro"
        dia_atual = dias_deste_ano - 31
    elif dias_deste_ano > 59 and dias_deste_ano <=90:
        mes_atual = "março"
        dia_atual = dias_deste_ano - 59
    elif dias_deste_ano > 90 and dias_deste_ano <=120:
        mes_atual = "abril"
        dia_atual = dias_deste_ano - 90
    elif dias_deste_ano > 120 and dias_deste_ano <=151:
        mes_atual = "maio"
        dia_atual = dias_deste_ano - 120
    elif dias_deste_ano > 151 and dias_deste_ano <=181:
        mes_atual = "junho"
        dia_atual = dias_deste_ano - 151
    elif dias_deste_ano > 181 and dias_deste_ano <=212:
        mes_atual = "julho"
        dia_atual = dias_deste_ano - 181
    elif dias_deste_ano > 212 and dias_deste_ano <=243:
        mes_atual = "agosto"
        dia_atual = dias_deste_ano - 212
    elif dias_deste_ano > 243 and dias_deste_ano <=273:
        mes_atual = "setembro"
        dia_atual = dias_deste_ano - 243
    elif dias_deste_ano > 273 and dias_deste_ano <=304:
        mes_atual = "outubro"
        dia_atual = dias_deste_ano - 373
    elif dias_deste_ano > 304 and dias_deste_ano <=334:
        mes_atual = "novembro"
        dia_atual = dias_deste_ano - 304
    elif dias_deste_ano > 334:
        mes_atual = "dezembro"
        dia_atual = dias_deste_ano - 334


if hora_atual == -3.0:                  # Conversão necessária devido à diferença de fuso horário
    hora_atual = 21
    dia_atual = dia_atual - 1
elif hora_atual == -2.0:
    hora_atual = 22
    dia_atual = dia_atual - 1
elif hora_atual == -1.0:
    hora_atual = 23
    dia_atual = dia_atual - 1
    
print("Hoje é dia", round(dia_atual), "de", mes_atual, "de", round(ano_atual))
print(" ")
print("A hora atual é ", round(hora_atual), ":", round(minuto_atual), ":", round(segundo_atual))