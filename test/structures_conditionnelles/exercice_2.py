nombre = float(input("Veuillez entrer votre nombre : "))

if nombre < 0:
    print(f"Votre nombre {nombre} est negatif")
elif nombre == 0:
    print(f"Votre nombre {nombre} est null")
else:
    print(f"Votre nombre {nombre} est positif")