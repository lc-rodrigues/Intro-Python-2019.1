import turtle
import math

def flor(t, r, n):

    """Desenha flores com tamanho r e n pétalas."""
    
    m = n//2
    for j in range(n):
        for i in range(180//m):
            t.forward(r*4*math.pi/360)
            t.left(2)
        
        t.left(180 - (360/m))
    
        for i in range(180//m):
            t.forward(r*4*math.pi/360)
            t.left(2)
      
        t.left(180)
        t.right(180/m)

tela = turtle.Screen()
tartaruga = turtle.Turtle()
flor(tartaruga, 200, 10)

tela.mainloop()

        
        
