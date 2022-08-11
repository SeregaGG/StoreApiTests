class Register:
    def __init__(self, name, password):
        self._name = name
        self._password = password

    def as_dict(self):
        body = {
            'username': self._name,
            'password': self._password
        }
        return body

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password
