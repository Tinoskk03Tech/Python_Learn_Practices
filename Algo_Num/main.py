# ===========================================================
#   RÉSOLUTION D'ÉQUATION f(x)=0 PAR :
#   - MÉTHODE DE BALAYAGE (BISSECTION)
#   - MÉTHODE DE SUBSTITUTION (POINT FIXE)
#   - TEST DE CONTRACTION (LIPSCHITZ)
#   - JUSTIFICATION PAR LE THÉORÈME DES ACCROISSEMENTS FINIS
# ===========================================================

import math

# === 1. DÉFINITION DE LA FONCTION ET DE SA DÉRIVÉE ===
def f(x):
    """Fonction dont on cherche la racine."""
    return x**2 - 2   # Exemple : f(x) = x² - 2

def f_deriv(x):
    """Dérivée de f(x)."""
    return 2 * x      # f'(x) = 2x

# === 2. MÉTHODE DE BALAYAGE / BISECTION ===
def balayage_bisection(a, b, eps):
    """Localise la racine en réduisant l’intervalle [a, b]."""
    if f(a) * f(b) > 0:
        raise ValueError("Pas de changement de signe sur [a,b] !")
    
    while abs(b - a) > eps:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2, a, b

# === 3. CONSTRUCTION DE F(x) ET TEST LIPSCHITZ ===
def construire_F(a, b):
    """
    Construit la fonction F(x) = x - (1/K)*f(x)
    en choisissant un K tel que |1 - f'(x)/K| < 1
    """
    # Évaluation approximative de M = sup|f'(x)| sur [a,b]
    M = max(abs(f_deriv(a)), abs(f_deriv(b)))
    K = M + 1  # marge de sécurité
    print(f"[INFO] Estimation de M = {M:.4f} -> K choisi = {K:.4f}")
    
    def F(x):      # Fonction de substitution
        return x - f(x) / K
    
    def F_deriv(x):  # Dérivée de F(x)
        return 1 - f_deriv(x) / K
    
    # Calcul du Lipschitz L = sup|F'(x)|
    L = max(abs(F_deriv(a)), abs(F_deriv(b)))
    print(f"[INFO] Constante de Lipschitz estimée L = {L:.4f}")
    
    # Test de contraction
    if L >= 1:
        print("[ATTENTION] F n’est pas contractante ! Ajustez K.")
    else:
        print("[OK] F est contractante (L < 1) → convergence garantie.")
    
    return F, F_deriv, L, K

# === 4. MÉTHODE DE SUBSTITUTION ===
def methode_substitution(F, a, b, eps, Nmax):
    """Itère x_{n+1} = F(x_n) jusqu'à convergence."""
    x_prec = (a + b) / 2   # point de départ au milieu de l’intervalle
    print(f"\n[ITÉRATIONS] Point de départ x0 = {x_prec:.6f}\n")

    for n in range(1, Nmax + 1):
        x_suiv = F(x_prec)
        print(f"Iteration {n:2d} : x = {x_suiv:.8f}, f(x) = {f(x_suiv):.3e}")
        
        if abs(x_suiv - x_prec) < eps or abs(f(x_suiv)) < eps:
            print(f"\nConvergence atteinte en {n} itérations.")
            return x_suiv, n
        
        x_prec = x_suiv
    
    print("\n[ALERTE] Nombre maximal d’itérations atteint.")
    return x_suiv, Nmax

# === 5. PROGRAMME PRINCIPAL ===
def main():
    print("=== RÉSOLUTION PAR MÉTHODE DE SUBSTITUTION ===")
    
    # Paramètres initiaux
    a, b = 1, 2
    eps = 1e-6
    Nmax = 50
    
    # Étape 1 : Balayage (localisation de la racine)
    x0, a0, b0 = balayage_bisection(a, b, eps)
    print(f"\n[LOCALISATION] Intervalle réduit : [{a0:.6f}, {b0:.6f}]")
    print(f"Approximation initiale : x0 = {x0:.6f}")
    
    # Étape 2 : Construction de F(x) et test Lipschitz
    F, F_deriv, L, K = construire_F(a0, b0)
    
    # Étape 3 : Méthode de substitution
    x_star, n_iter = methode_substitution(F, a0, b0, eps, Nmax)
    
    # Étape 4 : Résultats et vérification
    print("\n=== RÉSULTATS ===")
    print(f"Racine approchée : x* = {x_star:.8f}")
    print(f"Vérification : f(x*) = {f(x_star):.3e}")
    print(f"Constante de Lipschitz L = {L:.4f}  (<1 ⇒ convergence garantie)")
    print(f"Erreur estimée ≤ {(abs(f(x_star)) / (1 - L)):.3e}")

    print("\nJustification par le Théorème des Accroissements Finis :")
    print("   |F(x) - F(y)| ≤ L * |x - y|,  avec L =", round(L, 4))
    print("   Donc F est contractante ⇒ la suite (x_n) converge vers x* unique.")

# === 6. LANCEMENT DU PROGRAMME ===
if __name__ == "__main__":
    main()
