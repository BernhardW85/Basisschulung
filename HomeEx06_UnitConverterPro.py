# Bibliotheken- und Funktionen-Import
from HomeEx06_Functions import DecPrefix  # Funktion Erkennung und Umwandlung der Dezimalpräfixe in Multiplikatoren
from HomeEx06_Functions import RawUnit  # Funktion Entfernung des Dezimalpräfix
from HomeEx06_Functions import Convert2SIUnit  # Funktion Einheit in Multiplikator umwandeln
import json

print("Willkommen beim Energieeinheiten-Umwandler!")
print("Zwischen den folgenden Einheiten kann umgerechnet werden: J | Wh | toe | cal | gSKE | BTU")

with open("HomeEx06_LogFile.txt", "r") as fileLog:
    listLog = json.loads(fileLog.read())

strWeiter = "j"
while strWeiter == "j":  # Solange durchspielen, bis nicht mehr "j" eingegeben wird
    # Eingabe durch BenutzerInnen
    fltZahl01 = input("Bitte gib die umzuwandelnde Zahl ein: ")
    strEinheit01 = input("Bitte gib die Energieeinheit zu dieser Zahl an: ")
    strEinheit02 = input("Bitte gib die Ziel-Energieeinheit an: ")

    # Identifikation der Präfix-Multiplikatoren
    fltDecPrefix = DecPrefix(strEinheit01), DecPrefix(strEinheit02)

    # Umwandlung in Einheiten ohne Präfixe
    strRohEinheit = RawUnit(strEinheit01, fltDecPrefix[0]), RawUnit(strEinheit02, fltDecPrefix[1])

    # Einheitenumwandlung in Faktoren
    bolUnitFactor = Convert2SIUnit(strRohEinheit[0])[0], Convert2SIUnit(strRohEinheit[1])[0]
    fltUnitFactor = Convert2SIUnit(strRohEinheit[0])[1], Convert2SIUnit(strRohEinheit[1])[1]

    # Wenn Einheit nicht vorhanden ist, dann Rückmeldung geben, andernfalls Ergebnis ausgeben und in Log-Date spielen
    if bolUnitFactor[0] is True or fltUnitFactor[1] is True:
        print("Die angegebene Einheit konnte nicht identifiziert werden! Bitte versuche es nochmal.")
    else:
        fltErgebnis = float(fltZahl01) * fltDecPrefix[0] / fltDecPrefix[1] / fltUnitFactor[0] * fltUnitFactor[1]
        print(f"{fltZahl01} {strEinheit01} = {fltErgebnis} {strEinheit02}")

        # Ergebnis in das Dictionary eintragen
        listLog.append({"Wert": fltZahl01, "Start-Einheit": strEinheit01, "Ergebnis": fltErgebnis, "Ziel-Einheit": strEinheit02, "SI-Einheiten": strRohEinheit})

        # Dictionary in die Log-Datei überspielen
        with open("HomeEx06_LogFile.txt", "w") as fileLog:
            fileLog.write(json.dumps(listLog))

    strWeiter = input("Noch eine Umrechnung gefällig? (j/n): ")
