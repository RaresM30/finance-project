from pydantic import BaseModel, Field
from uuid import UUID


# todo add field with description, aprox half

class OrmModel(BaseModel):
    class Config:
        orm_mode = True


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars!")


class AssetAdd(BaseModel):
    ticker: str


class AssetInfoBase(BaseModel):
    ticker: str
    name: str
    country: str
    sector: str


class AssetInfoUser(AssetInfoBase):
    units: float


class AssetInfoPrice(AssetInfoBase):
    current_price: float
    currency: str
    today_low_price: float
    today_high_price: float
    open_price: float
    closed_price: float
    fifty_day_price: float


class UserInfo(OrmModel):
    id: UUID = Field(description="An ID by which to identify a user")
    username: str
    stocks: list[AssetInfoBase]
