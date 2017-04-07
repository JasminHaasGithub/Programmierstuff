datei = open("beispiel-tabelle-2.csv")
Fahrgemeinschaft = dict()
import csv
with open("beispiel-tabelle-1.csv") and open("beispiel-tabelle-2.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Vorname"], row["Nachname"], row["KlasseID"], row["Freunde"])
        
        
