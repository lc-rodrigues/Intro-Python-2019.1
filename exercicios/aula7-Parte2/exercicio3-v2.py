def is_triangle(x, y, z):
    if x >= y + z or y >= x + z or z >= x + y:
        print("No")
    else:
        print("Yes")
        
def pergunte():
    x = int(input("Qual o primeiro lado do triângulo? "))
    y = int(input("Qual o segundo lado do triângulo? "))
    z = int(input("Qual o terceiro lado do triângulo? "))
    print(" ")
    is_triangle(x, y, z)
    
pergunte()
