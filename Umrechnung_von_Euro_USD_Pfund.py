#INFO
# requests-Bibliothek muss installiert sein und Internetverbindung vorhanden
# (in Thonny-> Tool-> Manage packages -> nach requests suchen -> Bibliothek installieren)

import requests

# Funktion, um die Wechselkurse von einer bestimmten Basiswährung zu bekommen
def get_exchange_rates(base_currency):
    # URL der API mit der Basiswährung
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    # HTTP GET-Anfrage senden
    response = requests.get(url)
    
    # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
    if response.status_code == 200:
        # JSON-Daten in ein Python-Dictionary umwandeln
        data = response.json()
        return data['rates']
    else:
        print(f"Fehler beim Abrufen der Daten für {base_currency}.")
        return None

# Benutzerwährung auswählen
def waehrung_auswahl():
    print("Verfügbare Währungen zum umrechnen: EUR, USD, GBP")
    wahl = input("Welche Währung hast du? (EUR, USD, GBP): ").upper()
    
    if wahl not in ['EUR', 'USD', 'GBP']:
        print("Ungültige Währung. Bitte wähle EUR, USD oder GBP.")
        return None
    
    return wahl

# Umrechnungsfunktion
def waehrung_umrechnen(base_currency):
    # Wechselkurse abrufen
    rates = get_exchange_rates(base_currency)
    
    if rates:
        # Auswahl der Zielwährung
        target_currency = input(f"In welche Währung möchtest du {base_currency} umrechnen? (USD, EUR, GBP): ").upper()
        
        if target_currency not in rates:
            print(f"Ungültige Zielwährung. Verfügbare Währungen: {list(rates.keys())}")
            return
        
        # Eingabe des Betrags
        betrag = float(input(f"Gib den Betrag in {base_currency} ein: "))
        
        # Umrechnung durchführen
        umgerechnet = betrag * rates[target_currency]
        
        # Ergebnis anzeigen
        print(f"{betrag} {base_currency} sind {umgerechnet:.2f} {target_currency}.")
    else:
        print("Fehler beim Abrufen der Wechselkurse.")

# Hauptschleife zur Auswahl und Umrechnung
while True:
    base_currency = waehrung_auswahl()
    
    if base_currency:
        waehrung_umrechnen(base_currency)
    
    # Möchte der Benutzer eine weitere Umrechnung vornehmen?
    erneut = input("Möchtest du eine weitere Umrechnung machen? (Ja/Nein): ").lower()
    if erneut != "ja":
        print("Programm beendet.")
        break