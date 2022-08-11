import random

import pytest
from connector.Connector import Connector
from models.Register import Register
from models.Auth import Auth
from faker import Faker


@pytest.fixture(scope='class', params=[('https://stores-tests-api.herokuapp.com',)])
def connection(request):
    base_url = request.param[0]
    connection = Connector(base_url)
    return connection


@pytest.fixture(scope='class')
def connection_auth(connection: Connector):
    fake: Faker = Faker()
    random_data = (fake.name(), fake.password())
    user_data = Register(*random_data)
    connection.user_reg(user_data)
    access_token: Auth = connection.user_auth(user_data)
    return access_token


@pytest.fixture(scope='class')
def random_store_name():
    fake: Faker = Faker()
    return fake.company()


@pytest.fixture(scope='class')
def random_item_data():
    fake: Faker = Faker()
    item_data = {
        'name': ''.join(fake.random_letters(length=10)),
        'price': random.randint(1, 10000),
        'store_id': 1,
        'description': ''.join(fake.random_letters(length=10)),
        'image': ''.join(fake.random_letters(length=10))
    }
    return item_data
