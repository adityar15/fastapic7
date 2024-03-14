from pydantic import BaseModel, validator, EmailStr
from typing import Optional


class UserInputValidation(BaseModel):
    email: EmailStr
    password: str
    @validator('password')
    def passwordCheck(cls, v):

        if len(v) < 6 or len(v) > 16:
            raise ValueError("Password must be in range of 6 to 16 characters")
        
        return v
    



class UserModel(BaseModel):
    email: str
    class Config:
        orm_mode = True



class UserResponseModel(BaseModel):
    status: int
    message: str
    user: Optional[UserModel] = None
 
    class Config:
        orm_mode = True
   