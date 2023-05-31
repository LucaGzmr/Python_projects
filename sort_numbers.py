
# Funktion, welche die einzelnen Zahlen als Parameter aufzählt, welche selber festgelegt wurden, um sie im If Statement anwenden zu können
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
    elif num4 >= num1 and num4 >= num2 and num4>= num3 and num4 >= num5:
        return num4
    
    # num5 ist die größte zahl
    elif num5 >= num1 and num5 >= num2 and num5 >= num3 and num5 >= num4:
        return num5
    else:
        print("Error: System64.exe")

# Die fünf Zahlen für die Parameter der Funktion 
print("Schreibe fünf Zahlen, bei jedem Eingabefeld jeweils eine Zahl:")
print(größer(input("Schreibe eine Zahl: "),
             input("Schreibe eine Zahl: "),
             input("Schreibe eine Zahl: "),
             input("Schreibe eine zahl: "),
             input("Schreibe eine Zahl: ")))
