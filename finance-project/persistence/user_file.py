import json
import uuid
import logging
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.user_persistence_interface import UserPersistenceInterface
from domain.user.user import User
from persistence.asset_sqlite import AssetPersistenceSqlite

logging.basicConfig(
    filename="finance.log",
    level=logging.DEBUG,
    format="%(asctime)s _ %(levelname)s _ %(name)s _ %(message)s",
)


class ErrorWhenWritingInPersistence(Exception):
    pass


class UserPersistenceFile(UserPersistenceInterface):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        try:
            with open(self.__file_path) as f:
                contents = f.read()
            users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistence(x) for x in users_info]

        except Exception as e:
            logging.error("Could not read file, reason: " + str(e))
            return []

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        users_json = json.dumps(users_info)
        try:
            with open(self.__file_path, "w") as file:
                file.write(users_json)
        except ErrorWhenWritingInPersistence as e:
            logging.error("Sorry! We can't write info into persistence! Error: " + str(e))
            raise e

    def get_by_id(self, uid: str) -> User:
        current_users = self.get_all()
        for u in current_users:
            if u.id == uuid.UUID(hex=uid):
                assets = AssetRepo(AssetPersistenceSqlite()).get_all(u)

                return User(uuid=u.id,
                            username=u.username,
                            stocks=assets
                            )

    def delete_by_id(self, uid: str):
        current_users = self.get_all()
        users_without_id = [u for u in current_users if u.id != uuid.UUID(hex=uid)]
        users_info = [(str(x.id), x.username, x.stocks) for x in users_without_id]
        json_current_users = json.dumps(users_info)
        try:
            with open(self.__file_path, "w") as f:
                f.write(json_current_users)
        except ErrorWhenWritingInPersistence as e:
            logging.warning("Sorry! We can't perform this action! Error: " + str(e))
            raise e

    def edit(self, user_id: str, username: str):
        current_users = self.get_all()
        for user in current_users:
            if user.id == uuid.UUID(hex=user_id):
                user.username = username
        users_info = [(str(u.id), u.username, u.stocks) for u in current_users]
        users_json = json.dumps(users_info)
        try:
            with open(self.__file_path, "w") as f:
                f.write(users_json)
        except ErrorWhenWritingInPersistence as e:
            logging.warning("Sorry! We can't perform this action!")
