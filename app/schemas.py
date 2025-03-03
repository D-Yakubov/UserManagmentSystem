#from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
#from pydantic.types import conint

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_active: bool=True
    is_admin: bool = False

class UserCreate(UserBase):
    #email: EmailStr
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    role: str

class AdminCreate(AdminBase):
    user_id: int

class Admin(AdminBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    model_config = ConfigDict(coerce_numbers_to_str=True)