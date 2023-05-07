import unittest
import uuid

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User
from uuid import UUID




class UnitFactoryTestCase(unittest.TestCase):
    def test_it_creates_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-and-20-"
        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_below_6(self):
        username = "below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have at least 6 chars", str(context.exception)
        )

    def test_it_raises_exception_if_the_username_is_above_20_chars(self):
        username = "u" * 21
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have a maximum of 20 chars !", str(context.exception)
        )

    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        username = "rares123-"
        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_has_invalid_chars(self):
        username = "rares@1"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have only letters and numbers as characters or '-' ",
            str(context.exception),
        )

    def test_make_from_persistence(self):
        uuid_ = "4a4c58ee-8fd4-415e-9801-947e86b97d7e"
        username = "random-1"
        info = (uuid_, username)
        factory = UserFactory()
        user = factory.make_from_persistence(info)
        self.assertIsInstance(user, User)


if __name__ == "__main__":
    unittest.main()
