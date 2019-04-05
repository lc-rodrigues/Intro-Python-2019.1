import turtle
import math

def poligono(t, l, n):

    """Desenha polígonos regulares com n lados que medem l, divididos em triângulos isósceles"""
    
    r = ((l/2)**2 + ((l/2)/math.tan(math.pi/n))**2)**0.5        #cálculo do raio do polígono inscrito numa circunferência de raio r a partir do lado e da apótema.
    t.left(2*(180-((n-2)*90)//n) - 90)                          #posicionando o cursos inicialmente
    for i in range(n):                                          #loop para desenhar o polígono com as divisões
       t.forward(r)
       t.left(180-((n-2)*90)//n)
       t.forward(l)
       t.left(180-(n-2)*90//n)
       t.forward(r)
       t.left(180)
    t.right(360//n)                                             #reposcionando o cursor após o desenho

tela = turtle.Screen()
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.speed(4)
poligono(tartaruga, 100, 12)



tela.mainloop()

        
        
