import requests
from config.routes import StoreRoutes
from models.Register import Register
from models.RegisterResponse import RegisterResponse
from models.Auth import Auth
from models.StoreResponse import StoreResponse
from models.Item import Item
from models.ItemResponse import ItemResponse
from models.ItemsResponse import ItemsResponse
from jsonschema import validate
from schemas.register_response import valid_schema as reg_schema
from schemas.auth import valid_schema as auth_schema


class Connector:

    def __init__(self, base_url):
        self._base_url = base_url

    def user_reg(self, user_data: Register) -> RegisterResponse:
        url = f'{self._base_url}{StoreRoutes.REGISTER_ROUTE}'
        response = requests.post(url, json=user_data.as_dict())
        validate(instance=response.json(), schema=reg_schema)
        register_response = RegisterResponse(response)
        return register_response

    def user_auth(self, user_data: Register) -> Auth:
        url = f'{self._base_url}{StoreRoutes.AUTH_ROUTE}'
        response = requests.post(url, json=user_data.as_dict())
        validate(instance=response.json(), schema=auth_schema)
        auth_response = Auth(response)
        return auth_response

    def add_new_store(self, store_name, jwt) -> StoreResponse:
        url = f'{self._base_url}{StoreRoutes.STORE}/{store_name}'
        response = requests.post(url, headers={'Authorization': f'JWT {jwt}'})
        new_store = StoreResponse(response)
        return new_store

    def get_store(self, store_name, jwt) -> StoreResponse:
        url = f'{self._base_url}{StoreRoutes.STORE}/{store_name}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        new_store = StoreResponse(response)
        return new_store

    def add_new_item(self, item: Item, jwt) -> ItemResponse:
        url = f'{self._base_url}{StoreRoutes.ITEM}/{item.name}'
        response = requests.post(url, json=item.as_dict(), headers={'Authorization': f'JWT {jwt}'})
        new_item = ItemResponse(response)
        return new_item

    def get_item(self, item_name, jwt):
        url = f'{self._base_url}{StoreRoutes.ITEM}/{item_name}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        item_resp = ItemResponse(response)
        return item_resp

    def get_items(self, jwt):
        url = f'{self._base_url}{StoreRoutes.ITEMS}'
        response = requests.get(url, headers={'Authorization': f'JWT {jwt}'})
        items_list = ItemsResponse(response)
        return items_list
