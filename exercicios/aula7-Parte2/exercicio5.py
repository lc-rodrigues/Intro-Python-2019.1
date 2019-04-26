import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)
    
janela = turtle.Screen()
tartaruga = turtle.Turtle()

draw(tartaruga, 10, 10)

janela.mainloop()