from domain.asset.asset import Asset
from domain.asset.asset_persistence_interface import AssetPersistenceInterface
from domain.user.user import User


class AssetRepo:
    def __init__(self, persistence: AssetPersistenceInterface):
        self.__persistence = persistence
        self.__assets = None

    def add(self, new_user: User, asset: Asset):
        self.__check_we_have_assets(new_user)
        self.__persistence.add(new_user, asset)
        self.__assets.append([new_user, asset])

    def get_all(self, new_user: User) -> list[Asset]:
        self.__check_we_have_assets(new_user)
        return self.__assets

    def __check_we_have_assets(self, user: User):
        if self.__assets is None:
            self.__assets = self.__persistence.get_all(user)
