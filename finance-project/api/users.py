from fastapi import APIRouter

from domain.asset.factory import AssetFactory
from domain.user.factory import UserFactory
from domain.user.repo import UserRepo
from api.models import UserAdd, UserInfo, AssetInfoUser
from persistence.user_file import UserPersistenceFile

users_router = APIRouter(prefix="/users")

user_persistence = UserPersistenceFile("main_users.json")
repo = UserRepo(user_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


# todo get /users/{user_id}

@users_router.get("/{user_id}", response_model=UserInfo)
def get_user_by_id(user_id: str):
    return repo.get_by_id(user_id)


@users_router.get("/{username}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


# todo delete a user, DELETE /USERS/{user_id}

@users_router.delete("/{user_id}")
#def delete_a_user(user_id: str):
    #return repo.delete_by_id(user_id)


@users_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


# TODO fix api, return asset info
@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, ticker: str):
    asset = AssetFactory().make_new(ticker)
    print(asset.__dict__)
    return asset
