from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# User base model
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    full_name: str
    is_active: bool = True


# User model from Userbase (which represents the postgreSQL table)
class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: Optional[datetime] = Field(default=None)

    #  Bidirectional relationship with Item table
    items: List["Item"] = Relationship(back_populates="supplier")


#  Item base model
class ItemBase(SQLModel):
    title: str
    description: str
    price: int
    is_offer: bool = False


# Item model from ItemBase (which represents the postgreSQL table)
class Item(ItemBase, table=True):
    __tablename__ = "items"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    supplier_id: int = Field(foreign_key="users.id")  # foreign key

    #  Bidirectional relationship with User table
    supplier: User = Relationship(back_populates="items")


# pydantic models for API


# User
class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime


class UserUpdate(SQLModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


# Item
class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    created_at: datetime
    supplier_id: int


class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    is_offer: Optional[bool] = None


__all__ = ["User", "Item"]
