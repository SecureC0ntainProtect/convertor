import json
import logging
import requests
from typing import Union

from config import currencies, CRYPTOCOMPARE_API_KEY
from exceptions import APIException


class Convert:
    @staticmethod
    def get_price(to: str, from_: str, amount: Union[int, str]) -> str:
        if not amount.isdigit():
            raise APIException('Неправильно введен запрос\nПодробно можно посмотреть /help')

        if to not in list(currencies.keys()) or from_ not in list(currencies.keys()):
            raise APIException('Введены недоступные валюты\nДоступные валюты /values')
        elif from_ == to:
            raise APIException(f'Нельзя конвертировать одинаковые валюты {from_} на {to}')
        elif int(amount) > 1:
            raise APIException('Нельзя получить курс больше единицы\nПодробно можно посмотреть /help')

        params = {
            'fsym': currencies[from_],
            'tsyms': currencies[to],
            'api_key': CRYPTOCOMPARE_API_KEY,
        }

        try:
            response = requests.get('https://min-api.cryptocompare.com/data/price', params=params)
            result = json.loads(response.content)
        except Exception as error:
            logging.warning(error)
            raise APIException(f'Сервер временно не доступен\nПопробуйте снова чуть позже\nИзвините за неудобства')
        else:
            return f'{amount} {from_} = {result[currencies[to]]} {to}'
