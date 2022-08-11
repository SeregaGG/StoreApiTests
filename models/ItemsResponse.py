import requests
from models.ItemResponse import ItemResponse


class ItemsResponse:
    def __init__(self, response: requests.Response):
        self._items_list = [ItemResponse(**x) for x in response.json().get('items')]
        self._status_code = response.status_code

    @property
    def items_list(self):
        return self._items_list

    @property
    def status_code(self):
        return self._status_code
