import turtle
def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
   # t.forward(10)


lista = input("Digite as frequências do histograma separadas por espaços. Exemplo: 10 20 40 70 15   ")
cor_fundo = input("Qual cor gostaria que fosse o fundo da sua janela?   ")
cor_linha = input("Qual cor gostaria que fosse a linha do seu histograma?   ")
cor_barra = input("Qual cor gostaria que fosse o preenchimento das barras do histograma?   ")


wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor(cor_fundo)

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color(cor_linha, cor_barra)
tess.pensize(3)

#xs = [48,117,200,240,160,260,220]

list = lista.split()

for a in list:
    draw_bar(tess, a)

wn.mainloop()
