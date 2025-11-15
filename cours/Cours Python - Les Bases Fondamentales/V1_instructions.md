# Cours Python - Les Bases Fondamentales (Partie 1)
## Bienvenue dans votre apprentissage Python ! 🐍

Ce cours s'adresse à tous ceux qui découvrent la programmation. Cette **première partie** couvre les notions essentielles de données et d'interaction de base. Nous allons apprendre ensemble ces concepts fondamentaux pour bien débuter en Python. Pas d'inquiétude si certains termes vous paraissent étranges au début - nous prendrons le temps d'expliquer chaque notion pas à pas !

---

## 1. La notion de données

### Qu'est-ce qu'une donnée ?

Une **donnée** est simplement une information que votre programme peut utiliser. C'est comme si vous aviez des boîtes dans lesquelles vous rangez différents types d'objets.

### Les types de données les plus courants

En Python, nous travaillons principalement avec ces types de données :

- **Texte** (chaînes de caractères) : `"Bonjour"`, `"Mon nom est Kossi"`
- **Nombres entiers** : `5`, `42`, `-10`
- **Nombres décimaux** : `3.14`, `2.5`, `-1.8`
- **Valeurs logiques** : `True` (vrai) ou `False` (faux)

### Exemples concrets

# Du texte
"Salut tout le monde !"
"J'ai 25 ans"

# Des nombres entiers
10
-5
1000

# Des nombres décimaux
3.14
-2.7
0.5

# Des valeurs logiques
True
False

### Exercice 1 - Identifier les données
Parmi ces éléments, identifiez le type de donnée :
- `"Python"`
- `100`
- `3.14` 
- `True`
- `"123"`

<details>
<summary>Solution</summary>

- `"Python"` → Texte (chaîne de caractères)
- `100` → Nombre entier
- `3.14` → Nombre décimal
- `True` → Valeur logique
- `"123"` → Texte (même si ça ressemble à un nombre, les guillemets en font du texte)
</details>

---

## 2. La syntaxe et l'utilisation des variables

### Qu'est-ce qu'une variable ?

Une **variable** est comme une étiquette que vous collez sur une boîte pour la reconnaître. Elle permet de donner un nom à une donnée pour pouvoir l'utiliser plus tard dans votre programme.

### Comment créer une variable

La syntaxe est très simple :
````python

nom_de_la_variable = valeur


### Exemples pratiques

# Créer des variables
prenom = "Alice"
age = 25
taille = 1.65
est_etudiant = True


# Utiliser les variables
print(prenom)  # Affiche : Alice
print(age)     # Affiche : 25
print(taille)  # Affiche : 1.65
print(est_etudiant)  # Affiche : True
````

### Pourquoi utiliser des variables ?

Les variables permettent de :
- **Réutiliser** une valeur plusieurs fois
- **Modifier** facilement une valeur
- **Rendre** le code plus lisible

# Sans variable (pas pratique)
````python
print("Bonjour Fatou !")
print("Fatou a 30 ans")
print("Au revoir Fatou !")

# Avec variable (beaucoup mieux !)
nom = "Fatou"
print("Bonjour", nom, "!")
print(nom, "a 30 ans")
print("Au revoir", nom, "!")
````

### Exercice 2 - Créer vos premières variables
Créez des variables pour stocker :
- Votre prénom
- Votre âge
- Votre ville
- Si vous aimez le chocolat (True ou False)

<details>
<summary>Solution exemple</summary>

```python
prenom = "Paskod"
age = 28
ville = "Lomé"
aime_chocolat = True
```
</details>

---

## 3. Le nommage correct des variables

### Les règles obligatoires

En Python, un nom de variable doit respecter ces règles :

1. **Commencer** par une lettre ou un underscore `_`
2. **Contenir** uniquement des lettres, chiffres et underscores
3. **Être sensible** à la casse (`nom` et `Nom` sont différents)
4. **Ne pas être** un mot réservé Python (`if`, `for`, `while`, etc.)

