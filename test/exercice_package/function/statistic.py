import statistics

def DonneesStat (data = (2, 5, 8, 6, 2, 3, 8, 6, 2, 2)):
    mode = statistics.mode(data)
    eqType = statistics.stdev(data)
    print(f'Mode : {mode}  \nEquart type : {eqType}')

DonneesStat(data = (3, 3, 4, 2, 3, 3, 5, 9, 3, 7))

print("Programme de serie statistiques")

while True:
    while True:
        try:
            n = int(input("Entrez le nombre de donnees a saisir : "))
            if n <= 0:
                print("Veuillez entrer un entier positif.")
                continue
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier.")
    data = []
    for i in range(n):
        while True:
            try:
                valeur = float(input(f"Entrez la valeur {i + 1} : "))
                data.append(valeur)
                break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre.")
                
    DonneesStat(data)
    continuer = input("Voulez-vous continuer ? (o/n) : ").strip().lower()
    if continuer != 'o':
        print("Fin du programme.")
        break