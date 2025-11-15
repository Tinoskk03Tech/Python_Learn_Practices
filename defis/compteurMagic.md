# Défi Python : Le Compteur Magique

## 📋 Cahier des charges

Créez un programme qui compte de 1 à 20, mais avec des règles spéciales :

### Règles du jeu :
1. **Compter de 1 à 20** avec une boucle `for`
2. **Ignorer les multiples de 3** (3, 6, 9, 12, 15, 18) → utiliser `continue`
3. **S'arrêter si on trouve le nombre 17** → utiliser `break`
4. **Pour le nombre 13**, ne rien faire du tout → utiliser `pass`

### Objectifs pédagogiques :
- 🟢 Utiliser une boucle `for` avec `range()`
- 🟢 **Obligatoirement** utiliser `continue` pour ignorer certains nombres
- 🟢 **Obligatoirement** utiliser `break` pour arrêter la boucle
- 🟢 **Obligatoirement** utiliser `pass` comme placeholder
- 🟢 Utiliser les conditions `if`
- 🟢 Utiliser l'opérateur modulo `%`

## 🎮 Exemple d'exécution

```
=== COMPTEUR MAGIQUE ===
Comptage de 1 à 20 avec des règles spéciales...

1
2
4  (3 ignoré - multiple de 3)
5
7  (6 ignoré - multiple de 3) 
8
10 (9 ignoré - multiple de 3)
11
13 (nombre mystère - on ne fait rien)
14
16 (15 ignoré - multiple de 3)

STOP ! Nombre 17 trouvé - arrêt du compteur !
```

## Indications pour les débutants

### Aide technique :
- **Multiple de 3** : utiliser `nombre % 3 == 0`
- **Afficher un message** : `print("STOP ! Nombre 17 trouvé")`
- **Commentaires** : expliquer pourquoi vous utilisez chaque instruction

## 🏆 Critères de réussite

Votre programme doit :
- [x] Utiliser une boucle `for` avec `range(1, 21)`
- [x] Contenir **exactement** un `break`
- [x] Contenir **exactement** un `continue` 
- [x] Contenir **exactement** un `pass`
- [x] Ignorer les multiples de 3 (ne pas les afficher)
- [x] S'arrêter quand il trouve 17
- [x] Afficher le nombre 13 mais sans commentaire spécial

## Résultat attendu

Le programme doit afficher exactement :
```
1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16
```

Puis s'arrêter avec un message d'arrêt.

## Extension (optionnelle)

Une fois le défi réussi, essayez ces variantes :
- Compter de 1 à 50
- Ignorer les multiples de 5 au lieu de 3
- S'arrêter à un autre nombre

---

**Temps estimé :** 15-30 minutes  
**Niveau :** Débutant  
**Notions utilisées :** Variables, boucles, conditions, break/continue/pass