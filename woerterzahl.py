datei = open("mbox.txt")
anzahl = 0

for zeile in datei:
    new_string = zeile.strip().split(" ")
    for wort in new_string:
        anzahl = anzahl + 1
    
print(anzahl)        
