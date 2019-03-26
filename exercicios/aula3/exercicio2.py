def vel (xi, xf, t):
    v = (xf-xi)/t
    print('Posição inicial = ', xi, 'm')
    print('Posição final = ', xf, 'm')
    print('Tempo transcorrido = ', t, 's')
    print('A velocidade média é', v,  'm/s')

vel(0, 10, 5)

def vel_ac (v0, t, a):
    v = v0 + a*t
    print('Se o objeto estiver acelerado com a = ', a, 'm/(s*s):'
    print('Velocidade inicial = ', v0, 'm')
    print('Posição final = ', xf, 'm')
    print('Tempo transcorrido = ', t, 's')
    print('A velocidade média é', v,  'm/s')
    

