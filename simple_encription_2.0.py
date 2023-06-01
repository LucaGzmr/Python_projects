
# Die Variablen für die If Statements werden mit Individuellen Informationen versehen 
zu_ersetzender_Buchstabe = input("Nenne Buchstaben die ausgetsuscht werden sollen: ")
ersetzender_Großbuchstabe = input("Nenne Großbuchstaben die eingesetzt werden sollen: ")
ersetzender_Buchstabe = input("Nenne Buchstaben die eingesetzt werden sollen: ")

# Parameter der Funktion ist die Variable auf der alles aufbaut
def übersetze(satz):

    # Platzhalter für die letztendliche Übersetztung
    übersetzung = ""

    # Variable "Buchstabe" wird durch for-loop hinugefügt die für das if Statement wichtig ist
    for buchstabe in satz: 

        # wird bestimmt, dass der Buchstabe generell klein ist spezifisch bezogen auf die individuellen Infos
        if buchstabe.lower() in zu_ersetzender_Buchstabe:
            
            # wird dann besagt, dass wenn der Buchstabe generell (Wort) klein geschreiben ist + 
            # ein kleines a (Beispielbuchstabe) ist, dass dann der kleine Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
            # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
            if buchstabe.islower() and (buchstabe == "a"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(0)

            elif buchstabe.islower() and (buchstabe == "b"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(1)

            elif buchstabe.islower() and (buchstabe == "c"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(2)

            elif buchstabe.islower() and (buchstabe == "d"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(3)

            elif buchstabe.islower() and (buchstabe == "e"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(4)
        
            elif buchstabe.islower() and (buchstabe == "f"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(5)

            elif buchstabe.islower() and (buchstabe == "g"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(6)

            elif buchstabe.islower() and (buchstabe == "h"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(7)

            elif buchstabe.islower() and (buchstabe == "i"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(8)

            elif buchstabe.islower() and (buchstabe == "j"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(9)

            elif buchstabe.islower() and (buchstabe == "k"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(10)

            elif buchstabe.islower() and (buchstabe == "l"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(11)

            elif buchstabe.islower() and (buchstabe == "m"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(12)

            elif buchstabe.islower() and (buchstabe == "n"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(13)

            elif buchstabe.islower() and (buchstabe == "o"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(14)

            elif buchstabe.islower() and (buchstabe == "p"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(15)

            elif buchstabe.islower() and (buchstabe == "q"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(16)

            elif buchstabe.islower() and (buchstabe == "r"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(17)

            elif buchstabe.islower() and (buchstabe == "s"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(18)

            elif buchstabe.islower() and (buchstabe == "t"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(19)

            elif buchstabe.islower() and (buchstabe == "u"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(20)

            elif buchstabe.islower() and (buchstabe == "v"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(21)

            elif buchstabe.islower() and (buchstabe == "w"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(22)

            elif buchstabe.islower() and (buchstabe == "x"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(23)
        
            elif buchstabe.islower() and (buchstabe == "y"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(24)

            elif buchstabe.islower() and (buchstabe == "z"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(25)

            elif buchstabe.islower() and (buchstabe == "ß"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(26)

            elif buchstabe.islower() and (buchstabe == "ä"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(27)

            elif buchstabe.islower() and (buchstabe == "ö"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(28)

            elif buchstabe.islower() and (buchstabe == "Ü"):
                    übersetzung = übersetzung + ersetzender_Buchstabe + str(29)

            # wenn diese Buchstaben im selber gesetzten Wort nicht in großgeschreibener Form vorkommen, werden die groß geschreibene Buchstaben erstezt 
            else: 
                übersetzung = übersetzung + ersetzender_Großbuchstabe

        # wird bestimmt, dass der Buchstabe generell groß ist spezifisch bezogen auf die individuellen Infos
        elif buchstabe.upper() in zu_ersetzender_Buchstabe:
            
            # wird dann besagt, dass wenn der Buchstabe generell (Wort) groß geschreiben ist +
            # ein großes A (Beispielbuchstabe) ist, dass dann der große Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
            # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
            if buchstabe.isupper() and (buchstabe == "A"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(0)

            elif buchstabe.isupper() and (buchstabe == "B"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(1)

            elif buchstabe.isupper() and (buchstabe == "C"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(2)

            elif buchstabe.isupper() and (buchstabe == "D"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(3)

            elif buchstabe.isupper() and (buchstabe == "E"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(4)

            elif buchstabe.isupper() and (buchstabe == "F"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(5)

            elif buchstabe.isupper() and (buchstabe == "G"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(6)

            elif buchstabe.isupper() and (buchstabe == "H"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(7)

            elif buchstabe.isupper() and (buchstabe == "I"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(8)

            elif buchstabe.isupper() and (buchstabe == "J"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(9)

            elif buchstabe.isupper() and (buchstabe == "K"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(10)

            elif buchstabe.isupper() and (buchstabe == "L"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(11)

            elif buchstabe.isupper() and (buchstabe == "M"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(12)

            elif buchstabe.isupper() and (buchstabe == "N"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(13)

            elif buchstabe.isupper() and (buchstabe == "O"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(14)

            elif buchstabe.isupper() and (buchstabe == "P"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(15)

            elif buchstabe.isupper() and (buchstabe == "Q"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(16)

            elif buchstabe.isupper() and (buchstabe == "R"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(17)

            elif buchstabe.isupper() and (buchstabe == "S"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(18)

            elif buchstabe.isupper() and (buchstabe == "T"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(19)

            elif buchstabe.isupper() and (buchstabe == "U"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(20)

            elif buchstabe.isupper() and (buchstabe == "V"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(21)

            elif buchstabe.isupper() and (buchstabe == "W"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(22)

            elif buchstabe.isupper() and (buchstabe == "X"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(23)

            elif buchstabe.isupper() and (buchstabe == "Y"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(24)

            elif buchstabe.isupper() and (buchstabe == "Z"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(25) 

            elif buchstabe.isupper() and (buchstabe == "Ä"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(26)

            elif buchstabe.isupper() and (buchstabe == "Ö"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(27)

            elif buchstabe.isupper() and (buchstabe == "Ü"):
                übersetzung = übersetzung + ersetzender_Großbuchstabe + str(28)

            # wenn diese Buchstaben im selber gesetzten Wort nicht in kleingeschreibener Form vorkommen, werden die durch großgeschreibene Buchstaben erstezt
            else:
                übersetzung = übersetzung + ersetzender_Buchstabe
        
        # wenn keiner dieser Fälle auftreten, so wird das selber gesetzte Wort unverändert gelassen 
        else:
            übersetzung = übersetzung + buchstabe
            
    # Ergebnis 
    return übersetzung

# Info die zu übersetzen/verändern ist 
print(übersetze(input("Schreibe ein Wort/Satz: ")))
