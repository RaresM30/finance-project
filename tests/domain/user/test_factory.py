import unittest
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
        username = "rares123-"
        uuid_test = "5a4c46aa-7fg4415e980-1932e85b-97d7e"
        test_info = (uuid_test, username)

        factory = UserFactory()
        user = factory.make_from_persistence(test_info)

        self.assertIsInstance(user, User)
        self.assertEqual(user.id, UUID(uuid_test))
        self.assertEqual(user.username, username)



if __name__ == "__main__":
    unittest.main()
