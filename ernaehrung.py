import codecs
datei1 = open("liste-ernaehrung.txt", "w")


datei = open("beispiel-tabelle-1.csv") and open("beispiel-tabelle-2.csv")
zahl = 0
import csv
with open("beispiel-tabelle-1.csv") and open("beispiel-tabelle-2.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["Ernährung"])
        print(",")
        zahl = zahl + 1
        datei1.write(row["Ernährung"])
        datei1.write(", ")
        
datei.close()       
