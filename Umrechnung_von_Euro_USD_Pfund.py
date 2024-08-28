#INFO
# requests-Bibliothek muss installiert sein und Internetverbindung vorhanden
# (in Thonny-> Tool-> Manage packages -> nach requests suchen -> Bibliothek installieren)

# while-Schleife
eingabeJaNein = 1
while eingabeJaNein == 1:
    
    wahl = input("Welche Währung soll umgerechnet werden? EUR, USD oder GBP: ")
    if wahl == "EUR":
        import requests

# URL einer API, die den aktuellen Kurs EUR zu USD liefert
        url = "https://api.exchangerate-api.com/v4/latest/EUR"

# HTTP GET-Anfrage senden
        response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
# JSON-Daten in ein Python-Dictionary umwandeln
            data = response.json()

# Den Kurs EUR zu USD extrahieren
            kurs_eur_usd = data['rates']['USD']

            print(f"Der aktuelle Wechselkurs von EUR zu USD beträgt: {kurs_eur_usd}")
        else:
            print("Fehler beim Abrufen der Daten.")


        import requests

# URL einer API, die den aktuellen Kurs EUR zu GBP liefert
        url = "https://api.exchangerate-api.com/v4/latest/EUR"

# HTTP GET-Anfrage senden
        response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
# JSON-Daten in ein Python-Dictionary umwandeln
            data = response.json()

# Den Kurs EUR zu USD extrahieren
            kurs_eur_gbp = data['rates']['GBP']

            print(f"Der aktuelle Wechselkurs von EUR zu GPB beträgt: {kurs_eur_gbp}")
        else:
            print("Fehler beim Abrufen der Daten.")

    inputEUR = float(input("Gib den Wert in Euro an: "))
    outputUSD = inputEUR * kurs_eur_usd
    print(inputEUR,"Euro sind",outputUSD,"USD")
    outputGBP = inputEUR * kurs_eur_gbp
    print(inputEUR,"Euro sind",outputGBP,"Pfund")

# Sprung zum Anfang (while-Schleife)
    neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
    if neueEingabe == "Ja":
        eingabeJaNein = 1
    elif neueEingabe == "Nein":
        eingabeJaNein = 0