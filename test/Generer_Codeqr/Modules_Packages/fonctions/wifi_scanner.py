import subprocess

import subprocess

def run_wifi():
    print("\n=== Scanner WiFi ===")

    # 🔹 Étape 1 — Demander confirmation
    while True:
        confirm = input("Souhaitez-vous lancer le scan ? (y/n) : ").strip().lower()

        if confirm == "y":
            break  # on continue vers le scan
        elif confirm == "n":
            print("Scan annulé par l'utilisateur.")
            return  # on sort de la fonction
        else:
            print("Entrée invalide — veuillez taper 'y' ou 'n'.\n")

    # 🔹 Étape 2 — Lancer le scan
    print("\nScan en cours...\n")

    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

        if result.returncode != 0:
            print("❌ Erreur de scan — code retour :", result.returncode)
            return

        # 🔹 Analyse du résultat
        lines = result.stdout.splitlines()
        ssids = []

        for line in lines:
            if "SSID" in line and ":" in line:
                ssid = line.split(":", 1)[1].strip()
                if ssid:
                    ssids.append(ssid)

        # 🔹 Affichage des résultats
        if ssids:
            print("📡 Réseaux WiFi détectés :\n")
            for i, ssid in enumerate(ssids, 1):
                print(f"{i}. {ssid}")
            print(f"\nTotal : {len(ssids)} réseau(x)")
        else:
            print("⚠️ Aucun réseau détecté.")

    except FileNotFoundError:
        print("❌ Commande 'netsh' introuvable — ce script fonctionne uniquement sous Windows.")
    except Exception as e:
        print(f"❌ Erreur de scan : {e}")




