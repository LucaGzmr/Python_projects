
# um mehr Rechenoperatoren und Befehle nach Python zu Importieren, z.B. der float Befehl, um eine Zahl in einen String umzuwandeln. 
from math import *

# Die Rechenart wird für die if Statements festgelegt, um zu entscheiden welche Rechenart angewendet werden soll. 
rechenart = input("Schreibe welche Rechenart angewendet werden soll: ")

# Addition 
if (rechenart == "Addition") or (rechenart == "addieren") or (rechenart == "plus"):
    number1 = float(input("Schreibe eine Zahl: "))
    operator = input("Schreibe einen Rechenoperator: ")
    number2 = float(input("Schreibe eine weitere Zahl: "))
    if (operator == "+"):
        print(number1 + number2)
    else:
        print("Error: System64.exe")

# Subtraktion
elif (rechenart == "Subtraktion") or (rechenart == "subtrahieren") or (rechenart == "minus"):
    number1 = float(input("Schreibe eine Zahl: "))
    operator = input("Schreibe einen Rechenoperator: ")
    number2 = float(input("Schreibe eine weitere Zahl: "))
    if (operator == "-"):
        print(number1 - number2)
    else:
        print("Error: System64.exe")

# Multiplikation
elif (rechenart == "Multiplikation") or (rechenart == "multiplizieren") or (rechenart == "mal"):
    number1 = float(input("Schreibe eine Zahl: "))
    operator = input("Schreibe einen Rechenoperator: ")
    number2 = float(input("Schreibe eine weitere Zahl: "))
    if (operator == "*"):
        print(number1 * number2)
    else:
        print("Error: System64.exe")

# Division
elif (rechenart == "Division") or (rechenart == "dividieren") or (rechenart == "geteilt"):
    number1 = float(input("Schreibe eine Zahl: "))
    operator = input("Schreibe einen Rechenoperator: ")
    number2 = float(input("Schreibe eine weitere Zahl: "))
    if (operator == ":") or (operator == "/"):
        print(number1 / number2)
    else:
        print("Error: System64.exe")

# Potentzrechnung
elif (rechenart == "Potenzieren") or (rechenart == "potenzieren") or (rechenart == "Hochrechnen"):
    number1 = float(input("Schreibe eine Zahl: "))
    operator = input("Schreibe einen Rechenoperator: ")
    number2 = float(input("Schreibe eine weitere Zahl: "))
    if (operator == "^") or (operator == "Hoch") or (operator == "hoch"):
        print(pow(number1, number2))
    else:
        print("Error: System64.exe")

# Radizieren
elif (rechenart == "Radizieren") or (rechenart == "radizieren") or (rechenart == "Wurzel") or (rechenart == "Quadratwurzel") or (rechenart == "Wurzelziehen"):
    number1 = float(input("Schreibe eine Zahl: "))
    print(sqrt(number1))
    
else:
    print("Error: System64.exe")

