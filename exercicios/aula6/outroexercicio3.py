import turtle

def polygon(t, length, n):
    for i in range(n):
        t.forward(length)
        t.left(360/n)

janela = turtle.Screen()
joana = turtle.Turtle()
polygon(joana, 50, 8)

janela.mainloop()
    
