from sqlalchemy.orm import Session
import models,schemas
from fastapi import HTTPException,status

def get_all(db : Session):
    blog = db.query(models.Blog).all()
    return blog

def create(db : Session,request):
    new_blog = models.Blog(title = request.title, body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(db : Session , id:int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail  = f"{id} not found" )
    return blog

def update(db : Session, id: int , request: schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found")
    blog.update(request.dict()) 
    db.commit()
    return 'Successfully updated'

def delete(db : Session , id : int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Done"}
