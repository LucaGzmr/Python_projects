
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
    # Variable für die While Schleife
    Variable = True

    # While Schleife damit das ganze Programm von vorne gestartet wird
    while Variable:

        # die Funktion bestimmt den Parameter als Variable satz, wo index = 0 gesetzt wird und eine variable erstellt wird mit keiner information als Lückenfüller
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
        print("\n")
        print(entschlüssele(input("Schreibe die zu entschlüsselnde Information: ")))
