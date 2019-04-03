import turtle
import math

def circle(t, r):
    t.forward(r)                            #desenhar o raio e posicionando o cursor
    t.left(90)
    for i in range(90):                     #loop para desenhar o círculo
        t.left(4)
        t.forward(2*math.pi*r/90)
    t.left(90)                              #reposicionar o cursor na posição inicial
    t.forward(r)
    t.left(180)
        
janela = turtle.Screen()
joana = turtle.Turtle()
circle(joana, 200)

janela.mainloop()
