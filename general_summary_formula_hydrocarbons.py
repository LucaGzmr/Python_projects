
print("\n")
print("aliphatische Kohlenwasserstoffe (Alkane = CnH(2*n)+2, Alkene = CnH(2*n), Alkine = CnH(2*n)-2, Alkanole = CnH(2*n)+2O")

# Kohlenwasserstoff festlegen
Kohlenwasserstoff = input("schreibe eine der Art von Kohlenwasserstoff: ")

# Summenformel Alkane
if Kohlenwasserstoff == "Alkane":
    n = int(input("Definiere n für die allgemeine Summenformel: "))
    if n > 0:
        print("\n")
        print("C" + str(n) + "H" + (str(2 * n + 2)))
        print("\n")
    else:
        print("Error: System64.exe")

# Summenformel Alkene
elif Kohlenwasserstoff == "Alkene":
    n = int(input("Definiere n für die allgemeine Summenformel: "))
    if n > 0:
        print("\n")
        print("C" + str(n) + "H" + str(2 * n))
        print("\n")
    else:
        print("Error: System64.exe")

# Summenformel Alkine
elif Kohlenwasserstoff == "Alkine":
    n = int(input("Definiere n für die allgemeine Summenformel: "))
    if n > 0:
        print("\n")
        print("C" + str(n) + "H" + str(2 * n - 2))
        print("\n")
    else:
        print("Error: System64.exe")

# Summenformel Alkanole
elif Kohlenwasserstoff == "Alkanole":
    n = int(input("Definiere n für die allgemeine Summenformel: "))
    if n > 0:
        print("\n")
        print("C" + str(n) + "H" + (str(2 * n + 2)) + "O")
        print("\n")

else:
    print("Error: System64.exe")