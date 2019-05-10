import turtle
import math

def flor(t, r, n):

    t.color("black", "pink")
    t.begin_fill()
    
    for j in range(n):                    # desenha as n pétalas
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
        
        t.left(180 - (360/n))
    
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
      
        t.left(180)
    t.end_fill()

    t.right(120)                         # desenha metade do talo

    t.color("green")
    t.pensize(5)
    
    for i in range(20):
        t.forward(4*r*4*math.pi/360)
        t.left(2)

    t.left(45)                            # desenha a folha

    t.pensize(1)
    t.color("black", "green")
    t.begin_fill()
    
    for i in range(45):                
        t.forward(r*4*math.pi/360)
        t.left(2)

    t.left(90)

    for i in range(45):
        t.forward(r*4*math.pi/360)
        t.left(2)

    t.left(45)
    t.end_fill()

    t.color("green")
    t.pensize(5)
    for i in range(20):                 # desenha a outra metade do talo
        t.forward(4*r*4*math.pi/360)
        t.left(2)

tela = turtle.Screen()
tela.bgcolor("yellow")
tartaruga = turtle.Turtle()
flor(tartaruga, 50, 3)

tela.mainloop()

        
        