### Exemples corrects et incorrects

✅ **Corrects :**
```python
nom = "Kwame"
age_utilisateur = 25
_variable_privee = "secret"
nombre1 = 10
mon_score = 100
```

❌ **Incorrects :**
```python
2nom = "Kwame"         # Commence par un chiffre
nom-utilisateur = 25   # Contient un tiret
mon âge = 30          # Contient un espace et un accent
if = True             # Mot réservé Python
```

### Les bonnes pratiques de nommage

1. **Utilisez des noms descriptifs**
```python
# ❌ Pas clair
x = 25
y = "Kwame"

# ✅ Clair et descriptif
age = 25
prenom = "Kwame"
```

2. **Utilisez le snake_case** (mots séparés par des underscores)
```python
# ✅ Recommandé en Python
nom_complet = "Kwame Nkrumah"
age_en_annees = 25
score_final = 850
```

3. **Évitez les abréviations obscures**
```python
# ❌ Difficile à comprendre
nb_usr = 10
tmp_val = "test"

# ✅ Plus lisible
nombre_utilisateurs = 10
valeur_temporaire = "test"
```

### Exercice 3 - Nommage des variables
Corrigez ces noms de variables pour qu'ils respectent les bonnes pratiques :

```python
# Variables à corriger
2prenom = "Amina"
nom-famille = "Diallo"
a = 1.75
temp = True
```

<details>
<summary>Solution</summary>

```python
# Variables corrigées
prenom = "Amina"                # ou premier_prenom
nom_famille = "Diallo"          # remplace le tiret par un underscore
taille = 1.75                   # plus descriptif que 'a'
est_present = True              # plus descriptif que 'temp'
```
</details>

---

## 4. L'affectation à plusieurs variables

### Affectation simple vs affectation multiple

Python permet d'affecter des valeurs à plusieurs variables en une seule ligne !

### Affectation multiple avec la même valeur

```python
# Donner la même valeur à plusieurs variables
a = b = c = 10
print(a)  # Affiche : 10
print(b)  # Affiche : 10
print(c)  # Affiche : 10
```

### Affectation multiple avec des valeurs différentes

```python
# Affecter des valeurs différentes en une ligne
nom, age, ville = "Alice", 25, "Paris"

# Équivalent à :
nom = "Alice"
age = 25
ville = "Paris"
```

### Échange de variables

Une technique très utile pour échanger le contenu de deux variables :

```python
# Variables initiales
a = 10
b = 20

# Échange en une ligne !
a, b = b, a

print(a)  # Affiche : 20
print(b)  # Affiche : 10
```

### Exemples pratiques

```python
# Coordonnées d'un point
x, y = 5, 10

# Informations d'une personne
prenom, nom, age = "Kossi", "Kossivi", 28

# Initialisation de compteurs
compteur1 = compteur2 = compteur3 = 0
```

### Exercice 4 - Affectation multiple
1. Créez trois variables `rouge`, `vert`, `bleu` avec la valeur 255
2. Créez en une ligne les variables : `produit = "Ordinateur"`, `prix = 899.99`, `disponible = True`
3. Échangez le contenu des variables `x = 100` et `y = 200`

<details>
<summary>Solution</summary>

```python
# 1. Même valeur pour trois variables
rouge = vert = bleu = 255

# 2. Affectation multiple différente
produit, prix, disponible = "Ordinateur", 899.99, True

# 3. Échange de variables
x, y = 100, 200
x, y = y, x  # Maintenant x=200 et y=100
```
</details>

---

## 5. L'utilisation de print() pour afficher

### Qu'est-ce que print() ?

La fonction `print()` est votre outil principal pour **afficher** des informations à l'écran. C'est comme dire à Python : "Montre-moi cette information !"

### Syntaxe de base

```python
print("Votre message ici")
```

### Afficher du texte

