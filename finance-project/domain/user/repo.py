import json
import uuid

from config.config_for_asset import check_asset_persistence_type
from domain.asset.asset_persistence_interface import AssetPersistenceInterface
from singleton import singleton
from domain.asset.repo import AssetRepo
from domain.user.factory import UserFactory
from domain.user.user_persistence_interface import UserPersistenceInterface
from domain.user.user import User


@singleton
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface, asset: AssetPersistenceInterface):
        print("Init user repo")
        self.__persistence = persistence
        self.__users = None
        self.__asset = asset

    def add(self, new_user: User):
        self.__check_we_have_users()
        self.__persistence.add(new_user)
        self.__users.append(new_user)

    def get_all(self) -> list[User]:
        self.__check_we_have_users()
        return self.__users

    def get_by_id(self, uid: str) -> User:
        self.__check_we_have_users()

        for u in self.__users:
            if u.id == uuid.UUID(hex=uid):
                asset_persistence = check_asset_persistence_type(
                    "config.json"
                )
                assets = asset_persistence.get_all(u)
                return User(
                    uuid=u.id,
                    username=u.username,
                    stocks=assets,
                )

    def delete_by_id(self, uid: str):
        self.__check_we_have_users()
        self.__persistence.delete_by_id(uid)

    def edit(self, user_id: str, username: str):
        self.__check_we_have_users()
        self.__persistence.edit(user_id, username)
        for user in self.__users:
            if user.id == uuid.UUID(hex=user_id):
                user.username = username

    def __check_we_have_users(self):
        if self.__users is None:
            self.__users = self.__persistence.get_all()
