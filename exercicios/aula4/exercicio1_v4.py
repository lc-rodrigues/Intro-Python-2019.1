def soma(x,y):
    s=x+y
    return s
    
def do_twice(f,g): 
    f (g)
    f (g)

def print_twice(palavra): 
    print(palavra) 
    print(palavra)

def do_four(f,g):
    do_twice (f,g)
    do_twice (f,g)

do_four(print_twice, soma(2,3))
