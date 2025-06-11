from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..hashing import Hash


def create_user(request: schemas.User, db: Session):
    request.password = Hash.bcrypt(request.password)
    new_user = models.User(**request.model_dump())
    db.add(new_user)
    db.commit()
    return new_user


def get_user(identifier: int, db: Session):
    user = db.query(models.User).filter(models.User.id == identifier).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {identifier} is not available")
    return user
