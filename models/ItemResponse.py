import requests
from config.status_codes import StatusCodes


class ItemResponse:
    def __init__(self, response: requests.Response = None, **kwargs):
        if response is None:
            self._name = kwargs.get('name')
            self._price = kwargs.get('price')
            self._item_id = kwargs.get('itemID')
            self._description = kwargs.get('description')
            self._image = kwargs.get('image')
            self._status_code = StatusCodes.CREATED
        else:
            self._name = response.json().get('name')
            self._price = response.json().get('price')
            self._item_id = response.json().get('itemID')
            self._description = response.json().get('description')
            self._image = response.json().get('image') or kwargs.get('image')
            self._status_code = response.status_code

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def item_id(self):
        return self._item_id

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

    @property
    def status_code(self):
        return self._status_code
