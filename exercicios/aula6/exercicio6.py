import turtle              # nos permite usar as tartarugas (turtles)

cor_fundo = input("Que cor gostaria que que fosse sua janela?    ")
cor_linha = input("Que cor gostaria que fossem suas linhaa?    ")
largura = input("Considerando 1 o mais fino possível, quão largas gostaria que fossem suas linhas?   ")

jn = turtle.Screen()       # Abre uma janela onde as tartarugas vão caminhar
jn.bgcolor(cor_fundo)      # Associa a resposta gravada na variável cor_fundo à cor de fundo da janela

joana = turtle.Turtle()    # Cria uma tartaruga, atribui a joana

joana.color(cor_linha)     # Associa a resposta gravada na variável cor_linha à cor da linha
joana.pensize(largura)     # Associa a resposta gravada na variável largura à largura da linha
joana.shape("turtle")      # Define a forma do cursor como turtle
joana.speed(10)            # Define a velocidade com que o cursor desenha as linhas

joana.color(cor_fundo)    # Instruções para posicionar o cursor, sem desenhar na tela
joana.backward(200)
joana.left(90)
joana.forward(200)
joana.right(90)
joana.color(cor_linha)
joana.speed(2)

for i in range(5):         # Loop para desenhar a primeira estrela
    joana.forward(100)
    joana.right(144)

joana.forward(103)        # Instruções para afastar o cursor, sem desenhar na tela
joana.color(cor_fundo)
joana.forward(200)
joana.color(cor_linha)
           

for i in range(5):         # Loop para desenhar a segunda estrela
    joana.forward(100)
    joana.right(144)

joana.backward(3)
joana.color(cor_fundo)
joana.right(90)
joana.forward(300)
joana.left(90)
joana.color(cor_linha)

for i in range(5):         # Loop para desenhar a terceira estrela
    joana.forward(100)
    joana.right(144)

joana.backward(3)
joana.color(cor_fundo)     # Instruções para afastar o cursor, sem desenhar na tela
joana.backward(300)
joana.color(cor_linha)

for i in range(5):         # Loop para desenhar a quarta estrela
    joana.forward(100)
    joana.right(144)

joana.backward(3)
joana.color(cor_fundo)     # Instruções para afastar o cursor, sem desenhar na tela
joana.left(90)
joana.forward(140)
joana.right(90)
joana.forward(210)
joana.left(90)
joana.color(cor_linha)


jn.mainloop()             # Espera o usuário fechar a janela
