
# Variable für die while Schleife 
variable = True

# Die while schleife lopped immer wieder durch das Programm/Funktion
while variable: 

    # Parameter der Funktion ist die Variable auf der alles aufbaut
    def verschlüssele(satz):    

        # Platzhalter für die letztendliche Übersetztung
        übersetzung = ""

        # Variable "Buchstabe" wird durch for-loop hinugefügt die für das if Statement wichtig ist
        for buchstabe in satz: 

            # Wird geprüft, ob der Buchstabe generell klein ist spezifisch bezogen auf die individuellen Infos
            if buchstabe.islower():
                
                # Wird dann besagt, dass wenn der Buchstabe generell klein geschreiben ist + 
                # ein kleines a (Beispielbuchstabe) ist, dass dann der kleine Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
                # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
                if buchstabe == "a":
                    übersetzung += ersetzender_Buchstabe + "0"

                elif buchstabe == "b":
                    übersetzung += ersetzender_Buchstabe + "1"

                elif buchstabe == "c":
                    übersetzung += ersetzender_Buchstabe + "2"

                elif buchstabe == "d":
                    übersetzung += ersetzender_Buchstabe + "3"

                elif buchstabe == "e":
                    übersetzung += ersetzender_Buchstabe + "4"
            
                elif buchstabe == "f":
                    übersetzung += ersetzender_Buchstabe + "5"

                elif buchstabe == "g":
                    übersetzung += ersetzender_Buchstabe + "6"

                elif buchstabe == "h":
                    übersetzung += ersetzender_Buchstabe + "7"

                elif buchstabe == "i":
                    übersetzung += ersetzender_Buchstabe + "8"

                elif buchstabe == "j":
                    übersetzung += ersetzender_Buchstabe + "9"

                elif buchstabe == "k":
                    übersetzung += ersetzender_Buchstabe + "10"

                elif buchstabe == "l":
                    übersetzung += ersetzender_Buchstabe + "11"

                elif buchstabe == "m":
                    übersetzung += ersetzender_Buchstabe + "12"

                elif buchstabe == "n":
                    übersetzung += ersetzender_Buchstabe + "13"

                elif buchstabe == "o":
                    übersetzung += ersetzender_Buchstabe + "14"

                elif buchstabe == "p":
                    übersetzung += ersetzender_Buchstabe + "15"

                elif buchstabe == "q":
                    übersetzung += ersetzender_Buchstabe + "16"

                elif buchstabe == "r":
                    übersetzung += ersetzender_Buchstabe + "17"

                elif buchstabe == "s":
                    übersetzung += ersetzender_Buchstabe + "18"

                elif buchstabe == "t":
                    übersetzung += ersetzender_Buchstabe + "19"

                elif buchstabe == "u":
                    übersetzung += ersetzender_Buchstabe + "20"

                elif buchstabe == "v":
                    übersetzung += ersetzender_Buchstabe + "21"

                elif buchstabe == "w":
                    übersetzung += ersetzender_Buchstabe + "22"

                elif buchstabe == "x":
                    übersetzung += ersetzender_Buchstabe + "23"
        
                elif buchstabe == "y":
                    übersetzung += ersetzender_Buchstabe + "24"

                elif buchstabe == "z":
                    übersetzung += ersetzender_Buchstabe + "25"

                elif buchstabe == "ß":
                    übersetzung += ersetzender_Buchstabe + "26"

                elif buchstabe == "ä":
                    übersetzung += ersetzender_Buchstabe + "27"

                elif buchstabe == "ö":
                    übersetzung += ersetzender_Buchstabe + "28"

                elif buchstabe == "ü":
                    übersetzung += ersetzender_Buchstabe + "29"

                else:
                    übersetzung += buchstabe

            # Wird geprüft, ob der Buchstabe generell groß ist spezifisch bezogen auf die individuellen Infos
            elif buchstabe.isupper():
                
                # Wird dann besagt, dass wenn der Buchstabe generell groß geschreiben ist +
                # ein großes A (Beispielbuchstabe) ist, dass dann der große Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
                # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
                if buchstabe == "A":
                    übersetzung += ersetzender_Großbuchstabe + "0"

                elif buchstabe == "B":
                    übersetzung += ersetzender_Großbuchstabe + "1"

                elif buchstabe == "C":
                    übersetzung += ersetzender_Großbuchstabe + "2"

                elif buchstabe == "D":
                    übersetzung += ersetzender_Großbuchstabe + "3"

                elif buchstabe == "E":
                    übersetzung += ersetzender_Großbuchstabe + "4"

                elif buchstabe == "F":
                    übersetzung += ersetzender_Großbuchstabe + "5"

                elif buchstabe == "G":
                    übersetzung += ersetzender_Großbuchstabe + "6"

                elif buchstabe == "H":
                    übersetzung += ersetzender_Großbuchstabe + "7"

                elif buchstabe == "I":
                    übersetzung += ersetzender_Großbuchstabe + "8"

                elif buchstabe == "J":
                    übersetzung += ersetzender_Großbuchstabe + "9"

                elif buchstabe == "K":
                    übersetzung += ersetzender_Großbuchstabe + "10"

                elif buchstabe == "L":
                    übersetzung += ersetzender_Großbuchstabe + "11"

                elif buchstabe == "M":
                    übersetzung += ersetzender_Großbuchstabe + "12"

                elif buchstabe == "N":
                    übersetzung += ersetzender_Großbuchstabe + "13"

                elif buchstabe == "O":
                    übersetzung += ersetzender_Großbuchstabe + "14"

                elif buchstabe == "P":
                    übersetzung += ersetzender_Großbuchstabe + "15"

                elif buchstabe == "Q":
                    übersetzung += ersetzender_Großbuchstabe + "16"

                elif buchstabe == "R":
                    übersetzung += ersetzender_Großbuchstabe + "17"

                elif buchstabe == "S":
                    übersetzung += ersetzender_Großbuchstabe + "18"

                elif buchstabe == "T":
                    übersetzung += ersetzender_Großbuchstabe + "19"

                elif buchstabe == "U":
                    übersetzung += ersetzender_Großbuchstabe + "20"

                elif buchstabe == "V":
                    übersetzung += ersetzender_Großbuchstabe + "21"

                elif buchstabe == "W":
                    übersetzung += ersetzender_Großbuchstabe + "22"

                elif buchstabe == "X":
                    übersetzung += ersetzender_Großbuchstabe + "23"

                elif buchstabe == "Y":
                    übersetzung += ersetzender_Großbuchstabe + "24"

                elif buchstabe == "Z":
                    übersetzung += ersetzender_Großbuchstabe + "25" 

                elif buchstabe == "Ä":
                    übersetzung += ersetzender_Großbuchstabe + "26"

                elif buchstabe == "Ö":
                    übersetzung += ersetzender_Großbuchstabe + "27"

                elif buchstabe == "Ü":
                    übersetzung += ersetzender_Großbuchstabe + "28"

                else:
                    übersetzung += buchstabe

            # Wird geprüft, ob ein die variable buchstabe eine Zahl ist 
            elif buchstabe.isdigit():
                
                # Wird dann besagt, dass wenn die Variable buchstabe eine Zahl ist, dass dann ein # + ein A eingesetzt (Beispielbuchstabe bei 0) wird
                if int(buchstabe) == 0:
                    übersetzung += "#" + "A"

                elif int(buchstabe) == 1:
                    übersetzung += "#" + "B"

                elif int(buchstabe) == 2:
                    übersetzung += "#" + "C"

                elif int(buchstabe) == 3:
                    übersetzung += "#" + "D"

                elif int(buchstabe) == 4:
                    übersetzung += "#" + "E"

                elif int(buchstabe) == 5:
                    übersetzung += "#" + "F"

                elif int(buchstabe) == 6:
                    übersetzung += "#" + "G"

                elif int(buchstabe) == 7:
                    übersetzung += "#" + "H"

                elif int(buchstabe) == 8:
                    übersetzung += "#" + "I"

                elif int(buchstabe) == 9:
                    übersetzung += "#" + "J"    

                else:
                    übersetzung += buchstabe

            # wenn die oberen Bedingungen nicht erfüllt sind wird die Variable buchstabe unverändert gelassen
            else:
                übersetzung += buchstabe

        # Ergebnis 
        return übersetzung
    
    # Die Variablen für die If Statements
    print("\n")
    ersetzender_Großbuchstabe = "X"
    ersetzender_Buchstabe = "x"

    # Info die zu übersetzen/verändern ist 
    print(verschlüssele(input("Schreibe ein Wort/Satz: ")))
