# ============================================================
# 🎓 GESTIONNAIRE D'INSCRIPTION SCOLAIRE
# Objectif : Pratiquer les fonctions avec/sans argument et retour
# Auteur : Projet Étudiant
# ============================================================

# ---------------------------
# Variables globales
# ---------------------------
nombre_total_inscrits = 0
recettes_totales = 0

effectif_6eme = effectif_5eme = effectif_4eme = effectif_3eme = 0
effectif_2nde = effectif_1ere = effectif_terminale = 0

bourse_excellence = bourse_sociale = bourse_familiale = bourse_aucune = 0

# Informations de l'élève actuel
eleve_nom = ""
eleve_prenom = ""
eleve_age = 0
eleve_classe = ""
eleve_etab = ""
eleve_bourse = "aucune"
eleve_frais = 0


# ---------------------------
# Fonctions principales
# ---------------------------

def afficher_menu():
    """Affiche le menu principal (aucun argument, aucun retour)."""
    print("\nGESTIONNAIRE D'INSCRIPTION SCOLAIRE")
    print("===================================")
    print("1. Inscrire un élève")
    print("2. Consulter l'élève actuel")
    print("3. Modifier les informations")
    print("4. Calculer les frais")
    print("5. Voir les statistiques")
    print("6. Quitter")


def saisir_age():
    """Saisie sécurisée de l'âge (avec exception et retour)."""
    while True:
        try:
            age = int(input("Âge : "))
            if age < 10 or age > 25:
                print("❌ Âge invalide ! Entre 10 et 25 ans.")
                continue
            return age
        except ValueError:
            print("⚠️ Erreur ! Entrez un nombre valide.")


def calculer_frais(classe, etablissement, bourse):
    """Calcule et retourne le total des frais selon les paramètres."""
    global recettes_totales

    # Base selon établissement
    frais_base = 35000 if etablissement == "privé" else 15000 if etablissement == "technique" else 0

    # Réductions selon la bourse
    reduction = 0
    if bourse == "excellence":
        reduction = 0.5
    elif bourse == "sociale":
        reduction = 0.3
    elif bourse == "familiale":
        reduction = 0.2

    # Autres frais fixes
    frais_ape = 2000
    frais_cantine = 1500
    frais_transport = 1000

    # Calcul total
    frais_final = (frais_base * (1 - reduction)) + frais_ape + frais_cantine + frais_transport
    recettes_totales += frais_final

    return frais_final


def inscrire_eleve():
    """Inscription complète d'un élève (avec paramètres et global)."""
    global eleve_nom, eleve_prenom, eleve_age, eleve_classe, eleve_etab, eleve_bourse, eleve_frais
    global nombre_total_inscrits, recettes_totales
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global bourse_excellence, bourse_sociale, bourse_familiale, bourse_aucune

    print("\nINSCRIPTION D'UN NOUVEL ÉLÈVE")
    print("==============================")

    eleve_nom = input("Nom : ").upper()
    eleve_prenom = input("Prénom : ").capitalize()
    eleve_age = saisir_age()

    eleve_classe = input("Classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Terminale) : ").capitalize()
    eleve_etab = input("Type d'établissement (public, privé, technique) : ").lower()
    eleve_bourse = input("Type de bourse (excellence, sociale, familiale, aucune) : ").lower()

    # Mise à jour effectif
    if eleve_classe == "6ème":
        effectif_6eme += 1
    elif eleve_classe == "5ème":
        effectif_5eme += 1
    elif eleve_classe == "4ème":
        effectif_4eme += 1
    elif eleve_classe == "3ème":
        effectif_3eme += 1
    elif eleve_classe == "2nde":
        effectif_2nde += 1
    elif eleve_classe == "1ère":
        effectif_1ere += 1
    elif eleve_classe == "Terminale":
        effectif_terminale += 1

    # Statistiques bourses
    if eleve_bourse == "excellence":
        bourse_excellence += 1
    elif eleve_bourse == "sociale":
        bourse_sociale += 1
    elif eleve_bourse == "familiale":
        bourse_familiale += 1
    else:
        bourse_aucune += 1

    nombre_total_inscrits += 1
    eleve_frais = calculer_frais(eleve_classe, eleve_etab, eleve_bourse)

    print("\n✅ Élève inscrit avec succès !")
    print(f"Total à payer : {eleve_frais:.0f} FCFA")


