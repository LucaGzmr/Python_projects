
# Passwort, welcher die Lösung definiert
passwort = "security_cript"
# Platzhalter für die einzugebenen Versuche
versuche = ""
# Definiert die theoretisch gesehen minimale Anzahl an Versuchen und = 0 da python ab 0 beginnt zu Zählen
anzahl_Versuche = 0
# Definiert die maximale Anzahl an Versuchen
max_Versuche = 3
max_Versuche_erreicht = False 

print("\n")

# While schleife Die regelt ob das Passwort richtig eingegeben wird
while versuche != passwort and (max_Versuche_erreicht == False):
    if anzahl_Versuche < max_Versuche:
        versuche = input("Passwort: ")
        anzahl_Versuche += 1
        
    else:
        max_Versuche_erreicht = True

if max_Versuche_erreicht == True:
    print("Invalid Input")

else:
    print("Access confirmed")

    # Variable für die while Schleife 
    variable = True

    # Die while schleife lopped immer wieder durch das Programm/Funktion
    while variable: 

        # Parameter der Funktion ist die Variable auf der alles aufbaut
        def verschlüssele(satz):    

            # Platzhalter für die letztendliche Übersetztung
            verschlüsselung = ""

            # Variable "Buchstabe" wird durch for-loop hinugefügt die für das if Statement wichtig ist
            for buchstabe in satz: 

                # Wird geprüft, ob der Buchstabe generell klein ist spezifisch bezogen auf die individuellen Infos
                if buchstabe.islower():
                    
                    # Wird dann besagt, dass wenn der Buchstabe generell klein geschreiben ist + 
                    # ein kleines a (Beispielbuchstabe) ist, dass dann der kleine Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
                    # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
                    if buchstabe == "a":
                        verschlüsselung += ersetzender_Buchstabe + "0"

                    elif buchstabe == "b":
                        verschlüsselung += ersetzender_Buchstabe + "1"

                    elif buchstabe == "c":
                        verschlüsselung += ersetzender_Buchstabe + "2"

                    elif buchstabe == "d":
                        verschlüsselung += ersetzender_Buchstabe + "3"

                    elif buchstabe == "e":
                        verschlüsselung += ersetzender_Buchstabe + "4"
                
                    elif buchstabe == "f":
                        verschlüsselung += ersetzender_Buchstabe + "5"

                    elif buchstabe == "g":
                        verschlüsselung += ersetzender_Buchstabe + "6"

                    elif buchstabe == "h":
                        verschlüsselung += ersetzender_Buchstabe + "7"

                    elif buchstabe == "i":
                        verschlüsselung += ersetzender_Buchstabe + "8"

                    elif buchstabe == "j":
                        verschlüsselung += ersetzender_Buchstabe + "9"

                    elif buchstabe == "k":
                        verschlüsselung += ersetzender_Buchstabe + "10"

                    elif buchstabe == "l":
                        verschlüsselung += ersetzender_Buchstabe + "11"

                    elif buchstabe == "m":
                        verschlüsselung += ersetzender_Buchstabe + "12"

                    elif buchstabe == "n":
                        verschlüsselung += ersetzender_Buchstabe + "13"

                    elif buchstabe == "o":
                        verschlüsselung += ersetzender_Buchstabe + "14"

                    elif buchstabe == "p":
                        verschlüsselung += ersetzender_Buchstabe + "15"

                    elif buchstabe == "q":
                        verschlüsselung += ersetzender_Buchstabe + "16"

                    elif buchstabe == "r":
                        verschlüsselung += ersetzender_Buchstabe + "17"

                    elif buchstabe == "s":
                        verschlüsselung += ersetzender_Buchstabe + "18"

                    elif buchstabe == "t":
                        verschlüsselung += ersetzender_Buchstabe + "19"

                    elif buchstabe == "u":
                        verschlüsselung += ersetzender_Buchstabe + "20"

                    elif buchstabe == "v":
                        verschlüsselung += ersetzender_Buchstabe + "21"

                    elif buchstabe == "w":
                        verschlüsselung += ersetzender_Buchstabe + "22"

                    elif buchstabe == "x":
                        verschlüsselung += ersetzender_Buchstabe + "23"
            
                    elif buchstabe == "y":
                        verschlüsselung += ersetzender_Buchstabe + "24"

                    elif buchstabe == "z":
                        verschlüsselung += ersetzender_Buchstabe + "25"

                    elif buchstabe == "ß":
                        verschlüsselung += ersetzender_Buchstabe + "26"

                    elif buchstabe == "ä":
                        verschlüsselung += ersetzender_Buchstabe + "27"

                    elif buchstabe == "ö":
                        verschlüsselung += ersetzender_Buchstabe + "28"

                    elif buchstabe == "ü":
                        verschlüsselung += ersetzender_Buchstabe + "29"

                    else:
                        verschlüsselung += buchstabe

                # Wird geprüft, ob der Buchstabe generell groß ist spezifisch bezogen auf die individuellen Infos
                elif buchstabe.isupper():
                    
                    # Wird dann besagt, dass wenn der Buchstabe generell groß geschreiben ist +
                    # ein großes A (Beispielbuchstabe) ist, dass dann der große Buchstabe und die 0 (Beispielzahl) dafür ersetzt werden
                    # mit dem Prinzip werden alle anderen Buchstaben fortgeführt
                    if buchstabe == "A":
                        verschlüsselung += ersetzender_Großbuchstabe + "0"

                    elif buchstabe == "B":
                        verschlüsselung += ersetzender_Großbuchstabe + "1"

                    elif buchstabe == "C":
                        verschlüsselung += ersetzender_Großbuchstabe + "2"

                    elif buchstabe == "D":
                        verschlüsselung += ersetzender_Großbuchstabe + "3"

                    elif buchstabe == "E":
                        verschlüsselung += ersetzender_Großbuchstabe + "4"

                    elif buchstabe == "F":
                        verschlüsselung += ersetzender_Großbuchstabe + "5"

                    elif buchstabe == "G":
                        verschlüsselung += ersetzender_Großbuchstabe + "6"

                    elif buchstabe == "H":
                        verschlüsselung += ersetzender_Großbuchstabe + "7"

                    elif buchstabe == "I":
                        verschlüsselung += ersetzender_Großbuchstabe + "8"

                    elif buchstabe == "J":
                        verschlüsselung += ersetzender_Großbuchstabe + "9"

                    elif buchstabe == "K":
                        verschlüsselung += ersetzender_Großbuchstabe + "10"

                    elif buchstabe == "L":
                        verschlüsselung += ersetzender_Großbuchstabe + "11"

                    elif buchstabe == "M":
                        verschlüsselung += ersetzender_Großbuchstabe + "12"

                    elif buchstabe == "N":
                        verschlüsselung += ersetzender_Großbuchstabe + "13"

                    elif buchstabe == "O":
                        verschlüsselung += ersetzender_Großbuchstabe + "14"

                    elif buchstabe == "P":
                        verschlüsselung += ersetzender_Großbuchstabe + "15"

                    elif buchstabe == "Q":
                        verschlüsselung += ersetzender_Großbuchstabe + "16"

                    elif buchstabe == "R":
                        verschlüsselung += ersetzender_Großbuchstabe + "17"

                    elif buchstabe == "S":
                        verschlüsselung += ersetzender_Großbuchstabe + "18"

                    elif buchstabe == "T":
                        verschlüsselung += ersetzender_Großbuchstabe + "19"

                    elif buchstabe == "U":
                        verschlüsselung += ersetzender_Großbuchstabe + "20"

                    elif buchstabe == "V":
                        verschlüsselung += ersetzender_Großbuchstabe + "21"

                    elif buchstabe == "W":
                        verschlüsselung += ersetzender_Großbuchstabe + "22"

                    elif buchstabe == "X":
                        verschlüsselung += ersetzender_Großbuchstabe + "23"

                    elif buchstabe == "Y":
                        verschlüsselung += ersetzender_Großbuchstabe + "24"

                    elif buchstabe == "Z":
                        verschlüsselung += ersetzender_Großbuchstabe + "25" 

                    elif buchstabe == "Ä":
                        verschlüsselung += ersetzender_Großbuchstabe + "26"

                    elif buchstabe == "Ö":
                        verschlüsselung += ersetzender_Großbuchstabe + "27"

                    elif buchstabe == "Ü":
                        verschlüsselung += ersetzender_Großbuchstabe + "28"

                    else:
                        verschlüsselung += buchstabe

                # Wird geprüft, ob ein die variable buchstabe eine Zahl ist 
                elif buchstabe.isdigit():
                    
                    # Wird dann besagt, dass wenn die Variable buchstabe eine Zahl ist, dass dann ein # + ein A eingesetzt (Beispielbuchstabe bei 0) wird
                    if int(buchstabe) == 0:
                        verschlüsselung += "#" + "A"

                    elif int(buchstabe) == 1:
                        verschlüsselung += "#" + "B"

                    elif int(buchstabe) == 2:
                        verschlüsselung += "#" + "C"

                    elif int(buchstabe) == 3:
                        verschlüsselung += "#" + "D"

                    elif int(buchstabe) == 4:
                        verschlüsselung += "#" + "E"

                    elif int(buchstabe) == 5:
                        verschlüsselung += "#" + "F"

                    elif int(buchstabe) == 6:
                        verschlüsselung += "#" + "G"

                    elif int(buchstabe) == 7:
                        verschlüsselung += "#" + "H"

                    elif int(buchstabe) == 8:
                        verschlüsselung += "#" + "I"

                    elif int(buchstabe) == 9:
                        verschlüsselung += "#" + "J"    

                    else:
                        verschlüsselung += buchstabe

                # wenn die oberen Bedingungen nicht erfüllt sind wird die Variable buchstabe unverändert gelassen
                else:
                    verschlüsselung += buchstabe

            # Ergebnis 
            return verschlüsselung
        
        # Die Variablen für die If Statements
        print("\n")
        ersetzender_Großbuchstabe = "X"
        ersetzender_Buchstabe = "x"

        # Info die zu verschlüsseln ist 
        print(verschlüssele(input("Schreibe die zu verschlüsselnde Information: ")))

        decript = input("Entschlüsselung?: ")

        if decript == "ja" or decript == "Ja" or decript == "yes" or decript == "Yes":

            def entschlüssele(satz):
                entschlüsselung = ""
                index = 0
                
                # Die While Sschleife gilt solange der index kleier der Länge von satz
                while index < len(satz):
                    zeichen = satz[index]

                    # Wenn ein Leerzeichen vorkommt, dann wird das ohne Veränderung in das Ergebnis eingesetzt
                    if satz[index] == " ":
                        entschlüsselung += " "

                    # Wenn das Zeichen ein "X" ist, wird der Index um 1 erhöht, um zum nächsten Zeichen zu gelangen und die zahl wird in der Variable gespeichert
                    elif satz[index] == "X":
                        index += 1
                        zahl = ""
                        zahl += satz[index]
                        
                        # Wird überprüft, ob index + 1 kleiner len(satz) ist und ob das nächste Zeichen eine Ziffer ist und die zahl wird in Variable gespeichert
                        if index + 1 < len(satz):
                            if satz[index + 1].isdigit():
                                index += 1
                                zahl += satz[index]
                        
                        # Zu jeder zahl nach dem X gibt es ein dazugehörigen Buchstaben
                        # Durch das Speichern der einzelnen Ziffern in der Variable zahl, funktioniert das auch bei zweistelligen Zahlen
                        if zahl == "0":
                            entschlüsselung += "A"

                        elif zahl == "1":
                            entschlüsselung += "B"

                        elif zahl == "2":
                            entschlüsselung += "C"

                        elif zahl == "3":
                            entschlüsselung += "D"

                        elif zahl == "4":
                            entschlüsselung += "E"

                        elif zahl == "5":
                            entschlüsselung += "F"

                        elif zahl == "6":
                            entschlüsselung += "G"

                        elif zahl == "7":
                            entschlüsselung += "H"

                        elif zahl == "8":
                            entschlüsselung += "I"

                        elif zahl == "9":
                            entschlüsselung += "J"

                        elif zahl == "10":
                            entschlüsselung += "K"

                        elif zahl == "11":
                            entschlüsselung += "L"

                        elif zahl == "12":
                            entschlüsselung += "M"

                        elif zahl == "13":
                            entschlüsselung += "N"

                        elif zahl == "14":
                            entschlüsselung += "O"

                        elif zahl == "15":
                            entschlüsselung += "P"

                        elif zahl == "16":
                            entschlüsselung += "Q"

                        elif zahl == "17":
                            entschlüsselung += "R"

                        elif zahl == "18":
                            entschlüsselung += "S"

                        elif zahl == "19":
                            entschlüsselung += "T"

                        elif zahl == "20":
                            entschlüsselung += "U"

                        elif zahl == "21":
                            entschlüsselung += "V"

                        elif zahl == "22":
                            entschlüsselung += "W"

                        elif zahl == "23":
                            entschlüsselung += "X"

                        elif zahl == "24":
                            entschlüsselung += "Y"

                        elif zahl == "25":
                            entschlüsselung += "Z"

                        elif zahl == "26":
                            entschlüsselung += "Ä"

                        elif zahl == "27":
                            entschlüsselung += "Ö"

                        elif zahl == "28":
                            entschlüsselung += "Ü"

                        else:
                            entschlüsselung += zeichen

                    # Wenn das Zeichen ein "x" ist, wird der Index um 1 erhöht, um zum nächsten Zeichen zu gelangen und die zahl wird in der Variable gespeichert
                    elif satz[index] == "x":
                        index += 1
                        zahl = ""
                        zahl += satz[index] 

                        # Wird überprüft, ob index + 1 kleiner len(satz) ist und ob das nächste Zeichen eine Ziffer ist und die zahl wird in Variable gespeichert
                        if index + 1 < len(satz):
                            if satz[index + 1].isdigit():
                                index += 1
                                zahl += satz[index]

                        # Zu jeder zahl nach dem x gibt es ein dazugehörigen Buchstaben
                        # Durch das Speichern der einzelnen Ziffern in der Variable zahl, funktioniert das auch bei zweistelligen Zahlen
                        if zahl == "0":
                            entschlüsselung += "a"

                        elif zahl == "1":
                            entschlüsselung += "b"

                        elif zahl == "2":
                            entschlüsselung += "c"

                        elif zahl == "3":
                            entschlüsselung += "d"

                        elif zahl == "4":
                            entschlüsselung += "e"

                        elif zahl == "5":
                            entschlüsselung += "f"

                        elif zahl == "6":
                            entschlüsselung += "g"

                        elif zahl == "7":
                            entschlüsselung += "h"

                        elif zahl == "8":
                            entschlüsselung += "i"

                        elif zahl == "9":
                            entschlüsselung += "j"

                        elif zahl == "10":
                            entschlüsselung += "k"

                        elif zahl == "11":
                            entschlüsselung += "l"

                        elif zahl == "12":
                            entschlüsselung += "m"

                        elif zahl == "13":
                            entschlüsselung += "n"

                        elif zahl == "14":
                            entschlüsselung += "o"

                        elif zahl == "15":
                            entschlüsselung += "p"

                        elif zahl == "16":
                            entschlüsselung += "q"

                        elif zahl == "17":
                            entschlüsselung += "r"

                        elif zahl == "18":
                            entschlüsselung += "s"

                        elif zahl == "19":
                            entschlüsselung += "t"

                        elif zahl == "20":
                            entschlüsselung += "u"

                        elif zahl == "21":
                            entschlüsselung += "v"

                        elif zahl == "22":
                            entschlüsselung += "w"

                        elif zahl == "23":
                            entschlüsselung += "x"

                        elif zahl == "24":
                            entschlüsselung += "y"

                        elif zahl == "25":
                            entschlüsselung += "z"

                        elif zahl == "26":
                            entschlüsselung += "ß"

                        elif zahl == "27":
                            entschlüsselung += "ä"

                        elif zahl == "28":
                            entschlüsselung += "ö"

                        elif zahl == "29":
                            entschlüsselung += "ü"

                        else:
                            entschlüsselung += zeichen

                    # Wenn das Zeichen ein "#" ist, wird der Index um 1 erhöht, um zum nächsten Zeichen zu gelangen
                    elif satz[index] == "#":
                        index += 1

                        # Zu jedem Buchstaben nach dem # gibt es eine dazugehörige zahl
                        if satz[index] == "A":
                            entschlüsselung += "0"

                        elif satz[index] == "B":
                            entschlüsselung += "1"

                        elif satz[index] == "C":
                            entschlüsselung += "2"

                        elif satz[index] == "D":
                            entschlüsselung += "3"

                        elif satz[index] == "E":
                            entschlüsselung += "4"

                        elif satz[index] == "F":
                            entschlüsselung += "5"

                        elif satz[index] == "G":
                            entschlüsselung += "6"

                        elif satz[index] == "H":
                            entschlüsselung += "7"

                        elif satz[index] == "I":
                            entschlüsselung += "8"

                        elif satz[index] == "J":
                            entschlüsselung += "9"

                        else:
                            entschlüsselung += zeichen    
                    
                    # wenn die oberen Bedingungen nicht erfüllt sind wird die Variable zeichen unverändert gelassen
                    else:
                        entschlüsselung += zeichen

                    # Der index wird um 1 erhöht um zum nächsten zeichen im Satz zu gehen
                    index += 1

                # Ergebnis
                return entschlüsselung
            
            # Info die zu entschlüsseln ist
            print(entschlüssele(input("Schreibe die zu entschlüsselnde Information: ")))

        elif decript == "nein" or decript == "Nein" or decript == "no" or decript == "No":
            print("decription error")
