from sqlalchemy.orm import Session
from app.models.user import User


def create_user(db: Session, email: str, password_hash: str) -> User:
    user = User(
        email=email,
        password_hash=password_hash,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
