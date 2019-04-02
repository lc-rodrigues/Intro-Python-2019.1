import turtle
import math

def circle(t, r):
    t.right(90)
    t.forward(r)
    t.left(90)
    for i in range(360):
        t.left(1)
        t.forward(2*math.pi*r/360)
        
janela = turtle.Screen()
joana = turtle.Turtle()
circle(joana, 100)

janela.mainloop()
    
