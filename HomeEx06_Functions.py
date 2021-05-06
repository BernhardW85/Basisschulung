
def DecPrefix(unit):  # Wird das erste Zeichen aus einer Liste an Buchstaben erkannt, so wird ein Multiplikator zurückgegeben
    lstPrefix = {"k": 10 ** 3, "M": 10 ** 6, "G": 10 ** 9, "T": 10 ** 12, "P": 10 ** 15, "E": 10 ** 18, "m": 10 ** -3,
                 "n": 10 ** -6}
    fltDecFactor = lstPrefix.get(unit[0])  # Funktion "get" gibt bei Nichtauffindung ein "None" zurück
    if fltDecFactor is None:  # wenn kein Präfix gefunden wird, dann ist der Multiplikator 1
        fltDecFactor = 1
    return fltDecFactor


def RawUnit(unit, prefix):  # Solange es ein Präfix gibt, wird die Einheit um den Präfix bereinigt.
    if prefix != 1:  # Wenn ein Präfix vorhanden ist, wird dieser für die nächste Operation entfernt.
        unit = unit[1:]
    return unit


def Convert2SIUnit(unit):  # Wählt aus einer Einheitenliste den entsprechende
    bolUnitNotFound = False
    lstUnits = {"BTU": 0.0009, "cal": 1 / 4.1868, "J": 1, "gSKE": 1 / 29308, "toe": 1 / 41868000000, "goe": 1 / 41868,
                "Wh": 1 / 3600}
    fltUnitFactor = lstUnits.get(unit)
    if fltUnitFactor is None:
        bolUnitNotFound = True
    return bolUnitNotFound, fltUnitFactor
