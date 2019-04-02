import turtle             # nos permite usar as tartarugas (turtles)

cor = input("Que cor gostaria que que fosse sua janela?    ")

jn = turtle.Screen()      # Abre uma janela onde as tartarugas vão caminhar
jn.bgcolor(cor)           # Associa a resposta gravada na variável cor para a cor de fundo da janela

joana = turtle.Turtle()    # Cria uma tartaruga, atribui a joana

joana.forward(50)          # diz para joana andar para frente por 50 unidades
joana.left(90)             # diz para joana virar de 90 graus
joana.forward(30)          # Completa o segundo lado do retângulo

jn.mainloop()             # Espera o usuário fechar a janela
