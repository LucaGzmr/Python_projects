
Kohlenwasserstoff = True

# die Schleife sorgt dafür, dass immer wieder durch das Programm geloopt wird
while Kohlenwasserstoff:

    print("\n")
    print("aliphatische Kohlenwasserstoffe (Alkane = CnH(2*n)+2, Alkene = CnH(2*n), Alkine = CnH(2*n)-2, Alkanole = CnH(2*n)+2O, Carbonyle = CnH(2*n)+O")
    Kohlenwasserstoff = input("schreibe eine der Art von Kohlenwasserstoff: ")

    # Summenformel Alkane
    if Kohlenwasserstoff == "Alkane" or Kohlenwasserstoff == "alkane":
        try:
            n = int(input("Definiere n für die allgemeine Summenformel: "))
            if n > 0:
                print("C" + str(n) + "H" + (str(2 * n + 2)))
            else:
                print("Error: System64.exe")
        except ValueError as err:    
            print(err)

    # Summenformel Alkene
    elif Kohlenwasserstoff == "Alkene" or Kohlenwasserstoff == "alkene":
        try:
            n = int(input("Definiere n für die allgemeine Summenformel: "))
            if n > 0:
                print("C" + str(n) + "H" + str(2 * n))
            else:
                print("Error: System64.exe")
        except ValueError as err:
            print(err)

    # Summenformel Alkine
    elif Kohlenwasserstoff == "Alkine" or Kohlenwasserstoff == "alkine":
        try:
            n = int(input("Definiere n für die allgemeine Summenformel: "))
            if n > 0:
                print("C" + str(n) + "H" + str(2 * n - 2))
            else:
                print("Error: System64.exe")
        except ValueError as err:
            print(err)

    # Summenformel Alkanole
    elif Kohlenwasserstoff == "Alkanole" or Kohlenwasserstoff == "alkanole":
        try:
            n = int(input("Definiere n für die allgemeine Summenformel: "))
            if n > 0:
                print("C" + str(n) + "H" + str(2 * n + 2) + "O")
            else:
                print("Error: System64.exe")
        except ValueError as err:
            print(err)

    # Summenformel Carbonyle        
    elif Kohlenwasserstoff == "Carbonyle" or Kohlenwasserstoff == "carbonyle":
        try:
            n = int(input("Definiere n für die allgemeine Summenformel: "))
            if n > 0:
                print("C" + str(n) + "H" + str(2 * n) + "O")
            else:
                print("Error: System64.exe")
        except ValueError as err:
            print(err)
            