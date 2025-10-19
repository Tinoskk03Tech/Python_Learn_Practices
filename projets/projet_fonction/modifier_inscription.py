from inscription import saisir_age
# Fonction de modification des informations d'inscription d'un élève
def modifier_inscription () :
    # Globalisation des variables utilisées
    global nom, prenom, age, classe, etablissement, bourse
    # Message d'affichage de la modification des informations
    print("MODIFICATION DES INFORMATIONS")
    print(f"{'='*28}")
    # Affichage et modification du nom actuelle
    print(f"Nom actuel : {nom}")
    nom = input("Nouveau nom : ")
    # Affichage et modification du prénom actuelle
    print(f"Prénom actuel : {prenom}")
    prenom = input("Nouveau prénom : ")
    # Affichage et modification de l'age actuelle
    print(f"Âge actuel : {age}")
    age = saisir_age()
    # Affichage et modification de la classe actuelle
    print(f"Classe actuelle : {classe}")
    classe = input("Nouvelle classe : ")
    # Affichage et modification de l'établissement actuelle
    print(f"Établissement actuel : {etablissement}")
    etablissement = input("Nouvel établissement : ")
    # Affichage et modification du type de bourse actuelle
    print(f"Type de bourse actuel : {bourse}")
    bourse = input("Nouveau type de bourse : ")
    # Message de confirmation de la modification des informations
    print("\nINFORMATIONS MODIFIÉES AVEC SUCCÈS !")
