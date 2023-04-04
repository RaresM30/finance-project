import json

from domain.user.factory import UserFactory
from domain.user.persistence_interface import UserPersistenceInterface
from domain.user.user import User

#todo singleton, no hw
class UserRepo:
    def __init__(self, persistence: UserPersistenceInterface):
        self.__persistence = persistence
        self.__users = None


    def add(self, new_user: User):
        #todo refactor to not have duplicate code + add for get_by_id
        if self.__users is None:
            self.__users = self.__persistence.get_all()
        self.__users.append(new_user)
        self.__persistence.add(new_user)



    def get_all(self) -> list[User]:
        if self.__users is None:
            self.__users = self.__persistence.get_all()
        return self.__users

    def get_by_username(self, username: str) -> User:
        for u in self.__users:
            if u.username == username:
                return u

    def get_by_id(self, id_: str) -> User:
        for u in self.__users:
            if str(u.id) == id_:
                return u