```python
print("Bonjour tout le monde !")
print("Bienvenue dans le monde Python")
print("C'est parti pour l'aventure !")
```

### Afficher des variables

```python
nom = "Prince"
age = 30

print(nom)    # Affiche : Prince
print(age)    # Affiche : 30
```

### Afficher plusieurs éléments

```python
nom = "Alice"
age = 25

# Séparer par des virgules
print("Je m'appelle", nom, "et j'ai", age, "ans")
# Affiche : Je m'appelle Alice et j'ai 25 ans

# Avec des variables et du texte
print("Nom:", nom)
print("Âge:", age)
```

### Personnaliser l'affichage

```python
# Changer le séparateur
print("A", "B", "C", sep="-")  # Affiche : A-B-C
print("A", "B", "C", sep=" | ")  # Affiche : A | B | C

# Changer la fin de ligne
print("Première ligne", end=" ")
print("Suite sur la même ligne")
# Affiche : Première ligne Suite sur la même ligne
```

### Afficher des calculs

```python
a = 10
b = 5

print("Addition:", a + b)      # Affiche : Addition: 15
print("Soustraction:", a - b)  # Affiche : Soustraction: 5
print("Multiplication:", a * b) # Affiche : Multiplication: 50
```

### Exercice 5 - Maîtriser print()
1. Affichez votre présentation : "Je suis [nom] et j'ai [age] ans"
2. Affichez trois nombres séparés par des points
3. Créez un petit programme qui affiche un menu :
   ```
   === MENU ===
   1. Option A
   2. Option B
   3. Quitter
   ```

<details>
<summary>Solution</summary>

```python
# 1. Présentation
nom = "Paskod"
age = 20
print("Je suis", nom, "et j'ai", age, "ans")

# 2. Nombres avec des points
print(10, 20, 30, sep=".")  # Affiche : 10.20.30

# 3. Menu
print("=== MENU ===")
print("1. Option A")
print("2. Option B")
print("3. Quitter")
```
</details>

---

## 6. L'utilisation de input() pour lire une entrée

### Qu'est-ce qu'input() ?

La fonction `input()` permet à votre programme de **demander** une information à l'utilisateur et d'attendre qu'il tape sa réponse au clavier.

### Syntaxe de base

```python
variable = input("Votre question : ")
```

### Premier exemple

```python
nom = input("Comment vous appelez-vous ? ")
print("Bonjour", nom, "!")
```

Quand vous exécutez ce code :
1. Le programme affiche : "Comment vous appelez-vous ? "
2. Il attend que vous tapiez votre réponse
3. Votre réponse est stockée dans la variable `nom`
4. Le programme affiche : "Bonjour [votre nom] !"

### Important : input() retourne toujours du texte

```python
# ⚠️ Attention !
age = input("Quel âge avez-vous ? ")
# Si vous tapez 25, age contient "25" (texte) pas 25 (nombre)

print(type(age))  # Affiche : <class 'str'> (string = texte)
```

### Convertir en nombre

Pour utiliser la réponse comme un nombre, il faut la convertir :

```python
# Convertir en nombre entier
age_texte = input("Quel âge avez-vous ? ")
age_nombre = int(age_texte)
print("L'année prochaine, vous aurez", age_nombre + 1, "ans")

# Ou plus court :
age = int(input("Quel âge avez-vous ? "))
```

### Exemples pratiques

```python
# Demander des informations personnelles
prenom = input("Votre prénom : ")
ville = input("Votre ville : ")
print("Bonjour", prenom, "de", ville, "!")

# Calculatrice simple
nombre1 = int(input("Premier nombre : "))
nombre2 = int(input("Deuxième nombre : "))
resultat = nombre1 + nombre2
print("Résultat :", resultat)

# Avec des nombres décimaux
taille = float(input("Votre taille en mètres : "))
print("Votre taille est de", taille, "mètres")
```

### Programme interactif complet

