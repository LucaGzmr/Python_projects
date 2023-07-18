
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
