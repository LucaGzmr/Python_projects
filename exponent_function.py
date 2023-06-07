
# Schleife, um permanent durch das Programm zu loopen, selbst wenn ein Fehler auftritt
while ValueError:
    # Parameter werden gesetzt
    def exponent_function (basis, exponent):
        ergebnis = 1
        # range gibt durtch den gesetztenm Exponenten an wie oft durch die for-loop geloopt werden soll 
        for index in range(exponent):
            # da ergenbis = 1 gesetzt wurde wird durch die Anzahl an durchloopen die Basis immer wieder mit sich selbst multipliziert wird
            ergebnis = ergebnis * basis
        return ergebnis
    
    print("\n")
    print("Schreibe zwei Zahlen, ")

    # prüft ob Fehler auftreten
    try:
        # gibt der Funktion Information, für die Parameter
        print(exponent_function(float(input("Gib die Basis an: ")),
                                int(input("Gib den Exponenten an: "))))

    # der Fehler der auftreten kann
    except ValueError as err1:
        print(err1)
