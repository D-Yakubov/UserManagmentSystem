from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from pydantic.types import conint

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    model_config = ConfigDict(coerce_numbers_to_str=True)