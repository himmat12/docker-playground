from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from core.db import get_session
from models import User, UserCreate, UserRead, UserUpdate
from crud import user_crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    user_create: UserCreate,
    session: Session = Depends(get_session),
):
    # checking if user exists
    existing_user = user_crud.get_by_email(session, user_create.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    return user_crud.create(session, user_create)


@router.get("/", response_model=List[UserRead])
def read_users(
    skip: int = 0,
    limit: int = 100,
    session: Session = Depends(get_session),
):
    return user_crud.get_multi(session, skip, limit)


@router.get("/{user_id}", response_model=UserRead)
def read_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = user_crud.get(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )


@router.put("/{user_id}", response_model=UserRead)
def update_user(
    user_id: int,
    user_update: UserUpdate,
    session: Session = Depends(get_session),
):
    user = user_crud.get(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user_crud.update(session, user, user_update)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = user_crud.get(session, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    user_crud.delete(session, user)
    return {"message": "User deleted successfullt"}
