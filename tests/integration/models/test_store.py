from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertEqual(store.items.all(), [],
                         "The store's items length was not 0 even though no item were added.")

# Create, Read, Update, Delete
    def test_croud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'))

# What happens when you have an item? Does it appear?
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('MyItem', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'MyItem')

    def test_store_json_no_items(self):
        with self.app_context():
            store = StoreModel('MyStore')

            store.save_to_db()

            expected = {
                'name': 'MyStore',
                'items': []
            }

            self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('TestStore')
            item = ItemModel('TestItem', 72.39, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'TestStore',
                'items': [{'name': 'TestItem', 'price': 72.39}]
            }

            self.assertDictEqual(store.json(), expected)