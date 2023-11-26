from fastapi import APIRouter , Depends  
from blog import database , schemas 
from sqlalchemy.orm import Session
from blog.repository import user

get_db =database.get_db

router = APIRouter(
    prefix="/User" ,
    tags=['User']
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(db,request)
    
@router.get("/{id}" , response_model=schemas.ShowUser)
def show_user(id:int , db: Session = Depends(get_db)):
    return user.show(db,id)