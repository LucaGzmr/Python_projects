
# Parameter weriden gesetzt
def exponent_function (basis, exponent):
    ergebnis = 1
    # range gibt durtch den  gesetztenm Exponenten an wie oft durch die for-loop geloopt werden soll 
    for index in range(exponent):
        # da ergenbis = 1 gesetzt wurde wird durch die anzahl an durchloopen die Basis immer wieder mit sich multipliziert wird
        ergebnis = ergebnis * basis
    return ergebnis
print("Schreibe zwei Zahlen, ")

# gibt der Funktion Information, für die Parameter
print(exponent_function(float(input("Gib die Basis an: ")),
                          int(input("Gib den Exponenten an: "))))
