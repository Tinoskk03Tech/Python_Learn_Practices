# Système de Gestion de Profil Utilisateur
## Cahier des charges - Projet Python débutant (C Premier Pa)

### 📋 Description du projet

Ce projet consiste à créer un **mini système de gestion de profil utilisateur** entièrement en ligne de commande. Il s'agit d'un projet parfait pour débuter en Python et mettre en pratique les concepts de base : variables, conditions, boucles et interactions utilisateur.

Le programme permet à un utilisateur de créer son profil, de définir un mot de passe sécurisé avec des mots de récupération, puis de se connecter pour consulter ses informations personnelles.

### Objectifs pédagogiques

À la fin de ce projet, vous maîtriserez :
- 🟢 La saisie et validation des données utilisateur avec `input()`
- 🟢 L'utilisation des conditions `if/elif/else`
- 🟢 Les boucles `while` pour répéter des actions
- 🟢 La manipulation de chaînes de caractères
- 🟢 La logique de validation et de vérification
- 🟢 L'affichage formaté et convivial
- 🟢 La gestion d'erreurs simple avec des tentatives limitées

### ⚙️ Prérequis techniques

- **Python 3.6 ou supérieur** (recommandé : Python 3.8+)
- **Éditeur de code** : Visual Studio Code, PyCharm Community, ou même un simple éditeur de texte
- **Terminal/Invite de commandes** pour exécuter le programme
- **Connaissances de base** : variables, `print()`, `input()`, conditions `if/else`

### Spécifications fonctionnelles

#### 1. **Création du profil utilisateur**
- Saisie du **nom complet**
- Saisie de l'**âge** (avec validation numérique)
- Saisie de la **ville de résidence**
- Messages d'encouragement à chaque étape

#### 2. **Définition du mot de passe**
- Saisie du mot de passe avec **validation de longueur minimale** (8 caractères minimum)
- **Confirmation du mot de passe** avec vérification de correspondance
- Utilisation d'une **boucle `while`** pour redemander en cas d'erreur
- Messages clairs en cas d'échec de validation

#### 3. **Mots de récupération**
- Saisie de **deux mots de récupération** distincts
- Validation que les deux mots sont différents
- Stockage pour usage ultérieur

#### 4. **Système de connexion**
- **Maximum 3 tentatives** de connexion
- Saisie du nom d'utilisateur et mot de passe
- **Boucle `while`** pour gérer les tentatives
- Messages différenciés selon le succès/échec
- Blocage après 3 échecs consécutifs

#### 5. **Affichage du profil**
- **Accessible uniquement après connexion réussie**
- Affichage formaté des informations personnelles
- Message de bienvenue personnalisé

### Contraintes techniques

**Ce projet doit respecter les limitations suivantes pour rester accessible aux débutants :**
- ❌ **Pas de fonctions** (`def`)
- ❌ **Pas de `break` ni `continue`**
- ❌ **Pas de structures de données avancées** (listes, dictionnaires)
- ❌ **Pas de modules externes** ou d'imports
- ✅ **Uniquement** : `input()`, `print()`, conditions `if/elif/else`, boucles `while`, variables simples

### Bonnes pratiques à respecter

1. **Noms de variables explicites** : `nom_utilisateur` plutôt que `x`
2. **Messages clairs et encourageants** pour guider l'utilisateur
3. **Validation des données** à chaque saisie importante
4. **Espacement et lisibilité** du code avec des commentaires
5. **Gestion des erreurs** avec des messages informatifs
6. **Interface utilisateur conviviale** avec des séparateurs visuels

### 🎮 Exemple d'exécution

```
=========================================
🎉 CRÉATION DE VOTRE PROFIL UTILISATEUR 🎉
=========================================

👋 Bonjour ! Créons ensemble votre profil personnel.

📝 Veuillez saisir votre nom complet : PASCAL Paskod
✅ Parfait PASCAL Paskod !

🎂 Quel est votre âge ? : 250 
✅ Âge enregistré : 250 ans

🏠 Dans quelle ville habitez-vous ? : Lomé
✅ Ville enregistrée : Lomé

=========================================
🔐 CONFIGURATION DE VOTRE MOT DE PASSE
=========================================

🔑 Créez un mot de passe sécurisé (minimum 8 caractères) : motdepasse123
✅ Mot de passe accepté !

🔑 Confirmez votre mot de passe : motdepasse123
✅ Mot de passe confirmé avec succès !

🔐 Premier mot de récupération : PythonAuLait
🔐 Deuxième mot de récupération (différent du premier) : PassAndKod
✅ Mots de récupération enregistrés !

=========================================
🎉 PROFIL CRÉÉ AVEC SUCCÈS ! 🎉
=========================================

🔐 Veuillez maintenant vous connecter pour accéder à votre profil.

Nom d'utilisateur : PASCAL Paskod
Mot de passe : motdepasse123

✅ CONNEXION RÉUSSIE ! Bienvenue PASCAL Paskod ! ✅

=========================================
📋 VOTRE PROFIL PERSONNEL
=========================================
👤 Nom : PASCAL Paskod
🎂 Âge : 250 ans  
🏠 Ville : Lomé
🔐 Compte sécurisé avec mots de récupération
=========================================

Merci d'utiliser notre système ! 😊
```

