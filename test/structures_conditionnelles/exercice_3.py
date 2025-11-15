temperature = float(input("Veuillez entrer la temperature de votre liquide : "))

if temperature < 0:
    print("Glace")
elif temperature < 100:
    print("Liquide")
else:
    print("Vapeur")