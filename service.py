import requests

from config import URL


def get_currency_converter_data(currency: str = 'RUB') -> str:
    params = {'currencies': currency, 'source': 'USD', 'format': 1}

    response = requests.get(URL, params=params)
    if not response.ok:
        return 'XX'

    data = response.json()
    return data.get('quotes', {}).get('USDRUB', 'XX')
