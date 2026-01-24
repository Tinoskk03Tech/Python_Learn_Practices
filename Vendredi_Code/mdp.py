import random

mot_de_passe = "Jpo6#8@_j7"

print(mot_de_passe)

lettre = "ABCDEFJHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*-_?"

mot_de_passe_aleatoire = ""

for i in range(12):
    mot_de_passe_aleatoire += random.choice(lettre)


print(mot_de_passe_aleatoire)



maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
min = "abcdefghijklmnopqrstuvwxyz"
chiffre = "0123456789"
signes = "!@#$%^&*-_?"      

all_char = maj + min + chiffre + signes

def generer_mot_de_passe(longueur):
    mot_de_passe = ""
    for i in range(longueur):
        mot_de_passe += random.choice(all_char)
    return mot_de_passe

print(generer_mot_de_passe(16))