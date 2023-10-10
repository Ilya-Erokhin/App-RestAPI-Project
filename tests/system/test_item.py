from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json

class ItemTest(BaseTest):

    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('Ilia', 'IliaPaSsWOrd101001').save_to_db()

                auth_resp = client.post('/auth',
                                        json=({'username': 'Ilia', 'password': 'IliaPaSsWOrd101001'}),
                                        headers={'Content-Type': 'application/json'})
                auth_token = json.loads(auth_resp.data)['access_token']

                self.access_token = f'JWT {auth_token}'

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():

                resp = client.get('/item/Pork')

                self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.app() as client:
            with self.app_context():

                resp = client.get('/item/Bread', headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Costco').save_to_db()
                ItemModel('Meet', 19.99, 1).save_to_db()

                resp = client.get('/item/Meet', headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 200)

    def test_delete_item(self):
        with self.app() as client:
            with self.app_context():

                StoreModel('SevenEleven').save_to_db()
                ItemModel('Chicken', 19.99, 1).save_to_db()

                resp = client.delete('/item/Chicken')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(resp.data))

    def test_create_item(self):
        with self.app() as client:
            with self.app_context():

                StoreModel('Walmart').save_to_db()

                resp = client.post('/item/Milk',
                                   json={'price': 3.89, 'store_id': 1},
                                   headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 201)
                self.assertDictEqual({'name': 'Milk', 'price': 3.89},
                                     json.loads(resp.data))

    def test_create_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Parma').save_to_db()
                ItemModel('Cheese', 17.99, 1).save_to_db()

                resp = client.post('/item/Cheese', data={'price': 23.52, 'store_id': 1})

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': 'An item with name \'Cheese\' already exists.'},
                                     json.loads(resp.data))

    def test_create_then_delete_duplicate_item(self):
        with self.app() as client:
            with self.app_context():
                store = StoreModel('OBI')
                item = ItemModel('Hammer', 5.89, 1)
                ItemModel('Pillow', 17.99, 1).save_to_db()

                store.save_to_db()
                item.save_to_db()

                resp = client.post('/item/Pillow',
                                   data={'price': 17.99, 'store_id': 1},
                                   headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': 'An item with name \'Pillow\' already exists.'},
                                     json.loads(resp.data))
                self.assertIsNotNone(ItemModel.find_by_name('Hammer'))

                resp = client.delete('/item/Pillow')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'message': 'Item deleted'},
                                     json.loads(resp.data))
                self.assertIsNotNone(ItemModel.find_by_name('Hammer'))
                self.assertEqual(store.items.count(), 1)

    def test_put_item(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Pyaterochka').save_to_db()

                resp = client.put('/item/Chocolate', json={'price': 1.99, 'store_id': 1},
                                  headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('Chocolate').price, 1.99)
                self.assertDictEqual({'name': 'Chocolate', 'price': 1.99},
                                     json.loads(resp.data))

    def test_put_update_item(self):
        with self.app() as client:
            with self.app_context():

                StoreModel('Costco').save_to_db()
                ItemModel('Bread', 5.99, 1).save_to_db()

                self.assertEqual(ItemModel.find_by_name('Bread').price, 5.99)

                resp = client.put('/item/Bread', json={'price': 6.50, 'store_id': 1},
                                  headers={'Authorization': self.access_token})

                self.assertEqual(resp.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('Bread').price, 6.50)
                self.assertDictEqual({'name': 'Bread', 'price': 6.50},
                                     json.loads(resp.data))

    def test_item_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('Walmart').save_to_db()
                ItemModel('Beef', 9.89, 1).save_to_db()

                resp = client.get('/items')

                self.assertDictEqual({'items': [{'name': 'Beef', 'price': 9.89}]},
                                     json.loads(resp.data))