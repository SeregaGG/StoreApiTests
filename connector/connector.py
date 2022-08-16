import requests
from models.register import Register
from models.auth import Auth
from models.store import Store
from models.item import Item
from jsonschema import validate
from schemas.register_response import valid_schema as reg_schema
from schemas.auth import valid_schema as auth_schema


class Connector:

    AUTH_ROUTE = '/auth'
    REGISTER_ROUTE = '/register'
    STORE = '/store'
    ITEM = '/item'
    ITEMS = '/items'

    def __init__(self, base_url):
        self._base_url = base_url

    def user_reg(self, user_data: Register) -> Register:
        url = f'{self._base_url}{self.__class__.REGISTER_ROUTE}'
        response = requests.post(url, json=user_data.as_dict())
        validate(instance=response.json(), schema=reg_schema)
        register_response = Register(**response.json())
        return register_response

    def user_auth(self, user_data: Register) -> Auth:
        url = f'{self._base_url}{self.__class__.AUTH_ROUTE}'
        response = requests.post(url, json=user_data.as_dict())
        validate(instance=response.json(), schema=auth_schema)
        auth_response = Auth(response)
        return auth_response

    def add_new_store(self, store_name, jwt) -> Store:
        url = f'{self._base_url}{self.__class__.STORE}/{store_name}'
        response = requests.post(url, headers={'Authorization': f'JWT {jwt}'})
        new_store = Store(response)
        return new_store

    def get_store(self, store_name, jwt) -> Store:
        url = f'{self._base_url}{self.__class__.STORE}/{store_name}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        new_store = Store(response)
        return new_store

    def add_new_item(self, item: Item, jwt) -> Item:
        url = f'{self._base_url}{self.__class__.ITEM}/{item.name}'
        response = requests.post(url, json=item.as_dict(), headers={'Authorization': f'JWT {jwt}'})
        new_item = Item(**response.json(), status_code=response.status_code)
        return new_item

    def get_item(self, item_name, jwt):
        url = f'{self._base_url}{self.__class__.ITEM}/{item_name}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        item_resp = Item(**response.json(), status_code=response.status_code)
        return item_resp

    def get_items(self, jwt):
        url = f'{self._base_url}{self.__class__.ITEMS}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        items_list = [Item(**x) for x in response.json().get('items')]
        return items_list, response.status_code
