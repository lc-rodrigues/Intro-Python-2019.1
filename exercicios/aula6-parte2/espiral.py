import turtle
import math

def draw_espiral(t, n=500, l=3, a=0.05, b=0.0004):
    """
    Desenha uma espiral arquimediana de acordo com alguns parâmetros:
      n: diretamente proporcional ao número de voltas que a espiral terá
      l: quão suave será a espiral. Quanto menor, mais suave; mas também quanto menor l, menor a espiral (para um mesmo n)
      a: diretamente proprocional ao espaço central da espiral
      b: diretamente proporcional ao espaçamento entre as linhas da espiral
    """
    angulo = 0.0

    for i in range(n):
        t.forward(l)
        angulo2 = 1 / (a + b * angulo)
        t.left(angulo2)
        angulo += angulo2


janela = turtle.Screen()
tartaruga = turtle.Turtle()
draw_espiral(tartaruga, n=1000)

janela.mainloop()
