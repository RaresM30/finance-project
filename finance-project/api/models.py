

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


class AssetInfoBase(OrmModel):
    ticker: str = Field(description="A code that identifies the asset")
    name: str = Field(description="The name that describes the chosen asset")
    country: str = Field(description="The country where the asset first started")
    sector: str = Field(description="The sector where the asset belongs")


class AssetInfoUser(AssetInfoBase):
    units: float = Field("Number of units of the asset")


class AssetInfoPrice(AssetInfoBase):
    current_price: float = Field(description="The current price of the asset")
    currency: str = Field(description="The actual currency")
    today_low_price: float = Field(description="Lowest price for the current day")
    today_high_price: float = Field(description="Highest price for the current day")
    open_price: float = Field(description="Opening price for the asset in the current day")
    closed_price: float = Field(description="Closing price for the asset in the previous day")
    fifty_day_price: float = Field(description="The average price over the past fifty days")


class UserInfo(OrmModel):
    id: UUID = Field(description="An ID by which to identify a user")
    username: str
    stocks: list[AssetInfoBase] = Field("A list of stocks")
