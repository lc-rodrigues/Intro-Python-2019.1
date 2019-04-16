

#FALTAM G, K, W e X

import turtle
import math

def draw_A_(t, altura):
    linha=altura/(math.sin(math.radians(70)))
    corte = (linha**2 - altura**2)**0.5
    t.left(70)
    t.forward(linha)
    t.right(140)
    t.forward(linha/2)
    t.right(110)
    t.forward(corte)
    t.backward(corte)
    t.left(110)
    t.forward(linha/2)
    
def draw_B_(t, altura):
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/4)
    t.left(180)
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/4)
    t.left(90)
    t.forward(1.05*altura)
    
def draw_C_(t, altura):
    t.left(180)
    t.forward(altura/4)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/2)/90)
    t.forward(altura/4)
    
def draw_D_(t, altura):
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/2)/90)
    t.forward(altura/4)
    t.left(90)
    t.forward(altura)

def draw_E_(t, altura):
    for i in range(2):
        t.forward(altura/2)
        t.backward(altura/2)
        t.left(90)
        t.forward(altura/2)
        t.right(90)
    t.forward(altura/2)
    
def draw_F_(t, altura):
    for i in range(2):
        t.left(90)
        t.forward(altura/2)
        t.right(90)
        t.forward(altura/2)
        t.backward(altura/2)
    
def draw_H_(t, altura):
    t.left(90)
    t.forward(altura)
    t.backward(altura/2)
    t.right(90)
    t.forward(altura/2)
    t.left(90)
    t.forward(altura/2)
    t.backward(altura)
    
def draw_I_(t, altura):
    t.forward(altura/4)
    t.backward(altura/8)
    t.left(90)
    t.forward(altura)
    t.left(90)
    t.forward(altura/8)
    t.backward(altura/4)
    
def draw_J_(t, altura):
    t.penup()
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.pendown()
    t.backward(altura/6)
    t.forward(altura/3)
    t.backward(altura/6)
    t.right(90)
    t.forward(4*altura/5)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/5)/90)
        
def draw_L_ (t, altura):
    t.forward(altura/2)
    t.backward(altura/2)
    t.left(90)
    t.forward(altura)
    
def draw_M_ (t, altura):
    t.left(90)
    t.forward(altura)
    t.right(135)
    t.forward(2**0.5*altura/3)
    t.left(90)
    t.forward(2**0.5*altura/3)
    t.right(135)
    t.forward(altura)
    
def draw_N_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(135)
    t.forward(2**0.5*altura)
    t.left(135)
    t.forward(altura)
    
def draw_O_ (t, altura):
    for i in range(45):
        t.left(2)
        t.forward(2*math.pi*(altura/4)/180)
    t.forward(altura/2)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/2)
    for i in range(45):
        t.left(2)
        t.forward(2*math.pi*(altura/4)/180)
        
def draw_P_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(altura/4)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/4)
    
def draw_Q_ (t, altura):
    for i in range(45):
        t.left(2)
        t.forward(2*math.pi*(altura/4)/180)
    t.forward(altura/2)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/2)
    for i in range(45):
        t.left(2)
        t.forward(2*math.pi*(altura/4)/180)
    t.penup()
    t.left(90)
    t.forward(altura/6)
    t.right(120)
    t.pendown()
    t.forward(altura/3.5)
    
def draw_R_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(altura/4)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/4.1)
    t.left(135)
    t.forward((altura*2**0.5)/2)
    
def draw_S_(t, altura):
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/5)
    
def draw_T_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.backward(altura/3)
    t.forward(2*altura/3)
    
def draw_U_(t, altura):
    t.penup()
    t.left(90)
    t.forward(altura)
    t.left(180)
    t.pendown()
    t.forward(3*altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(3*altura/4)
        
def draw_V_(t, altura):
    t.penup()
    t.left(90)
    t.forward(altura)
    t.right(180 - math.degrees(math.atan(1/2)))
    t.pendown()
    t.forward(5**0.5*altura/2)
    t.left(180 - math.degrees(math.atan(2)))
    t.forward(5**0.5*altura/2)
    
def draw_Y_(t, altura):
    t.left(90)
    t.forward(altura/2)
    t.left(45)
    t.forward(2**0.5*altura/2)
    t.backward(2**0.5*altura/2)
    t.right(90)
    t.forward(2**0.5*altura/2)
    
def draw_Z_(t, altura):
    t.forward(altura/2)
    t.backward(altura/2)
    t.left(math.degrees(math.atan(2)))
    t.forward(5**0.5*altura/2)
    t.left(180 - math.degrees(math.atan(2)))
    t.forward(altura/2)
    


janela = turtle.Screen()
alfabeto = turtle.Turtle()
alfabeto.shape("turtle")
draw_R_(alfabeto, 200)



janela.mainloop()

           