import codecs
datei1 = open("abreise.txt", "w")


datei = open("beispiel-tabelle-1.csv")
zahl = 0

import csv
with open("beispiel-tabelle-1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not row["Abreise"] == "Bus":
            print(u"\u25A1 ", row["Nachname"], row["Vorname"], row["Notfallnummer 1"], row["Notfallnummer 2"], row["Notfallnummer 3"], "\n")
            zahl = zahl + 1
        
datei.close()
