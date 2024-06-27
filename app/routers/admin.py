from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    
    prefix="/admins",
    tags=['Admins']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    
    #hash the password - user.password
    hashed_password = utils.get_hashed_password(admin.password)
    admin.password = hashed_password
    
    new_admin = models.Admin(**admin.model_dump())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    
    return new_admin

@router.get('/{id}', response_model=schemas.Admin)
def get_admin(id: int, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin with id: {id} does not exist")
    
    return admin