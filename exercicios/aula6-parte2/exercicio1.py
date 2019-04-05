import turtle
import math

def flor(t, r, n):
    for j in range(n):
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
        
        t.left(180 - (360/n))
    
        for i in range(180//n):
            t.forward(r*4*math.pi/360)
            t.left(2)
      
        t.left(180)

tela = turtle.Screen()
tartaruga = turtle.Turtle()
flor(tartaruga, 200, 9)

tela.mainloop()

        
        
