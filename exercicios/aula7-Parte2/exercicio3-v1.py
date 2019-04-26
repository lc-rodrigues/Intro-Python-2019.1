def is_triangle(x, y, z):
    if x >= y + z or y >= x + z or z >= x + y:
        print("No")
    else:
        print("Yes")
        
is_triangle(3, 3, 3)