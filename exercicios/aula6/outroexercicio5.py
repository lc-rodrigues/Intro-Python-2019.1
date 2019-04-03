import turtle
import math

def arc(t, r, angle):                   
    t.forward(r)                           #desenhar o raio e posicionar o cursor
    t.left(90)
    for i in range(angle):                 #loop para desenhar o arco de círculo
        t.left(1)
        t.forward(2*math.pi*r/360)
    t.left(90)                             #reposicionar o cursor na posição inicial
    t.forward(r)
    t.left(180-angle)
        
janela = turtle.Screen()                  
joana = turtle.Turtle()
arc(joana, 150, 330)

janela.mainloop()
