Zahl = 97
Zahl = str(Zahl)

while len(Zahl) > 1:
    quersumme = sum([int(i) for i in Zahl])

print(quersumme)