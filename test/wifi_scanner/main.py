# Les importations
import subprocess

# Acceuil de l'application
print("\nScanner Wifi")
print("-" * 12, "\n")

print("Scaning...\n")

# Exécution de la commande netsh wlan show networks
try :
    reseau = subprocess.run(
        ['netsh', 'wlan', 'show', 'networks'],
        capture_output= True,
        text = True,
        encoding = "utf-8"
    )
    print(reseau.stdout)
    
except Exception as error :
    print(f"erreur : {error}")

