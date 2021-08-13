import requests
import json
from config import money, YOUR_APP_ID




class APIException(Exception):
    pass

class Convert:
    @staticmethod
    def get_price(quote, base, amount):

        r = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={YOUR_APP_ID}')
        dict_cur = json.loads(r.content)['rates']

        if quote not in money.keys() and quote not in dict_cur.keys():
            raise APIException(f'{quote} - эта валюта недоступна к сравнению')
        elif base not in money.keys() and base not in dict_cur.keys():
            raise APIException(f'{base} - эта валюта недоступна к сравнению')
        try:
            amount = float(amount)
        except:
            raise APIException(f'Количество "{amount}" указано не верно')

        if quote and base in money.keys():
            try:
                convers =(amount/float((dict_cur[money[quote]]))) * float(dict_cur[money[base]])
            except KeyError:
                raise APIException('Введите валюту в одном формате')

        elif quote and base in dict_cur.keys():
            try:
                convers =(amount/float(dict_cur[quote])) * float(dict_cur[base])
            except KeyError:
                raise APIException('Введите валюту в одном формате')
        if convers > 0.1:
            convers = round(convers,2)
        return convers

cur = requests.get('https://openexchangerates.org/api/currencies.json')
list_of_cur = json.loads(cur.content)