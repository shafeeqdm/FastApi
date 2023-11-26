from fastapi import APIRouter , Depends , Response ,  HTTPException , status
from typing import List
import database , schemas , models,oauth2
from sqlalchemy.orm import Session, session
from repository import blog

get_db = database.get_db



router = APIRouter(
    prefix="/blog" ,
    tags=['Blog']
)

@router.get("/", response_model=List[schemas.ShowBlog] )
def get_blog(db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
    
@router.post("/" , status_code=201 )
def create_blog(request : schemas.Blog, db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db,request)


@router.get("/{id}", response_model=schemas.ShowBlog )
def get_blog_id(id ,response : Response , db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(db,id)

@router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED )
def delete_blog(id , db : Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(db, id )

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED )
def update(id , request: schemas.Blog, db: Session = Depends(get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(db , id , request)



