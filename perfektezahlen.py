zahl = int(input("Die zu überprüfende Zahl lautet:"))
summe = 0
for i in range(1,zahl+1):
    if zahl % i == 0:
        summe = summe + i
    else:
        summe = summe
    if summe == zahl:
        print(zahl)

