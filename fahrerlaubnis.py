datei = open("beispiel-tabelle-2.csv")
Fahrgemeinschaft = dict()
import csv
with open("beispiel-tabelle-2.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Fahrgemeinschaft"] == "WAHR":
            print(row["Vorname"], row["Nachname"])
        
        
   
        
