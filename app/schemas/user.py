from pydantic import BaseModel,Field

class UserBase(BaseModel):
    username : str = Field(...,max_length=50)
    hashed_password: str # типо хэш

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id : int
    level: int
    score:int