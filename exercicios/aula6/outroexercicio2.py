import turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.left(90)

janela = turtle.Screen()
joana = turtle.Turtle()
square(joana, 300)

janela.mainloop()
    
