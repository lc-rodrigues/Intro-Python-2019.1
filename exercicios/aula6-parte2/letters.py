
import turtle
import math

"""Todas as funções a seguir são para desenhar as letras do alfabeto e mais alguns itens. Cada uma delas possui um nome autoexplicativo"""

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
    t.left(70)
    t.penup()
    t.forward(altura/4)
    t.pendown()
    
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
    t.left(90)
    t.penup()
    t.forward(3*altura/4)
    t.pendown()
    
def draw_C_(t, altura):
    t.penup()
    t.forward(3*altura/4)
    t.left(180)
    t.pendown()
    t.forward(altura/4)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/2)/90)
    t.forward(altura/4)
    t.penup()
    t.forward(altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.forward(altura/4)
    t.pendown()
    
    
def draw_D_(t, altura):
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/2)/90)
    t.forward(altura/4)
    t.left(90)
    t.forward(altura)
    t.penup()
    t.left(90)
    t.forward(altura)
    t.pendown()

def draw_E_(t, altura):
    for i in range(2):
        t.forward(altura/2)
        t.backward(altura/2)
        t.left(90)
        t.forward(altura/2)
        t.right(90)
    t.forward(altura/2)
    t.penup()
    t.forward(altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.pendown()
    
def draw_F_(t, altura):
    for i in range(2):
        t.left(90)
        t.forward(altura/2)
        t.right(90)
        t.forward(altura/2)
        t.backward(altura/2)
    t.penup()
    t.forward(3*altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.pendown()

def draw_G_(t, altura):
    t.penup()
    t.forward(altura/2)
    t.pendown()
    for i in range(90):
        t.left(1)
        t.forward(2*math.pi*(altura/2.5)/360)
    t.left(90)
    t.forward(altura/4)
    t.backward(altura/4)
    t.left(90)
    for i in range(180):
        t.right(1)
        t.forward(2*math.pi*(altura/2.5)/360)
    t.forward(altura/5)
    for i in range(180):
        t.right(1)
        t.forward(2*math.pi*(altura/2.5)/360)
    t.penup()
    t.forward(altura/(5/3))
    t.left(90)
    t.forward(altura/4)
    t.pendown()
            
def draw_H_(t, altura):
    t.left(90)
    t.forward(altura)
    t.backward(altura/2)
    t.right(90)
    t.forward(altura/2)
    t.left(90)
    t.forward(altura/2)
    t.backward(altura)
    t.penup()
    t.right(90)
    t.forward(altura/4)
    t.pendown()
    
def draw_I_(t, altura):
    t.forward(altura/4)
    t.backward(altura/8)
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.backward(altura/8)
    t.forward(altura/4)
    t.penup()
    t.forward(altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.pendown()
    
def draw_J_(t, altura):
    t.penup()
    t.forward(altura/2.5)
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
    t.penup()
    t.backward(altura/5)
    t.right(90)
    t.forward(47*altura/60)
    t.pendown()

def draw_K_(t, altura):
    t.left(90)
    t.forward(altura)
    t.backward(altura/2)
    t.right(45)
    t.forward(altura/2**0.5)
    t.backward(altura/2**0.5)
    t.right(90)
    t.forward(altura/2**0.5)
    t.penup()
    t.left(45)
    t.forward(altura/4)
    t.pendown()
        
def draw_L_ (t, altura):
    t.left(90)
    t.forward(altura)
    t.backward(altura)
    t.right(90)
    t.forward(altura/2)
    t.penup()
    t.forward(altura/4)
    t.pendown()
    
def draw_M_ (t, altura):
    t.left(90)
    t.forward(altura)
    t.right(135)
    t.forward(2**0.5*altura/3)
    t.left(90)
    t.forward(2**0.5*altura/3)
    t.right(135)
    t.forward(altura)
    t.penup()
    t.left(90)
    t.forward(altura/4)
    t.pendown()
    
def draw_N_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(135)
    t.forward(2**0.5*altura)
    t.left(135)
    t.forward(altura)
    t.penup()
    t.backward(altura)
    t.right(90)
    t.forward(altura/4)
    t.pendown()
    
def draw_O_ (t, altura):
    t.penup()
    t.forward(altura/4)
    t.pendown()
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
    t.forward(altura/2)
    t.pendown()
        
def draw_P_(t, altura):
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.forward(altura/4)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/4)
    t.penup()
    t.left(90)
    t.forward(altura/2)
    t.left(90)
    t.forward(3*altura/4)
    t.pendown()
    
def draw_Q_ (t, altura):
    t.penup()
    t.forward(altura/4)
    t.pendown()
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
    t.forward(altura/3.2)
    t.penup()
    t.left(30)
    t.forward(altura/3)
    t.pendown()
    
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
    t.penup()
    t.left(45)
    t.forward(altura/4)
    t.pendown()
    
def draw_S_(t, altura):
    t.forward(altura/4)
    for i in range(45):
        t.left(4)
        t.forward(2*math.pi*(altura/4)/90)
    for i in range(45):
        t.right(4)
        t.forward(2*math.pi*(altura/4)/90)
    t.forward(altura/5)
    t.penup()
    t.forward(altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.pendown()
    
def draw_T_(t, altura):
    t.penup()
    t.forward(altura/3)
    t.pendown()
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.backward(altura/3)
    t.forward(2*altura/3)
    t.penup()
    t.forward(altura/4)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.pendown()
    
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
    t.penup()
    t.backward(altura)
    t.right(90)
    t.forward(altura/4)
    t.pendown()
        
def draw_V_(t, altura):
    t.penup()
    t.left(90)
    t.forward(altura)
    t.right(150)
    t.pendown()
    t.forward(altura*2/3**0.5)
    t.left(120)
    t.forward(altura*2/3**0.5)
    t.penup()
    t.right(150)
    t.forward(altura)
    t.left(90)
    t.forward(altura/4)
    t.pendown()

def draw_W_(t, altura):
    t.penup()
    t.forward(altura/2)
    t.pendown()
    t.left(120)
    t.forward(2*altura/3**0.5)
    t.backward(2*altura/3**0.5)
    t.right(60)
    t.forward(altura/2)
    t.right(120)
    t.forward(altura/2)
    t.left(120)
    t.forward(2*altura/3**0.5)
    t.penup()
    t.right(150)
    t.forward(altura)
    t.left(90)
    t.forward(altura/4)
    t.pendown()    

def draw_X_(t, altura):
    t.left(45)
    t.forward(altura*2**0.5)
    t.backward((altura/2)*2**0.5)
    t.right(90)
    t.backward((altura/2)*2**0.5)
    t.forward((altura)*2**0.5)
    t.penup()
    t.left(45)
    t.forward(altura/4)
    t.pendown()
    
def draw_Y_(t, altura):
    t.penup()
    t.forward(altura/2)
    t.pendown()
    t.left(90)
    t.forward(altura/2)
    t.left(45)
    t.forward(2**0.5*altura/2)
    t.backward(2**0.5*altura/2)
    t.right(90)
    t.forward(2**0.5*altura/2)
    t.penup()
    t.right(135)
    t.forward(altura)
    t.left(90)
    t.forward(altura/4)
    t.pendown()
    
def draw_Z_(t, altura):
    t.penup()
    t.left(90)
    t.forward(altura)
    t.right(90)
    t.pendown()
    t.forward(altura/2)
    t.right(90 + math.degrees(math.atan(1/2)))
    t.forward(5**0.5*altura/2)
    t.left(180 - math.degrees(math.atan(2)))
    t.forward(altura/2)
    t.penup()
    t.forward(altura/4)
    t.pendown()
    
def draw_space_(t, altura):
    t.penup()
    t.forward(altura/2)
    t.pendown()
    
def draw_comma_and_space_ (t, altura):
    t.right(120)
    t.forward(altura/8)
    t.backward(altura/8)
    t.left(120)
    t.penup()
    t.forward(3*altura/4)
    t.pendown()
    
def draw_exclamation_and_space_ (t, altura):
    for i in range(90):
        t.left(4)
        t.forward(2*math.pi*(altura/20)/90)
    t.penup()
    t.left(90)
    t.forward(altura/5)
    t.pendown()
    t.forward(4*altura/5)
    t.penup()
    t.backward(altura)
    t.right(90)
    t.forward(3*altura/4)
    t.pendown()
    
    
janela = turtle.Screen()        # Cria a janela
alfabeto = turtle.Turtle()      # Cria uma tartaruga
alfabeto.shape("turtle")        # Muda a forma do cursor para tartaruga
alfabeto.penup()                # Recua o cursor para a esquerda para ter mais espaço para digitar
alfabeto.backward(300)
alfabeto.pendown()


draw_O_(alfabeto, 50)
draw_L_(alfabeto, 50)
draw_I_(alfabeto, 50)
draw_V_(alfabeto, 50)
draw_I_(alfabeto, 50)
draw_A_(alfabeto, 50)
draw_comma_and_space_(alfabeto, 50)

draw_T_(alfabeto, 50)
draw_E_(alfabeto, 50)
draw_space_(alfabeto, 50)

draw_A_(alfabeto, 50)
draw_M_(alfabeto, 50)
draw_O_(alfabeto, 50)
draw_exclamation_and_space_(alfabeto, 50)


janela.mainloop()

           
