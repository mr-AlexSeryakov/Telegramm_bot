"""
Модуль extensions.py

CryptoConverter - Предназначен для конвертации одной валюты в другую с использованием внешнего API

Класс имеет статический метод convert, который принемает коды двух валют и количество,
обращается к внешнему API CryptoCompare и возвращает стоимость указанной валюты.

Методы:
    convert (quote, base, amount): Конвертация указанной валюты и обработкой ошибок

Исключения:
    ConvertionException - выбрасывается при ошибках в обработке данных или невозможности конвертации
"""


import requests
import json
from conf import keys

 
class ConvertionException(Exception):
    pass

class CryptoConverter:
    """Класс для конвертации валюты с использованием внешнего API"""
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        """Конвертация валюты 
        принемает количество 'amount' валюты 'quote' в валюту 'base'

        Args:
            quote (str): Код исходной валюты
            base (str): Код валюты, в которую конвертируем
            amount (str): Количество валюты для ковертации

        Returns:
            float: Возвращает курс в валюте base 

        Raises:
            ConvertionException: Выбрасывается если валюты одинаковы, 
            или код валюты не найден,
            или если amout нельзя привести к числу
        """
        if quote == base:
            raise ConvertionException(f'Невозможно перевести динаковые валюты {base}.')
    
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
    
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
    
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}&tryConversion=true')
        total_base = json.loads(r.content)[keys[base]]

        return total_base