def consulter_eleve():
    """Affiche les informations de l'élève actuel."""
    global eleve_nom

    if eleve_nom == "":
        print("\n⚠️ Aucun élève inscrit pour le moment.")
        return

    print("\nCONSULTATION DE L'ÉLÈVE ACTUEL")
    print("==============================")
    print(f"Nom : {eleve_nom}")
    print(f"Prénom : {eleve_prenom}")
    print(f"Âge : {eleve_age} ans")
    print(f"Classe : {eleve_classe}")
    print(f"Établissement : {eleve_etab}")
    print(f"Bourse : {eleve_bourse}")
    print(f"Frais totaux : {eleve_frais:.0f} FCFA")
    print("Statut : Inscription complète ✅")


def modifier_eleve():
    """Permet de modifier les informations d’un élève déjà inscrit."""
    global eleve_nom, eleve_prenom, eleve_age, eleve_classe, eleve_etab, eleve_bourse, eleve_frais

    if eleve_nom == "":
        print("\n⚠️ Aucun élève à modifier.")
        return

    print("\nMODIFICATION DES INFORMATIONS")
    print("============================")

    print(f"Nom actuel : {eleve_nom}")
    eleve_nom = input("Nouveau nom : ") or eleve_nom

    print(f"Prénom actuel : {eleve_prenom}")
    eleve_prenom = input("Nouveau prénom : ") or eleve_prenom

    print(f"Âge actuel : {eleve_age}")
    try:
        nv_age = input("Nouvel âge : ")
        if nv_age != "":
            eleve_age = int(nv_age)
    except ValueError:
        print("⚠️ Entrée invalide, âge inchangé.")

    print(f"Classe actuelle : {eleve_classe}")
    nv_classe = input("Nouvelle classe : ") or eleve_classe
    eleve_classe = nv_classe

    print(f"Établissement actuel : {eleve_etab}")
    nv_etab = input("Nouvel établissement : ") or eleve_etab
    eleve_etab = nv_etab

    print(f"Bourse actuelle : {eleve_bourse}")
    nv_bourse = input("Nouvelle bourse : ") or eleve_bourse
    eleve_bourse = nv_bourse

    eleve_frais = calculer_frais(eleve_classe, eleve_etab, eleve_bourse)
    print("\n✅ Informations modifiées avec succès !")
    print(f"Nouveaux frais : {eleve_frais:.0f} FCFA")


def afficher_statistiques():
    """Affiche les statistiques globales (lecture seule, pas de global modifié)."""
    print("\nSTATISTIQUES GÉNÉRALES")
    print("======================")
    print(f"Nombre total d'inscrits : {nombre_total_inscrits}")
    print("Effectif par classe :")
    print(f"- 6ème : {effectif_6eme} élèves")
    print(f"- 5ème : {effectif_5eme} élèves")
    print(f"- 4ème : {effectif_4eme} élèves")
    print(f"- 3ème : {effectif_3eme} élèves")
    print(f"- 2nde : {effectif_2nde} élèves")
    print(f"- 1ère : {effectif_1ere} élèves")
    print(f"- Terminale : {effectif_terminale} élèves")
    print(f"\nRecettes totales : {recettes_totales:.0f} FCFA")
    print("Répartition des bourses :")
    print(f"- Excellence : {bourse_excellence}")
    print(f"- Sociale : {bourse_sociale}")
    print(f"- Familiale : {bourse_familiale}")
    print(f"- Aucune : {bourse_aucune}")


# ---------------------------
# Programme principal
# ---------------------------

def main():
    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            inscrire_eleve()
        elif choix == "2":
            consulter_eleve()
        elif choix == "3":
            modifier_eleve()
        elif choix == "4":
            if eleve_nom == "":
                print("\n⚠️ Aucun élève à calculer.")
            else:
                total = calculer_frais(eleve_classe, eleve_etab, eleve_bourse)
                print(f"\nTotal des frais recalculés : {total:.0f} FCFA")
        elif choix == "5":
            afficher_statistiques()
        elif choix == "6":
            print("\n👋 Merci d'avoir utilisé le gestionnaire d'inscription !")
            break
        else:
            print("❌ Choix invalide. Essayez encore.")


# Lancement du programme
main()
