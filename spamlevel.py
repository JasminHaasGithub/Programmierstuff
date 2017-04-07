datei = open("mbox.txt")
spamlevel = 0
anzahl = 0
spam = "X-DSPAM-Confidence:"

for zeile in datei:
    new_string = zeile.strip().split(" ")
    if new_string[0] == spam:
        spamlevel = spamlevel + float(new_string[1])
        anzahl = anzahl + 1
        

print("Das durchschnittliche Spamlevel ist " + str(spamlevel / anzahl))

