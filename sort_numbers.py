
sort = True

while sort:

    try:

        def größer(num1, num2, num3, num4, num5):
            # alle einzelnen num mern in eine Liste
            numbers = [num1, num2, num3, num4, num5]
            # Konvertierung der Eingabe in Gleitkommazahlen 
            numbers = [float(num) for num in numbers]
            # Annahme: Die erste Zahl ist vorläufig die größte
            größte_zahl = numbers[0]
            
            # In Schleife wird jede Zahl mit der bisher größten Zahl verglichen.
            # Wenn die aktuelle Zahl größer ist als die bisher größte Zahl, wird die aktuelle Zahl als die neue größte Zahl festgelegt.
            for num in numbers[1:]:
                if num > größte_zahl:
                    größte_zahl = num

            # Ergebnis nachdem alle zahlen in Liste überprüft wurden
            return größte_zahl

        print("\n")
        print("Schreibe fünf Zahlen, bei jedem Eingabefeld jeweils eine Zahl")
        print(größer(input("Schreibe eine Zahl: "),
                    input("Schreibe eine Zahl: "),
                    input("Schreibe eine Zahl: "),
                    input("Schreibe eine Zahl: "),
                    input("Schreibe eine Zahl: ")))
        
    except ValueError as err:
        print(err)
