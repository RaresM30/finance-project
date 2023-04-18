import json
import uuid

from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


class UserPersistenceFile(UserPersistenceInterface):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def get_all(self) -> list[User]:
        try:
            file = open(self.__file_path)
            contents = file.read()
            file.close()
            users_info = json.loads(contents)
            factory = UserFactory()
            return [factory.make_from_persistence(x) for x in users_info]
        except:
            #todo hw, log error
                return []

    def add(self, user: User):
        current_users = self.get_all()
        current_users.append(user)
        users_info = [(str(x.id), x.username, x.stocks) for x in current_users]
        users_json = json.dumps(users_info)
        # todo refactor with
        file = open(self.__file_path, "w")
        file.write(users_json)
        file.close()

    def get_by_id(self, uid: str) -> User:
        current_users = self.get_all()
        for u in current_users:
            if u.id == uuid.UUID(hex=uid):
                assets = AssetRepo().get_for_user(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets,
                )

    def delete_by_id(self, uid: str):
        pass

