from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..operations import blog

router = APIRouter(
    tags=["Blogs"],
    prefix="/blogs"
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, name='List blogs', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED, name='Create blog')
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, name='Get blog by id', response_model=schemas.ShowBlog)
def show(identifier: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(identifier, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, name='Delete blog by id')
def delete(identifier: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(identifier, db)


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED, name='Update blog by id')
def update(identifier: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(identifier, request, db)
