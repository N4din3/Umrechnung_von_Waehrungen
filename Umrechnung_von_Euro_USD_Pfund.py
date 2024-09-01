#INFO
# requests-Bibliothek muss installiert sein und Internetverbindung vorhanden
# (in Thonny-> Tool-> Manage packages -> nach requests suchen -> Bibliothek installieren)

# while-Schleife
eingabeJaNein = 1
while eingabeJaNein == 1:
    import requests
        
    def get_exchange_rate(base_currency,target_currency):
            
        # URL einer API, die den aktuellen Kurs liefert
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
            #"https://api.exchangerate-api.com/v4/latest/EUR"

        # HTTP GET-Anfrage senden
        response = requests.get(url)

        # Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200)
        if response.status_code == 200:
            # JSON-Daten in ein Python-Dictionary umwandeln
            data = response.json()

            # Den Kurs EUR zu USD extrahieren
            return data['rates'].get(target_currency)                
        else:
            print(f"Fehler beim Abrufen der Daten für {base_currency} zu {target_currency}.")
            return None
    # Auswahl der verfügbaren Währung   
    wahl = input("Welche Währung steht dir zur verfügung? EUR, USD oder GBP: ")
    # Verfügbare währung
    if wahl == "EUR" or "eur":
        # Nutzung der Funktion für verschiedene Währungen
        kurs_eur_usd = get_exchange_rate("EUR", "USD")
        kurs_eur_gbp = get_exchange_rate("EUR", "GBP")
        #Ausgabe des Kurses
        print(f"Der aktuelle Wechselkurs von EUR zu USD beträgt: {kurs_eur_usd}")
        print(f"Der aktuelle Wechselkurs von EUR zu GBP beträgt: {kurs_eur_gbp}")
        # Eingabe und Berechnung des Werts
        inputEUR = float(input("Gib den Wert in Euro an: "))
        outputUSD = inputEUR * kurs_eur_usd
        print(inputEUR,"Euro sind",outputUSD,"USD")
        outputGBP = inputEUR * kurs_eur_gbp
        print(inputEUR,"Euro sind",outputGBP,"Pfund")
    # Auswahl verfügbare Währung
    elif wahl == "USD" or "usd":
        # Nutzung der Funktion für verschiedene Währungen
        kurs_eur_usd = get_exchange_rate("EUR", "USD")
        kurs_usd_gbp = get_exchange_rate("USD", "GBP")
        #Ausgabe des Kurses
        print(f"Der aktuelle Wechselkurs von EUR zu USD beträgt: {kurs_eur_usd}")
        print(f"Der aktuelle Wechselkurs von USD zu GBP beträgt: {kurs_usd_gbp}")  
        # Eingabe und Berechnung des Werts
        inputUSD = float(input("Gib den Wert in USD an: "))
        outputEUR = inputUSD / kurs_eur_usd
        print(inputUSD,"Euro sind",outputEUR,"USD")
        outputGBP = inputEUR * kurs_usd_gbp
        print(inputUSD,"Euro sind",outputGBP,"Pfund")
    #Auswah der verfügabren Währung
    elif wahl == "GBP" or "gbp":
        # Nutzung der Funktion für verschiedene Währungen
        kurs_eur_gbp = get_exchange_rate("EUR", "GBP")
        kurs_usd_gbp = get_exchange_rate("USD", "GBP")
        #Ausgabe des Kurses
        print(f"Der aktuelle Wechselkurs von EUR zu GBP beträgt: {kurs_eur_gbp}")
        print(f"Der aktuelle Wechselkurs von USD zu GBP beträgt: {kurs_usd_gbp}")  
        # Eingabe und Berechnung des Werts
        inputGBP = float(input("Gib den Wert in Pfund an: "))
        outputEUR = inputGBP / kurs_eur_gbp
        print(inputGBP,"GBP sind",outputEUR,"Euro")
        outputUSD = inputGBP / kurs_usd_gbp
        print(inputGBP,"GBP sind",outputGBP,"USD")    

# Sprung zum Anfang (while-Schleife)
    neueEingabe = input("Willst du eine neue Umrechnung machen? Ja oder Nein? ")
    if neueEingabe == "Ja":
        eingabeJaNein = 1
    elif neueEingabe == "Nein":
        eingabeJaNein = 0