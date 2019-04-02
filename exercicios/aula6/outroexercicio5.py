import turtle
import math

def arc(t, r, angle):
    t.right(90)
    t.forward(r)
    t.left(90)
    for i in range(360):
        t.left(1)
        t.forward(2*math.pi*r/360)
        
janela = turtle.Screen()
joana = turtle.Turtle()
arc(joana, 100)

janela.mainloop()
    
