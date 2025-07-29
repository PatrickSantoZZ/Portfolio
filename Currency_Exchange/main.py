import requests
import os
from dotenv import load_dotenv


# URL von der Documentation => https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"

    try:
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['conversion_rates'][target_currency]

        if exchange_rate is None:
            raise ValueError(f"Zielwährung '{target_currency}' nicht gefunden.")

        return exchange_rate

    except:
        raise ValueError("Ungültige Basiswährung oder Zielwährung.")

def main():
    try:

        currency_amount = float(input("Bitte geben Sie die Betrag ein: "))
        base_currency = input("Bitte geben Sie die Basiswährung ein: ")
        target_currency = input("Bitte geben Sie die Zielwährung ein: ")

        exchange_rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = currency_amount * exchange_rate

        print(f"{currency_amount:.2f} {base_currency} entspricht {converted_amount} {target_currency}")
        print(f"Aktueller Wechselkurs: 1 {base_currency} entspricht {exchange_rate} {target_currency}")
    
    except ValueError as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()