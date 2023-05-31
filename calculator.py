
# Die zwei Variablen number1 und number2 gelten für alle 4 Rechenformen
# Wenn number1 > number2 dann ist das Ergebnis bei Subtraktion und Division result2 > 0 und result4 > 0
# Wenn number1 < number2 dan ist das Ergebnis bei Subtraktion und Division result2 < 0 und result4 >= 0

print("\n")
print("Schreibe jeweils eine Zahl ")
number1 = input("Zahl1: ")
number2 = input("Zahl2: ")
print("\n")

# Addition
result1 = float(number1) + float(number2)

# Subtraktion
result2 = float(number1) - float(number2)

# Multiplikation
result3 = float(number1) * float(number2)

# Division
result4 = float(number1) / float(number2)

print("Summe: " + str(result1))
print("Differenz: " + str(result2))
print("Produkt: " + str(result3))
print("Quotient: " + str(result4))
