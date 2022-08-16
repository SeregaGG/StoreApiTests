import requests
from config.status_codes import StatusCodes


class Item:
    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._price = kwargs.get('price')
        self._item_id = kwargs.get('itemID')
        self._store_id = kwargs.get('store_id')
        self._description = kwargs.get('description')
        self._image = kwargs.get('image')
        self._status_code = kwargs.get('status_code')

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
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def as_dict(self):
        body = {
            'price': self._price,
            'store_id': self._store_id,
            'description': self._description,
            'image': self._image
        }
        return body

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            is_eq = self._name == other.name and self._price == other.price \
                    and self._description == other.description and self._image == other.image
            return is_eq
        else:
            return False

