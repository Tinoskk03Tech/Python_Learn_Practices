age = int(input("Veuillez entrer votre age : "))

'''if age >= 18:
    print("Peut voté")
else:
    print("Ne peut pas voté")'''

'''print("Peut voté") if age >= 18 else print("Ne peut pas voté")'''

peutvoter = "Peut voté" if age >= 18 else "Ne peut pas voté"

print(peutvoter)