a=3 #coeficiente quadrático da equação quadrática
b=-4 #coeficiente linear da equação quadrática
c=-10 #coeficiente independente da equação quadrática

#Cálculo do discriminante

delta = b*b - 4*a*c

#Cálculos das raízes

x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)

print(' ')
print('Uma das raízes da equação y = 3x² - 4x - 10 é x =', round(x1, 1))
print('E a segunda raiz da mesma equação é x =', round(x2, 1))
print(' ')
