from typing import Optional, List
from sqlmodel import Session, select
from models import User, UserCreate, UserUpdate, Item, ItemCreate, ItemUpdate


class UserCRUD:
    def create(self, session: Session, user_create: UserCreate) -> User:
        user = User.model_validate(user_create)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get(self, session: Session, user_id: int) -> Optional[User]:
        return session.get(User, user_id)

    def get_by_email(self, session: Session, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()

    def get_multi(self, session: Session, skip: int = 0, limit: int = 100):
        statement = select(User).offset(skip).limit(limit)
        return session.exec(statement).all()

    def update(self, session: Session, user: User, user_update: UserUpdate):
        user_data = user_update.model_dump(exclude_unset=True)
        for key, value in user_data.items():
            setattr(user, key, value)

        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def delete(self, session: Session, user: User) -> User:
        session.delete(user)
        session.commit()
        return user


class ItemCRUD:
    def create(
        self, session: Session, item_create: ItemCreate, supplier_id: int
    ) -> Item:
        item = Item.model_validate(item_create, update={"supplier_id": supplier_id})
        session.add(item)
        session.commit()
        session.refresh(item)
        return item

    def get(self, session: Session, item_id: int) -> Optional[Item]:
        return session.get(Item, item_id)

    def get_multi(self, session: Session, skip: int = 0, limit: int = 100):
        statement = select(Item).offset(skip).limit(limit)
        return session.exec(statement).all()

    def get_by_supplier(self, session: Session, supplier_id: int) -> Optional[Item]:
        statement = select(Item).where(Item.supplier_id == supplier_id)
        return session.exec(statement).all()

    def update(self, session: Session, item: Item, item_update=ItemUpdate):
        item_data = item_update.model_dump(exclude_unset=True)
        for key, value in item_data.items():
            setattr(item, key, value)
            
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
    def delete(self, session: Session, item: Item)-> Item:
        session.delete(item)
        session.commit()
        return item
    

    
user_crud = UserCRUD()
item_crud = ItemCRUD()
