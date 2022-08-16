import requests


class Auth:
    def __init__(self, response: requests.Response):
        self._access_token = response.json().get('access_token')
        self._status_code = response.status_code

    @property
    def access_token(self):
        return self._access_token

    @property
    def status_code(self):
        return self._status_code
