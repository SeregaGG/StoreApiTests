import requests


class RegisterResponse:
    def __init__(self, response: requests.Response):
        self._message = response.json().get('message')
        self._uuid = response.json().get('uuid')
        self._status_code = response.status_code

    @property
    def message(self):
        return self._message

    @property
    def uuid(self):
        return self._uuid

    @property
    def status_code(self):
        return self._status_code
