import turtle
import math

def flor(t, r, n):

    t.penup()                              # reposiciona o cursor
    t.goto(0, -2*r)
    t.pendown()
    t.left(120)
    t.shape("turtle")

    t.color("green")                       # desenha metade do talo
    t.pensize(5)
    
    for i in range(15):
        t.forward(4*r*4*math.pi/360)
        t.right(2)

    t.right(135)                            # desenha a folha

    t.pensize(2)
    t.color("grey", "green")
    t.begin_fill()
    
    for i in range(45):                
        t.forward(0.75*r*4*math.pi/360)
        t.left(2)

    t.left(90)

    for i in range(45):
        t.forward(0.75*r*4*math.pi/360)
        t.left(2)

    t.right(135)                             
    t.end_fill()

    t.color("green")                        # desenha a outra metade do talo
    t.pensize(5)
    
    for i in range(15):                
        t.forward(4*r*4*math.pi/360)
        t.right(2)

    t.right(90)                             # desenha as n pétalas
    t.pensize(3)
    t.color("red", "magenta")
    t.begin_fill()
    
    for j in range(n):                     
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
        
        t.left(180 - (360/n))
    
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
      
        t.left(180)
    t.end_fill()
    t.hideturtle()
 

tela = turtle.Screen()
tela.bgcolor("lightblue")
tartaruga = turtle.Turtle()
flor(tartaruga, 70, 5)
tc= turtle.Screen().getcanvas()
tc.postscript(file="flor-LuizCarlos.ps")

tela.mainloop()
