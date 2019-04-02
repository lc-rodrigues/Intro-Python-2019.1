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
joana.speed(1)             # Define a velocidade com que o cursor desenha as linhas

for i in range(5):         # Loop para desenhar a estrela
    joana.forward(100)
    joana.right(144)



jn.mainloop()             # Espera o usuário fechar a janela
