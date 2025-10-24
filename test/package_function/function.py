def somme ( a, b ) :
    c = a + b
    print(f"{a} + {b} = {c}")
    
def soustraction ( a, b ) :
    c = a - b
    print(f"{a} - {b} = {c}")
    
def multiplication ( a, b ) :
    c = a * b
    print(f"{a} * {b} = {c}")
    
def division ( a, b ) :
    if b != 0 :
        c = a / b
        print(f"{a} / {b} = {c}")
    else :
        print("Erreur : Division par zéro")
        
def aurevoir ( nom ) :
    print(f"Au revoir {nom} !")