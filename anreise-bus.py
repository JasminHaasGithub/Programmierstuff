import codecs
datei1 = open("anreise-bus.txt", "w")


datei = open("beispiel-tabelle-1.csv")
zahl = 0

import csv
with open("beispiel-tabelle-1.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Anreise"] == "Bus":
            print(u"\u25A1 ", row["Nachname"], row["Vorname"], row["Notfallnummer 1"], row["Notfallnummer 2"], row["Notfallnummer 3"])
            print("\n")
            zahl = zahl + 1
        
datei.close()
