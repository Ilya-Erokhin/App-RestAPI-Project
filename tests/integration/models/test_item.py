from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):

    def test_crud(self):

        with self.app_context():

            StoreModel('MyStore').save_to_db()
            item = ItemModel('MyItem', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('MyItem'),
                              f"Found an item with name {item.name}, but expected not to.")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('MyItem'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('MyItem'))

    def test_store_relationship(self):

        with self.app_context():

            store = StoreModel('TestStore')
            item = ItemModel('UrItem', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'TestStore')