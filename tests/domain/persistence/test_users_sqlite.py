import sqlite3
import unittest

from domain.user.factory import UserFactory
from persistence.user_sqlite import UserPersistenceSqlite


class TestUserPersistenceSqlite(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.persistence = UserPersistenceSqlite()
        cls.factory = UserFactory()

    def test_add(self):
        user = self.factory.make_new("test-username")

        self.persistence.add(user)
        users = self.persistence.get_all()

        self.assertEqual(len(users), 1)

        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM users WHERE id = '{str(user.id)}'")
            conn.commit()

    def test_get_all(self):
        user1 = self.factory.make_new("test-username1")
        user2 = self.factory.make_new("test-username2")
        users_list = [user1, user2]
        for each_user in users_list:
            self.persistence.add(each_user)

        actual_users = self.persistence.get_all()

        self.assertEqual(len(actual_users), 2)

        with sqlite3.connect("main_users.db") as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM users WHERE id='{str(user1.id)}'")
            cursor.execute(f"DELETE FROM users WHERE id='{str(user2.id)}'")


if __name__ == '__main__':
    unittest.main()
