import uuid
from domain.user.user import User


class InvalidUsername(Exception):
    pass


class UserFactory:
    def make_new(self, username: str) -> User:
        if len(username) < 6:
            raise InvalidUsername("Username should have at least 6 chars")
        if len(username) > 20:
            raise InvalidUsername("Username should have a maximum of 20 chars !")
        for x in username:
            if not (x.isalnum() or x == "-"):
                raise InvalidUsername(
                    "Username should have only letters and numbers as characters or '-' "
                )

        user_uuid = uuid.uuid4()
        return User(user_uuid, username)

    @classmethod
    def make_from_persistence(cls, info: tuple) -> User:
        return User(
            uuid=uuid.UUID(info[0]),
            username=info[1],
        )
