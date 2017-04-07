datei = open("mbox.txt")
anzahl = 0

for zeile in datei:
    neue_zeile = zeile.strip().split(" ")
    for neue_zeile in datei: 
        if neue_zeile.startswith("From:"):
            anzahl = anzahl + 1
            
print(anzahl)
