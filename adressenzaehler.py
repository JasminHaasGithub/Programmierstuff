datei = open("mbox.txt")
Adressen = dict()

for zeile in datei:  
    neue_zeile = zeile.strip().split(" ")
    if neue_zeile[0].startswith("From"):
        if neue_zeile[1] not in Adressen:
            Adressen[neue_zeile[1]] = 1
        else:
            Adressen[neue_zeile[1]] = Adressen[neue_zeile[1]] + 1
                     
print(Adressen)            
    
    
    

           
                
                                 