```python
print("=== CALCULATRICE D'ÂGE ===")
nom = input("Comment vous appelez-vous ? ")
annee_courante = int(input("Entrer l'année courante : "))
annee_naissance = int(input("En quelle année êtes-vous né(e) ? "))

# Calcul de l'âge (approximatif)
age_approximatif = annee_courante - annee_naissance

print("Bonjour", nom, "!")
print("Vous avez environ", age_approximatif, "ans")
```

### Exercice 6 - Programme interactif
Créez un programme qui :
1. Demande le nom de l'utilisateur
2. Demande son plat préféré
3. Demande combien de fois par semaine il le mange
4. Affiche un message personnalisé avec ces informations

<details>
<summary>Solution</summary>

```python
print("=== QUESTIONNAIRE CULINAIRE ===")
nom = input("Quel est votre nom ? ")
plat = input("Quel est votre plat préféré ? ")
frequence = int(input("Combien de fois par semaine le mangez-vous ? "))

print()
print("Résumé :")
print("-------")
print("Nom :", nom)
print("Plat préféré :", plat)
print("Fréquence :", frequence, "fois par semaine")
print("Génial", nom, "! Vous mangez", plat, frequence, "fois par semaine !")
```
</details>

---

## Projet final - Carnet d'identité numérique

Maintenant que vous maîtrisez les bases, créons ensemble un petit programme qui utilise tout ce que nous avons appris !

### Objectif
Créer un programme qui demande des informations à l'utilisateur et crée son "carnet d'identité numérique".

### Code du projet

```python
print("=" * 40)
print("    CARNET D'IDENTITÉ NUMÉRIQUE")
print("=" * 40)
print()

# Collecte des informations
prenom = input("Votre prénom : ")
nom = input("Votre nom de famille : ")
age = int(input("Votre âge : "))
ville = input("Votre ville : ")
couleur_preferee = input("Votre couleur préférée : ")
hobby = input("Votre hobby principal : ")

print()
print("Traitement des données...")
print()

# Calculs automatiques
annee_naissance = 2025 - age
initiales = prenom[0] + nom[0]

# Affichage du carnet
print("=" * 40)
print("       VOTRE CARNET D'IDENTITÉ")
print("=" * 40)
print("Nom complet :", prenom, nom)
print("Initiales :", initiales)
print("Âge :", age, "ans")
print("Année de naissance :", annee_naissance)
print("Ville de résidence :", ville)
print("Couleur préférée :", couleur_preferee)
print("Hobby principal :", hobby)
print("=" * 40)
print("Merci", prenom, "! Votre profil a été créé avec succès !")
```

### Défi bonus
Améliorez le programme en ajoutant :
- Une question sur le sport préféré
- Le calcul de l'âge en 2030
- Un message personnalisé selon l'âge

---

## Récapitulatif de ce que vous avez appris

Félicitations ! Vous maîtrisez maintenant :

### ✅ Les données
- Les différents types : texte, nombres, booléens
- Comment Python les reconnaît

### ✅ Les variables
- Créer et utiliser des variables
- Les bonnes pratiques de nommage
- L'affectation multiple

### ✅ L'affichage avec print()
- Afficher du texte et des variables
- Combiner plusieurs éléments
- Personnaliser l'affichage

### ✅ La saisie avec input()
- Demander des informations à l'utilisateur
- Convertir le texte en nombres
- Créer des programmes interactifs

---

## Pour aller plus loin

Maintenant que vous avez ces bases solides, vous êtes prêts à découvrir :
- Les conditions (if, else)
- Les boucles (for, while)
- Les listes et dictionnaires
- Les fonctions

Continuez à pratiquer et n'hésitez pas à expérimenter ! La programmation s'apprend en codant.

---

*Ce cours fait partie de la formation C2P (https://chat.whatsapp.com/GNtDfxG6SzEHmDXRpovN3m). Pour plus de ressources et d'exercices, consultez notre groupe watsapp 👆*