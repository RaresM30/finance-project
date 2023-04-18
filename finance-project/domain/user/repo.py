import json
import uuid
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        print("Init user repo")
        self.__persistence = persistence
        self.__users = None

    def add(self, new_user: User):
        self.__check_we_have_users()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__check_we_have_users()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.__check_we_have_users()
        return self.__persistence.get_by_id(uid)

    def delete_by_id(self, uid: str):
        current_users = self.get_all()
        users_without_id = [u for u in current_users if u.id != uuid.UUID(hex=uid)]
        users_info = [(str(x.id), x.username, x.stocks) for x in users_without_id]
        json_current_users = json.dumps(users_info)
        with open(self.__file_path, "w") as f:
            f.write(json_current_users)

    def __check_we_have_users(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()


