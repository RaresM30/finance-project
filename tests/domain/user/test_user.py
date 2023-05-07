import unittest
import uuid

from domain.asset.asset import Asset
from domain.user.user import User


class TestsForUser(unittest.TestCase):
    def test_user_sets_the_right_username(self):
        # setup
        id_ = uuid.uuid4()
        username = "random.generated"
        user = User(id_, username)
        # execution
        actual_username = user.username
        # assertion
        self.assertEqual(username, actual_username)

    def test_it_sets_empty_list_if_we_do_not_specify_stocks(self):
        id_ = uuid.uuid4()
        user = User(id_, "random-username")

        actual_stocks = user.stocks

        self.assertEqual([], actual_stocks)

    def test_it_sets_the_stocks_we_give(self):
        id_ = uuid.uuid4()
        username = "random-name"

        actual_asset = [
            Asset(country="United States", ticker="tsla", nr=0, name="Tesla", sector="Tech")
        ]

        user = User(id_, username, actual_asset)

        actual = user.stocks

        self.assertEqual(actual_asset, actual)

    def test_it_sets_the_id(self):
        id_ = uuid.uuid4()
        user = User(id_, "user-test")
        actual_id_for_user = user.id
        self.assertEqual(actual_id_for_user, id_)

if __name__ == "__main__":
    unittest.main()