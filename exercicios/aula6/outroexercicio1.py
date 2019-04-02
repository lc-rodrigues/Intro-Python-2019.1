import turtle

def square(t):
    for i in range(4):
        t.forward(100)
        t.left(90)

janela = turtle.Screen()
joana = turtle.Turtle()
square(joana)

janela.mainloop()
    
