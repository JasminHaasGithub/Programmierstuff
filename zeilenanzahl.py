datei = open("mbox.txt")
anzahl = 0
    
for zeile in datei:
    new_string = string.strip().split("_")
for _ in datei:
    anzahl = anzahl + 1
    
print(anzahl)
