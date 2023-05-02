from abc import abstractmethod, ABC

from domain.asset.asset import Asset
from domain.user.user import User


class AssetPersistenceInterface(ABC):
    @abstractmethod
    def add(self, new_user: User, asset: Asset):
        pass

    @abstractmethod
    def get_all(self, new_user: User) -> list[Asset]:
        pass
