from tests.unit.unit_base_test import UnitBaseTest

from models.item import ItemModel


class ItemTest(UnitBaseTest):
# Tests for __init__ and json() methods - In ItemModel class
    def test_create_item(self):
        item = ItemModel('MyItem', 19.99, 1)

        self.assertEqual(item.name, 'MyItem',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)


def test_item_json(self):
        item = ItemModel('HisItem', 19.99, 1)

        expected = {
            'name': 'HisItem',
            'price': 19.99
        }

        self.assertEqual(item.json(), expected,
                         f"The JSON export of the item is incorrect. Received {item.json()}, expected {expected}.")