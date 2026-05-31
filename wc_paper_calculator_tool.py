print("Berechnungs-Tool zum Vergleich der WC-Papier-Kosten:")
# Dieses Tool wurde von mir selbst nach eigener Idee erstellt am 27.05.2026!#
##

def Packung_A():
    Anzahl_Rollen = float(input("Bitte hier die Anzahl der Rollen in der Verpackung eingeben: "))
    print(Anzahl_Rollen)
    Anzahl_Blatt = int(input("Bitte hier die Anzahl der Blätter pro Rolle eingeben: "))
    print(Anzahl_Blatt)
    Preis_gesamt = float(input("Bitte hier den Preis für die Verpackung eingeben im Format Euro.Cent (Bsp.: 3.50): "))
    print(Preis_gesamt)
    
    Anzahl_Blatt_gesamt = Anzahl_Rollen * Anzahl_Blatt

    Preis_pro_Blatt = Preis_gesamt / Anzahl_Blatt_gesamt

    print("Anzahl der WC-Blätter Packung A insgesamt: ")
    print(Anzahl_Blatt_gesamt)

    return Preis_pro_Blatt


def Packung_B():
    Anzahl_Rollen = float(input("Bitte hier die Anzahl der Rollen in der Verpackung eingeben: "))
    print(Anzahl_Rollen)
    Anzahl_Blatt = int(input("Bitte hier die Anzahl der Blätter pro Rolle eingeben: "))
    print(Anzahl_Blatt)
    Preis_gesamt = float(input("Bitte hier den Preis für die Verpackung eingeben im Format Euro.Cent (Bsp.: 3.50): "))
    print(Preis_gesamt)
    
    Anzahl_Blatt_gesamt = Anzahl_Rollen * Anzahl_Blatt

    Preis_pro_Blatt = Preis_gesamt / Anzahl_Blatt_gesamt

    print("Anzahl der WC-Blätter Packung B insgesamt: ")
    print(Anzahl_Blatt_gesamt)

    return Preis_pro_Blatt


Ergebnis_A = Packung_A()
Ergebnis_B = Packung_B()


print(f"Packung A kostet pro Blatt = {Ergebnis_A}.")
print(f"Packung B kostet pro Blatt = {Ergebnis_B}.")

print("Welche Verpackung ist nun insgesamt am günstigsten?")
##
def Fazit():
  if Ergebnis_A < Ergebnis_B:
    print("Fazit: Packung A ist günstiger!")
  else:
    print("Fazit: Packung B ist günstiger!")

Fazit()