
print("\n")
print("Schreibe jeweils eine Zahl ")
number1 = input("Zahl1: ")
number2 = input("Zahl2: ")

# Mit diesem Block wird direkt am Anfang geprüft ob die fahler auftraten, wenn nicht dann wird direkt zu else gesprungen
try:
    result1 = float(number1) + float(number2)
    result2 = float(number1) - float(number2)
    result3 = float(number1) * float(number2)
    result4 = float(number1) / float(number2)

except ZeroDivisionError as err1:
    print(err1)

except ValueError as err2:
    print(err2)

# Wenn die Fehler auftreten wird nach einer erneuten Eingabe der zahlen gebeten und die Ergebnisse werden aufs Neue versucht herauszufinden
if ZeroDivisionError or ValueError:

    # Die while Schleife besagt, dass während einer der Fehler auftritt das Programm immer wiederholt wird.
    while ZeroDivisionError or ValueError:
        print("\n")
        print("Schreibe jeweils eine Zahl ")
        number1 = input("Zahl1: ")
        number2 = input("Zahl2: ")

        # Mit deisem Block wird überprüft ob nach erneuteer Eingabe der Fehler immer noch auftritt. Falls ja wird wieder nach einer erneuten Eingabe gefordert.
        try:
            result1 = float(number1) + float(number2)
            result2 = float(number1) - float(number2)
            result3 = float(number1) * float(number2)
            result4 = float(number1) / float(number2)
            print("\n")
            print("Summe: " + str(result1))
            print("Differenz: " + str(result2))
            print("Produkt: " + str(result3))
            print("Quotient: " + str(result4))
            
        except ZeroDivisionError as err1:
            print(err1)

        except ValueError as err2:
            print(err2) 

# wenn die fahler nicht auftreten werden dei Ergebnisse ausgespuckt
else:
    result1 = float(number1) + float(number2)
    result2 = float(number1) - float(number2)
    result3 = float(number1) * float(number2)
    result4 = float(number1) / float(number2)
    print("Summe: " + str(result1))
    print("Differenz: " + str(result2))
    print("Produkt: " + str(result3))
    print("Quotient: " + str(result4))
