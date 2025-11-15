# Importation des donctions du package fonction
import function as tinos

# Saisie de deux nombres
A = tinos.saisir ( "premier nombre" )
B = tinos.saisir ( "deuxième nombre" )

# Affichage si les deux nombres sont de même signe ou de signes contraires
tinos.signe_meme ( A, B )

# Calcul et affichage du maximum entre les deux nombres
maximum = tinos.the_max ( A, B )
print ( f"\nLe maximum entre {A} et {B} est {maximum}.")

# Calcul et affichage du minimum entre les deux nombres
minimum = tinos.the_min ( A, B )
print ( f"\nLe minimum entre {A} et {B} est {minimum}.")

