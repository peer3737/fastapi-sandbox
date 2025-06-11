from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def show(identifier: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == identifier).first()
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {identifier} is not available")
    return blog


def delete(identifier: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == identifier)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {identifier} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(identifier: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == identifier)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {identifier} not found")

    blog.update(request.dict())
    db.commit()
    updated_blog = db.query(models.Blog).filter(models.Blog.id == identifier).first()
    return updated_blog
