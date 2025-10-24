# Fonction qui affiche si deux nombres sont de même signe ou de signes contraires
def signe_meme ( A, B ) :
    if A * B > 0 :
        print(f"\n{A} et {B} sont de meme signe.")
    elif A * B < 0 :
        print(f"\n{A} et {B} sont de signe contraire.")
    else :
        if A == 0 and B == 0 :
            print(f"\n{A} et {B} sont nuls.")
        elif A == 0 :
            print(f"\n{A} est nul et {B} est non nul.")
        else :
            print(f"\n{A} est non nul et {B} est nul.")

# Fonction qui retourne le maximum entre deux nombres
def the_max ( A, B ) :
    if A > B :
        return A
    else :
        return B

# Fonction qui retourne le minimum entre deux nombres
def the_min ( A, B ) :
    if A < B :
        return A
    else :
        return B

# Fonction de saisie d'un nombre flottant
def saisir ( msg = "premier nombre" ) :
    try :
        nombre = int ( input (f"\nSaisir le {msg} : ") )
    except ValueError :
        print ("Entrée invalide !!!, veuillez entrer un entier.")
        return saisir ( msg )
    return nombre