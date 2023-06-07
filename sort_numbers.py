
# Definiert die Variable "numbers" fdür die while schleife 
num1 = ""
num2 = ""
num3 = ""
num4 = ""
num5 = ""
numbers = num1, num2, num3, num4, num5

# bewirkt, dass der Prozess der Eingabe bis zum ergebniss immer wiederholt wird 
while numbers:

    # Funktion, die die Funktionen als Parameter definiert (mit eigenen Informationen versehen), um sie dann in if Statements zu benutzten 
    def größer(num1, num2, num3, num4, num5): 
            
        # num1 ist die größte zahl
        if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
            return num1

        # num2 ist die größte zahl
        elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
            return num2

        # num3 ist die größte zahl
        elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
            return num3

        # num4 ist die größte zahl
        elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
            return num4

        # num5 ist die größte zahl
        elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
            return num5

        else:
            print("Error: System64.exe")

    # Eingabe für Informationen der Tuple der Funktion
    print("\n")
    print("Schreibe fünf Zahlen, bei jedem Eingabefeld jeweils eine Zahl:")
    print(größer(input("Schreibe eine Zahl: "),
                input("Schreibe eine Zahl: "),
                input("Schreibe eine Zahl: "),
                input("Schreibe eine Zahl: "),
                input("Schreibe eine Zahl: ")))
