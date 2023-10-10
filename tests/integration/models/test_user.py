from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel('MyUser', 'KhfA2ys4aj1A1')

            self.assertIsNone(UserModel.find_by_username('MyUser'))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('MyUser'))
            self.assertIsNotNone(UserModel.find_by_id(1))



