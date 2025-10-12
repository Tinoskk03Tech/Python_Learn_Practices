print("Hello world !")

"""while True :
    try :
        nombre = int(input("Veuillez entrer un nombre : "))
        break
    except ValueError :
        print("Vous n'avez pas entré un nombre valide.")"""

def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())