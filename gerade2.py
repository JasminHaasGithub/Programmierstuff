summe = 0
for i in range(101):
    in i % 2 == 0:
        print("Die Zahl", i, "ist gerade! Addiere sie.")
        summe = summe + i
    else:
        print("Die Zahl", i, "ist ungerade! Überspringe sie.")
        
print(summe)
