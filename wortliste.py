datei = open("mbox.txt")
Liste = list()

for zeile in datei:
    neue_zeile = zeile.strip().split(" ")
    for wort in neue_zeile:
        if wort not in Liste:
            Liste.append(wort)
            
print(len(Liste))
