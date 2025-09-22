nombreA = float(input('Veuillez entrer le premier nommbre : '))
nombreB = float(input('Veuillez entrer le second nommbre : '))

'''if nombreB > nombreA:
    nombreMax = nombreB
else:
    nombreMax = nombreA'''

nombreMax = nombreA if nombreA > nombreB else nombreB

print(f"Le nombre maximum entre {nombreA} et {nombreB} est {nombreMax}")