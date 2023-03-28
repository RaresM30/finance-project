from pydantic import BaseModel, Field
from uuid import UUID


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars!")


class UserInfo(BaseModel):
    id: UUID
    username: str
    stocks: list[str]

    class Config:
        orm_mode = True


class AssetInfo(BaseModel):
    ticker: str
    units: float
    name: str
    country: str