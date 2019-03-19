valor = 24.95                #valor de 1 livro
desconto = 0.4*valor         #valor do desconto em 1 livro
n = 60                       #número de livros comprados
frete1 = 3                   #frete do primeiro livro
frete2 = 0.75                #frete dos demais livros

Total = (valor-desconto)*n + frete1 +(n-1)*frete2

print(' ')
print('O custo total da compra de 60 livros é R$',round(Total,2))
print(' ')
