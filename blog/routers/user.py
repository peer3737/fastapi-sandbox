from fastapi import APIRouter, Depends, status, Request
from .. import schemas, database
from sqlalchemy.orm import Session
from ..operations import user
from fastapi.templating import Jinja2Templates
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
template = Jinja2Templates(directory=TEMPLATES_DIR)

router = APIRouter(
    tags=['Users'],
    prefix="/users"
)
get_db = database.get_db



@router.post('/', name='Create user', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{identifier}', name='Get user by id', response_model=schemas.ShowUser)
def get_user(identifier: int, request: Request, db: Session = Depends(get_db)):
    data = user.get_user(identifier, db)
    return template.TemplateResponse('index.html', {"request": request, "user": data.__dict__})
    # return data
