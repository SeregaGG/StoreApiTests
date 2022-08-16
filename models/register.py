class Register:
    def __init__(self, **kwargs):
        self._name = kwargs.get('name')
        self._password = kwargs.get('password')
        self._message = kwargs.get('message')
        self._uuid = kwargs.get('uuid')
        self._status_code = kwargs.get('status_code')

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

    @property
    def message(self):
        return self._message

    @property
    def uuid(self):
        return self._uuid

    @property
    def status_code(self):
        return self._status_code
