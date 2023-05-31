
# Die Variablen für die If Statements werden mit Individuellen Informationen versehen 
zu_ersetzender_Buchstabe = input("Nenne Buchstaben der ausgetsuscht werden sollen: ")
erstzender_Großbuchstabe = input("Nenne Großbuchstaben die eingesetzt werden sollen: ")
erstzender_Buchstabe = input("Nenne Buchstaben die eingesetzt werden sollen: ")

# Parameter der Funktion ist die Variable auf der alles aufbaut
def übersetze(satz):

    # Platzhalter für die letztendliche Übersetztung
    übersetzung = ""

    # Variable "Buchstabe" wird durch for-loop hinugefügt die für das if Statement wichtig ist
    for buchstabe in satz:

        # wird bestimmt, dass kleine Buchstaben im selber gesetzten Wort, in den selber genannten Buchstaben vorkommen
        if buchstabe.lower() in zu_ersetzender_Buchstabe:
            
            # besagt, dass wenn diese Buchstaben im Wort groß geschreiben sind, dass diese dann durch die selber gesetzten Großbuchstaben ersetzt werden sollen
            if buchstabe.isupper():
                übersetzung = übersetzung + erstzender_Großbuchstabe

            # wenn diese Buchstaben im selber gesetzten Wort nicht in großgeschreibener Form vorkommen, werden die durch kleingeschreibene Buchstaben erstezt 
            else: 
                übersetzung = übersetzung + erstzender_Buchstabe

        # wird bestimmt, dass große Buchstaben im selber gesetzten Wort, in den selber genannten Buchstaben vorkommen
        elif buchstabe.upper() in zu_ersetzender_Buchstabe:
            
            # besagt, dass wenn diese Buchstaben im Wort klein geschreiben sind, dass diese dann durch die selber gesetzten kleingeschriebenen Buchstaben ersetzt werden soll
            if buchstabe.islower():
                übersetzung = übersetzung + erstzender_Buchstabe
            
            # wenn diese Buchstaben im selber gesetzten Wort nicht in kleingeschreibener Form vorkommen, werden die durch großgeschreibene Buchstaben erstezt
            else:
                übersetzung = übersetzung + erstzender_Großbuchstabe

        # wenn keiner dieser Fälle auftreten, so wird das selber gesetzte Wort unverändert gelassen 
        else:
            übersetzung = übersetzung + buchstabe
    
    # Ergebnis 
    return übersetzung

# Info die zu übersetzen/verändern ist 
print(übersetze(input("Schreibe ein Wort/Satz: ")))
