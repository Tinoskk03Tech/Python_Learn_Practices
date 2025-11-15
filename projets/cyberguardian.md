# Cyberguardian : Testez votre sécurité numérique !

> **Projet pédagogique Python pour débutants**  
> Niveau requis : Structures conditionnelles, opérateurs logiques, entrées/sorties

---

## Concepts Python mis en pratique

### Conditions imbriquées
Vous découvrirez comment imbriquer des conditions pour des analyses plus fines :

```python
if score >= 4:
    print("🛡️ Cyber-Expert")
    if mot_de_passe_unique == "non":
        print("⚠️ Attention : même un expert doit utiliser des mots de passe uniques !")
    else:
        print("🎉 Parfait ! Vous maîtrisez tous les aspects de la sécurité !")
```

### Opérateur ternaire
Apprenez à écrire des conditions courtes et élégantes :

```python
# Au lieu de :
if reponse == "oui":
    score = score + 1
else:
    score = score + 0

# Vous pouvez écrire :
score += 1 if reponse == "oui" else 0

# Ou encore :
message = "Bravo !" if score >= 4 else "À améliorer"
```

---

## Bienvenue dans votre premier projet Python !

Félicitations ! Vous allez créer votre premier programme interactif en `Python`. Ce projet va vous permettre de mettre en pratique tout ce que vous avez appris sur les conditions, les opérateurs logiques et les interactions avec l'utilisateur.

### Ce que vous allez apprendre

- Utiliser les structures `if/elif/else` dans un projet concret
- **Maîtriser les conditions imbriquées** pour des analyses plus précises
- **Découvrir l'opérateur ternaire** pour des conditions courtes et élégantes
- Combiner des conditions avec `and`, `or`, `not`
- Créer un programme qui s'adapte aux réponses de l'utilisateur
- Manipuler les entrées utilisateur avec `input()`
- Afficher des résultats personnalisés avec `print()`

---

## Votre mission

Vous allez créer un quiz de cybersécurité qui pose 5 questions importantes sur les habitudes numériques. Selon les réponses de l'utilisateur, votre programme calculera un score et affichera un profil personnalisé avec des conseils adaptés.

### 🔍 Les 5 questions à poser

1. **"Utilisez-vous un mot de passe différent pour chaque compte ?"**
2. **"Vérifiez-vous l'URL avant de saisir vos informations personnelles ?"**
3. **"Activez-vous les mises à jour automatiques de sécurité ?"**
4. **"Évitez-vous de vous connecter sur des réseaux Wi-Fi publics pour des tâches sensibles ?"**
5. **"Utilisez-vous l'authentification à deux facteurs quand c'est possible ?"**

> **Astuce** : L'utilisateur devra répondre par "oui" ou "non" à chaque question.

---

## Structure de votre programme

### Étape 1 : Message de bienvenue
Affichez un message d'accueil qui explique le concept du quiz.

### Étape 2 : Posez les questions
- Posez chaque question une par une
- Récupérez la réponse de l'utilisateur
- Comptez le nombre de "oui"

### Étape 3 : Analysez les résultats
Selon le nombre de réponses "oui", déterminez le profil :

| Score | Profil | Description |
|-------|--------|-------------|
| 4-5 "oui" | 🛡️ **Cyber-Expert** | Excellent niveau de sécurité |
| 2-3 "oui" | ⚠️ **Utilisateur Prudent** | Bonnes bases, quelques améliorations possibles |
| 0-1 "oui" | 🚨 **Cyber-Novice** | Attention, des améliorations sont nécessaires |

**💡 Défi avancé** : Utilisez des conditions imbriquées pour affiner l'analyse !
- Si le score est élevé ET que l'utilisateur n'utilise pas de mots de passe uniques → message spécial
- Si le score est faible MAIS qu'il utilise l'authentification à deux facteurs → encouragement particulier

### Étape 4 : Affichez le résultat personnalisé
Montrez le profil avec des conseils spécifiques selon le score obtenu.

---

## Exemple d'exécution

```
🔐 === CYBERGUARDIAN : TESTEZ VOTRE SÉCURITÉ NUMÉRIQUE ! ===

Bienvenue ! Ce quiz va évaluer vos habitudes de cybersécurité.
Répondez par 'oui' ou 'non' à chaque question.

Question 1/5 : Utilisez-vous un mot de passe différent pour chaque compte ?
Votre réponse : non

Question 2/5 : Vérifiez-vous l'URL avant de saisir vos informations personnelles ?
Votre réponse : oui

Question 3/5 : Activez-vous les mises à jour automatiques de sécurité ?
Votre réponse : oui

Question 4/5 : Évitez-vous de vous connecter sur des réseaux Wi-Fi publics pour des tâches sensibles ?
Votre réponse : non

Question 5/5 : Utilisez-vous l'authentification à deux facteurs quand c'est possible ?
Votre réponse : oui

       === VOTRE PROFIL CYBERSÉCURITÉ ===

⚠️ UTILISATEUR PRUDENT
Vous avez de bonnes bases mais quelques améliorations sont possibles !

  Conseils personnalisés :
- Pensez à utiliser un gestionnaire de mots de passe
- Méfiez-vous des réseaux Wi-Fi publics pour vos comptes importants

Score final : 3/5 - Continuez vos efforts !
```

---

## Conseils pour réussir

### 🔧 Outils Python à utiliser
- `input()` pour récupérer les réponses
- `print()` pour afficher les messages
- `if/elif/else` pour les conditions
- **Conditions imbriquées** : `if` à l'intérieur d'un autre `if`
- **Opérateur ternaire** : `variable = valeur1 if condition else valeur2`
- `and/or/not` pour combiner des conditions
- Variables pour stocker le score

### Points d'attention
- **Validation des entrées** : Assurez-vous que l'utilisateur répond bien par "oui" ou "non"
- **Comptage du score** : Incrémentez un compteur à chaque réponse "oui"
- **Conditions multiples** : Utilisez `elif` pour les différents profils
- **Conditions imbriquées** : Pour des analyses plus fines (ex: score élevé ET réponse spécifique)
- **Opérateurs ternaires** : Pour des assignations conditionnelles courtes
- **Messages personnalisés** : Adaptez les conseils selon le profil obtenu

### Pour aller plus loin (optionnel)
- Gérez les réponses en majuscules/minuscules avec `.lower()`
- Ajoutez des emojis pour rendre le programme plus attrayant
- **Utilisez des conditions imbriquées** pour des messages ultra-personnalisés
- **Expérimentez avec l'opérateur ternaire** pour simplifier vos conditions
- Proposez des conseils différents selon les combinaisons de réponses spécifiques

---

## Objectifs pédagogiques atteints

En réalisant ce projet, vous aurez :

✅ Maîtrisé les structures conditionnelles dans un contexte réel  
✅ **Découvert les conditions imbriquées** pour des analyses précises  
✅ **Appris l'opérateur ternaire** pour des conditions élégantes  
✅ Utilisé les opérateurs logiques pour combiner des conditions  
✅ Créé un programme interactif avec des entrées utilisateur  
✅ Développé une logique de scoring et de catégorisation  
✅ Affiché des résultats personnalisés selon les données  

---

## 🏁 Prêt à commencer ?

Ouvrez votre éditeur Python favori et commencez par écrire le message de bienvenue. N'hésitez pas à tester votre programme régulièrement pour vérifier que chaque étape fonctionne correctement.

**Bonne programmation !**

---


---

**📧 Questions ou suggestions ?** N'hésitez pas à ouvrir une issue sur ce repository !