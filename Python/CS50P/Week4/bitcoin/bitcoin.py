import requests
import json
import sys


def main():
    while True:
        try:
            if len(sys.argv) == 1:
                sys.exit("Missing command-line argument")
            else:
                print(calculate())
                break
        except ValueError:
            sys.exit("Command-line argument is not a number")

def calculate():
    try:
        number = float(sys.argv[1])
        data_base = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = data_base.json()
        price = data["bpi"]["USD"]["rate_float"]
        amount = price*number
        return f"${amount:,.4f}"
    except requests.RequestException:
        sys.exit("Error")

if __name__ == "__main__":
    main()
