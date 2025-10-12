def saisi (position = "premier") :
    while True:
        try:
            nombre = int(input(f"Entrer un {position} nombre : "))
            break
        except ValueError:
            print("Veuillez saisir un entier")
        else:
            nombre = int(input(f"Entrer un {position} nombre : "))
    return nombre


# Afficher le minimum
def minimum (X, Y) :
    min = X
    if X > Y :
        min = Y
    return min

# Afficher le maximum
def maximum (X, Y) :
    max = X
    if X < Y :
        max = Y
    return max

# Afficher le meme signe
def signe_enter (X, Y) :
    if (X * Y > 0) :
        print(f"{X} et {Y} sont du même signe")
    elif (X * Y == 0) :
        if (X == 0) :
            print(f"{X} est nul")
        elif (Y == 0) :
            print(f"{Y} est nul")
        else :
            print(f"{X} et {Y} sont nuls")
    else :
        print(f"{X} et {Y} sont de signe différent")

X = saisi()

Y = saisi("deuxième")

print(f"Le minimum entre {X} et {Y} est {minimum(X, Y)}")

print(f"Le maximum entre {X} et {Y} est {maximum(X, Y)}")

signe_enter(X, Y)