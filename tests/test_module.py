import pytest

from models.Auth import Auth
from connector.Connector import Connector
from models.StoreResponse import StoreResponse
from config.status_codes import StatusCodes
from models.Item import Item
from models.ItemResponse import ItemResponse
from models.ItemsResponse import ItemsResponse


@pytest.mark.usefixtures('connection_auth', 'connection', 'random_store_name')
class TestStore:
    def test_add_new_store(self, connection_auth: Auth, connection: Connector, random_store_name):
        new_store: StoreResponse = connection.add_new_store(random_store_name, connection_auth.access_token)
        assert new_store.name == random_store_name
        assert new_store.status_code == StatusCodes.CREATED

    def test_get_store(self, connection_auth: Auth, connection: Connector, random_store_name):
        store: StoreResponse = connection.get_store(random_store_name, connection_auth.access_token)
        assert store.name == random_store_name
        assert store.status_code == StatusCodes.OK


@pytest.mark.usefixtures('connection_auth', 'connection', 'random_item_data')
class TestItem:
    def test_add_new_item(self, connection_auth: Auth, connection: Connector, random_item_data):
        new_item_data: Item = Item(**random_item_data)
        new_item: ItemResponse = connection.add_new_item(new_item_data, connection_auth.access_token)
        assert new_item.name == new_item_data.name
        assert new_item.status_code == StatusCodes.CREATED

    def test_get_item(self, connection_auth: Auth, connection: Connector, random_item_data):
        item: ItemResponse = connection.get_item(random_item_data.get('name'), connection_auth.access_token)
        assert item.name == random_item_data.get('name')
        assert item.status_code == StatusCodes.OK

    def test_get_items(self, connection_auth: Auth, connection: Connector, random_item_data):
        items: ItemsResponse = connection.get_items(connection_auth.access_token)
        items_names = [x.name for x in items.items_list]
        assert items.status_code == StatusCodes.OK
        assert random_item_data.get('name') in items_names
