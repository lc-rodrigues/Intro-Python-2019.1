def recurse(n, s):
    """Se n é negativo, a função entra em loop infinito.
       Se n = 0, a função imprime s.
       Se n é positivo, a função imprime s + n(n+1)/2"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)