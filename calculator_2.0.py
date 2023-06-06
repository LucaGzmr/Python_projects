
# um mehr Rechenoperatoren und Befehle nach Python zu Importieren, z.B. der float Befehl, um eine Zahl in einen String umzuwandeln. 
from math import *

# besagt, dass während der Fehler auftritt das unendlich lange durchläuft, bzw. generell die ganze Zeit auch nach einem Ergebniss unendlich lange durchläuft
while ValueError or ZeroDivisionError:
    # Die Rechenart wird für die if Statements festgelegt, um zu entscheiden welche Rechenart angewendet werden soll
    print("\n")
    rechenart = input("Schreibe eine Rechenart: ")

    # Addition
    if (rechenart == "Addition") or (rechenart == "addieren") or (rechenart == "plus") or (rechenart == "+"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            number2 = float(input("Schreibe eine weitere Zahl: "))
            print(number1 + number2)
        
        except ValueError as err1:
            print(err1)
        
    # Subtraktion
    elif (rechenart == "Subtraktion") or (rechenart == "subtrahieren") or (rechenart == "minus") or (rechenart == "-"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            number2 = float(input("Schreibe eine weitere Zahl: "))
            print(number1 - number2)

        except ValueError as err1:
            print(err1)

    # Multiplikation
    elif (rechenart == "Multiplikation") or (rechenart == "multiplizieren") or (rechenart == "mal") or (rechenart == "*"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            number2 = float(input("Schreibe eine weitere Zahl: "))
            print(number1 * number2)

        except ValueError as err1:
            print(err1)    

    # Division
    elif (rechenart == "Division") or (rechenart == "dividieren") or (rechenart == "geteilt") or (rechenart == ":") or (rechenart == "/"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            number2 = float(input("Schreibe eine weitere Zahl: "))
            print(number1 / number2)

        except ValueError as err1:
            print(err1)  
        except ZeroDivisionError as err2:
            print(err2)

    # Potentzrechnung
    elif (rechenart == "Potenzieren") or (rechenart == "Hochrechnen") or (rechenart == "Hoch") or (rechenart == "hoch") or (rechenart == "°") or (rechenart == "^"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            number2 = float(input("Schreibe eine weitere Zahl: "))
            print(pow(number1, number2))

        except ValueError as err1:
            print(err1)

    # Radizieren
    elif (rechenart == "Radizieren") or (rechenart == "radizieren") or (rechenart == "Wurzel") or (rechenart == "Quadratwurzel") or (rechenart == "Wurzelziehen"):

        # wird geprüft ob der Fehler auftritt
        try:
            number1 = float(input("Schreibe eine Zahl: "))
            print(sqrt(number1))
        
        except ValueError as err1:
            print(err1)
