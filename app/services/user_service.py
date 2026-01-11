from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.user_repository import create_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def register_user(db: Session, email: str, password: str):
    password_hash = hash_password(password)

    try:
        return create_user(
            db,
            email=email,
            password_hash=password_hash
        )

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )