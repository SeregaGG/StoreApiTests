import requests


class StoreResponse:
    def __init__(self, response: requests.Response):
        self._name = response.json().get('name')
        self._uuid = response.json().get('uuid')
        self._items = response.json().get('items')
        self._status_code = response.status_code

    @property
    def name(self):
        return self._name

    @property
    def uuid(self):
        return self._uuid

    @property
    def items(self):
        return self._items

    @property
    def status_code(self):
        return self._status_code