### Structure recommandée du code

1. **En-tête du programme** avec titre et présentation
2. **Phase de création du profil** (nom, âge, ville)
3. **Phase de définition du mot de passe** avec validation
4. **Phase des mots de récupération**
5. **Message de confirmation de création**
6. **Phase de connexion** avec gestion des tentatives
7. **Affichage du profil** si connexion réussie

### Comment lancer le projet

1. **Créer un fichier** `gestion_profil.py`
2. **Écrire le code** en suivant les spécifications
3. **Ouvrir le terminal** dans le dossier du projet
4. **Exécuter** : `python gestion_profil.py`
5. **Suivre les instructions** affichées à l'écran

### Conseils pour bien débuter

#### Pour ce projet spécifiquement :
- **Commencez simple** : créez d'abord la structure de base, puis ajoutez les validations
- **Testez fréquemment** : exécutez votre code après chaque nouvelle fonctionnalité
- **Utilisez des `print()` temporaires** pour vérifier vos variables pendant le développement
- **Écrivez les messages utilisateur en premier** pour visualiser le déroulement du programme

#### Conseils généraux Python pour débutants :
- **Pratiquez régulièrement** : 15-30 minutes par jour valent mieux qu'une session de 3h par semaine
- **Lisez vos erreurs** : les messages d'erreur Python sont très informatifs
- **Commentez votre code** : écrivez ce que fait chaque section importante
- **Expérimentez** : n'hésitez pas à modifier le code pour voir ce qui se passe
- **Rejoignez des communautés** : forums, Discord Python, Reddit r/learnpython
- **Utilisez la documentation officielle** : docs.python.org est votre ami
- **Faites des pauses** : si vous bloquez, éloignez-vous 10-15 minutes puis revenez

### 🏆 Compétences acquises après ce projet

Félicitations ! En terminant ce projet, vous aurez développé des **compétences fondamentales** qui vous serviront dans tous vos futurs projets Python :

#### **Compétences techniques**
- **Interaction utilisateur** : maîtrise complète de `input()` et validation des données
- **Logique conditionnelle** : utilisation fluide des `if/elif/else` pour créer des programmes intelligents
- **Boucles de contrôle** : compréhension des `while` pour répéter des actions jusqu'à obtenir un résultat satisfaisant
- **Validation de données** : techniques pour vérifier et sécuriser les saisies utilisateur
- **Gestion d'erreurs basique** : anticipation des erreurs utilisateur et récupération gracieuse

#### **Compétences en résolution de problèmes**
- **Décomposition de problème** : transformer un besoin complexe en étapes simples
- **Logique algorithmique** : structurer un programme avec un début, un milieu et une fin cohérents
- **Debugging** : identifier et corriger les erreurs dans votre code
- **Test utilisateur** : prévoir les différents scénarios d'utilisation

#### 💪 **Compétences professionnelles**
- **Expérience utilisateur (UX)** : créer des interfaces claires et conviviales
- **Gestion de projet simple** : mener un projet de A à Z
- **Documentation** : habitude de commenter et structurer son code
- **Confiance en programmation** : sentiment d'accomplissement qui motivera pour des projets plus ambitieux

### Et après ce projet ?

Ce projet vous prépare parfaitement pour aborder :
- Les **fonctions** (organisation du code en blocs réutilisables)
- Les **listes et dictionnaires** (gestion de plusieurs utilisateurs)
- Les **fichiers** (sauvegarde des profils)
- Les **modules** (organisation en plusieurs fichiers)
- Les **interfaces graphiques** (Tkinter)

### Contribution et partage

N'hésitez pas à :
- **Partager votre version** du projet
- **Proposer des améliorations** via des issues ou pull requests
- **Aider d'autres débutants** qui découvrent ce projet
- **Documenter vos difficultés** pour améliorer ce cahier des charges

---

**Rappel important** : Ce projet est conçu pour être **votre première réussite** en Python. Prenez votre temps, amusez-vous, et surtout : soyez fier de chaque ligne de code que vous écrivez ! 

**Bon coding !**

---
# COMMUNAUTÉ : 
Rejoins l’univers `C2P` !  
Une communauté jeune, ambitieuse et passionnée par le code et l’apprentissage collaboratif.  
Des échanges, du soutien, des projets concrets, et surtout… des développeurs qui montent ensemble !

Tu veux progresser, rire, partager, apprendre à ton rythme ?  

|| [COMMUNAUTÉ C2P sur Discord](https://discord.gg/JuEbGcFC)

|| [COMMUNAUTÉ C2P sur LinkedIn](https://www.linkedin.com/company/c2p-community/)

|| [COMMUNAUTÉ C2P sur WhatsApp](https://chat.whatsapp.com/GNtDfxG6SzEHmDXRpovN3m)


---
