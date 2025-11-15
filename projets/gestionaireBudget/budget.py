# Fonction de verification de la positivité de nos variables
def isPositif (A, B, C):
    while A < 0:
        if A > 0:
            continue
        else:
            print(f'Votre {C} ne peut pas être negatif')
            A = int(input(B))

# déclaration de  Fonction pour calculer la dépense total
def calculDepenseTotal (A, B, C, D):
    return A + B + C + D

# declaration de Fonction pour le reste du revenu par rapport à la dépense
def calculResteDisponible (A, B):
    return A - B

# déclaration de Fonction pour calculer le pourcentage d'épargne
def calculPourcentageEpargne (A, B):
    return int((A/B)*100)

# Fonction conseil personalisé par ropport à l'épargne de l'utilisateur
def conseilPersonnalise (A):
    if A > 60:
        print(f'Conseil : Excellent ! Tu économises {A} % de tes revenus. \nContinue comme ça, tu peux te faire plaisir ou épargner !')
    elif A > 30:
        print(f'Conseil : C\'est Bien ! Tu économises {A} % de tes revenus. \nÇà peut aller continuie sur ta lancé et n\'oublie tes loisirs')
    else:
        print(f'Conseil : C\'est Passable ! Tu économises {A} % de tes revenus. \nEvite trop de loisir et essaie d\'épargner pôur ton future')

# ===============================
#       PROGRAMME PRINCIPAL
# ===============================


while True:
    # Affichage de l'utilité du programme
    print('\n\n=== GESTIONNAIRE DE BUDGET PERSONNEL ===\n')

    # Affichage d'un message de bienvenue
    print('Bonjour ! Je vais t\'aider à gérer ton budget mensuel.\n')

    # Saisie des informations de l'utilisateur et verification de leur positivité

    revenueMensuel = int(input('💰 Quel est ton revenu mensuel ? '))
    # Appel de la fonction isPositif pour la verication de la positivité du revenueMensuel
    isPositif(revenueMensuel, '💰 Quel est ton revenu mensuel ? ', 'revenue mensuel')

    depenseLogement = int(input('🏠 Combien dépenses-tu pour le logement ? '))
    # Appel de la fonction isPositif pour la verication de la positivité de depenseLogement
    isPositif(depenseLogement, '🏠 Combien dépenses-tu pour le logement ? ', 'depense logement')

    budgetNourriture = int(input('🍕 Budget nourriture mensuel ? '))
    # Appel de la fonction isPositif pour la verication de la positivité de budgetNourriture
    isPositif(budgetNourriture, '🍕 Budget nourriture mensuel ? ', 'budget nourriture')

    budgetTransport = int(input('🚗 Transport (essence, transport public) ? '))

    # Appel de la fonction isPositif pour la verication de la positivité de budgetTransport
    isPositif(budgetTransport, '🚗 Transport (essence, transport public) ? ', 'transport public')

    budgetLoisir = int(input('🎬 Budget loisirs ? '))

    # Appel de la fonction isPositif pour la verication de la positivité de budgetLoisir
    isPositif(budgetLoisir, '🎬 Budget loisirs ? ', 'budget loisir')

    # Affichage du recap du budget à l'utilisateur
    print('\n📊 === RÉCAPITULATIF DE TON BUDGET ===\n')

    print(f'Revenus : {revenueMensuel} Fcfa')

    # Appel et assignation de la fonction calculDepenseTotal
    depenseTotal = calculDepenseTotal(depenseLogement, budgetNourriture, budgetTransport, budgetLoisir)
    print(f'Dépenses totales : {depenseTotal} Fcfa')

    # Appel et assignation de la fonction calculResteDisponilble
    resteDisponible = calculResteDisponible(revenueMensuel, depenseTotal)
    print(f'Reste disponible : {resteDisponible} Fcfa\n')

    #vérification en vue de bien afficher le conseil
    if resteDisponible < revenueMensuel:

        pourcentageEpargne = calculPourcentageEpargne(resteDisponible, revenueMensuel)

        conseilPersonnalise(int(pourcentageEpargne))
    else :
        print(f'Conseil : Danger ! Vous etez en déficites vous devez régler ce problème déficitaire \nBeaucoup de courage et remédier à çà au plus vite')


    #Demande à l'user s'il va continuer ou pas

    saisi =input('\nVeux-tu refaire un calcul (oui/non) ? : ').lower()
    #le lower permet de mettre en miniscule la reponse de l'user

    #verification du choix de l'user avec cette boucle if et break pour arreter le programme
    if saisi != "oui":
        print(f"\nMerci d'avoir utilisé le gestionnaire de budget ! 👋")
        break
    else:
        continue
