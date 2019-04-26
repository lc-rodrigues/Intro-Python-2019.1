import math

def check_fermat(a, b, c, n):
    
    """O Teorema de Fermat diz que não existem números inteiros a, b e c
    tais que a**n + b**n == c**n, para qualquer n > 2.
    Esta função serve para checar este teorema."""
    
    if n > 2 and a**n + b**n == c**n:
        print("Holly Smokes, Fermat was Wrong")
    elif n > 2 and a**n + b**n != c**n:
        print("No, that doesn't work")
    elif n <= 2:
        print("n deve ser igual ou maior a 2")
        
def pergunte():
    a = int(input("Qual o número que será a primeira para testar o Teorema de Fermat? "))
    b = int(input("Qual o número que será a segunda base? "))
    c = int(input("Qual o número que será a terceira base? "))
    n = int(input("E qual será o expoente? "))
    print(" ")
    check_fermat (a, b, c, n)

pergunte()
