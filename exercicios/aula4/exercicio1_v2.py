def do_twice(f,g): 
    f (g)
    f (g)

def print_twice(palavra): 
    print(palavra) 
    print(palavra)

do_twice(print_twice, 'spam')

