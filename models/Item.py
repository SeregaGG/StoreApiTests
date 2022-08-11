import requests


class Item:
    def __init__(self, name, price, store_id, description, image):
        self._name = name
        self._price = price
        self._store_id = store_id
        self._description = description
        self._image = image

    def as_dict(self):
        body = {
            'price': self._price,
            'store_id': self._store_id,
            'description': self._description,
            'image': self._image
        }
        return body

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def store_id(self):
        return self._store_id

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image
