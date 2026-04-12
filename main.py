import requests
import os
import argparse
from dotenv import load_dotenv


def exchange_rate(exc,api_key):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{exc}"
        response = requests.get(url)
        response.raise_for_status()
    except:
        print("Вы ввели не существующий курс валют, попробуйте снова!")
        os._exit(0)
    return response.json()["conversion_rates"]


def convert_amount(exchange_rates,target_currency,amount):
    target_rate = exchange_rates[target_currency]
    print(f"курс целевой валюты: {target_rate}")
    return amount*target_rate


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")

    parser = argparse.ArgumentParser(description="Данная программа конвертирует валюты, сначала вводим наш курс валюты, следующий тот курс в который мы хотим перевести, и потом кол-во денежных средств которое нужно перевести")

    parser.add_argument("-b", "--base", help="RUB",type=str)
    parser.add_argument("-t", "--target", help="EUR",type=str)
    parser.add_argument("-a", "--amount", help="10000",type=float)
    args = parser.parse_args()

    exchange_rates = exchange_rate((args.base).upper(), api_key)

    print(f"Конвертированная сумма: {convert_amount(exchange_rates,(args.target).upper(),args.amount)} {(args.target).upper()}")


if __name__ == "__main__":
    main()