import json

from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/store/MyStore')

                self.assertEqual(resp.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('MyStore'))
                self.assertDictEqual({'name': 'MyStore', 'items': []},
                                     json.loads(resp.data))


    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():

                client.post('/store/SAS')
                resp = client.post('/store/SAS')

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': 'A store with name \'SAS\' already exists.'},
                                     json.loads(resp.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():

                StoreModel('YerevanCity').save_to_db()
                resp = client.delete('/store/YerevanCity')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(resp.data))
                self.assertIsNone(StoreModel.find_by_name('YerevanCity'))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():

                StoreModel('Parma').save_to_db()
                resp = client.get('/store/Parma')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'name': 'Parma', 'items': []},
                                     json.loads(resp.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():

                resp = client.get('/store/YerevanCity')

                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(resp.data))
                self.assertIsNone(StoreModel.find_by_name('YerevanCity'))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('SevenEleven').save_to_db()
                ItemModel('Bag', 41.86, 1).save_to_db()

                resp = client.get('/store/SevenEleven')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'name': 'SevenEleven', 'items': [{'name': 'Bag', 'price': 41.86}]},
                                     json.loads(resp.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Costco').save_to_db()

                resp = client.get('/stores')

                self.assertDictEqual({'stores': [{'name': 'Costco', 'items': []}]},
                                     json.loads(resp.data))

    def test_store_list_with_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Walmart').save_to_db()
                ItemModel('Pillow', 4.05, 1).save_to_db()

                resp = client.get('/stores')

                self.assertDictEqual({'stores': [{'name': 'Walmart', 'items': [{'name': 'Pillow', 'price': 4.05}]}]},
                                     json.loads(resp.data))