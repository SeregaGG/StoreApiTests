import pytest

from models.auth import Auth
from connector.connector import Connector
from models.store import Store
from config.status_codes import StatusCodes
from models.item import Item


@pytest.mark.usefixtures('connection_auth', 'connection', 'random_store_name')
class TestStore:
    def test_add_new_store(self, connection_auth: Auth, connection: Connector, random_store_name):
        new_store: Store = connection.add_new_store(random_store_name, connection_auth.access_token)
        assert new_store.name == random_store_name
        assert new_store.status_code == StatusCodes.CREATED

    def test_get_store(self, connection_auth: Auth, connection: Connector, random_store_name):
        store: Store = connection.get_store(random_store_name, connection_auth.access_token)
        assert store.name == random_store_name
        assert store.status_code == StatusCodes.OK


@pytest.mark.usefixtures('connection_auth', 'connection', 'random_item_data')
class TestItem:
    def test_add_new_item(self, connection_auth: Auth, connection: Connector, random_item_data):
        new_item: Item = Item(**random_item_data)
        created_item: Item = connection.add_new_item(new_item, connection_auth.access_token)
        assert created_item == new_item
        assert created_item.status_code == StatusCodes.CREATED

    def test_get_item(self, connection_auth: Auth, connection: Connector, random_item_data):
        item: Item = connection.get_item(random_item_data.get('name'), connection_auth.access_token)
        assert item.name == random_item_data.get('name')
        assert item.status_code == StatusCodes.OK

    def test_get_items(self, connection_auth: Auth, connection: Connector, random_item_data):
        items, status_code = connection.get_items(connection_auth.access_token)
        items_names = [x.name for x in items]
        assert status_code == StatusCodes.OK
        assert random_item_data.get('name') in items_names
