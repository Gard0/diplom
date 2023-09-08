import requests

from configuration import URL_SERVICE, CREATE_ORDER_PATH, GET_ORDER_INFO
from data import request_body


# Создание нового заказ:
def post_new_order():
    return requests.post(URL_SERVICE + CREATE_ORDER_PATH,
                         json=request_body)


# Получение информацию о заказе по трек-номеру:
def get_order_info(track):
    return requests.get(URL_SERVICE + GET_ORDER_INFO,
                        params={"t": track})
