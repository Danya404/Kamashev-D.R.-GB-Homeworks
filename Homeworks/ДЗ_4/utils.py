import requests
from decimal import *
from datetime import datetime

getcontext().prec = 4


def currency_rates(val):
    val = val.upper()
    responce = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in responce:
        return None
    rub = responce[responce.find('<Value>', responce.find(val)) + 7:responce.find('</Value>', responce.find(val))]
    actual_date = responce[responce.find('Date="') + 6:responce.find('"', responce.find('Date="') + 6)].split('.')
    day, month, year = map(int, actual_date)
    return f'{Decimal(rub.replace(",", "."))}, {datetime(day=day, month=month, year=year)}'


if __name__ == '__main__':
    import sys

    print(currency_rates(sys.argv[1]))
