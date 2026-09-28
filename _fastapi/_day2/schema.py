from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
  username: str
  email: str
  bio: Optional[str] = None

class UserResponse(CreateUser):
  id: int

class UpdateUser(BaseModel):
  id: int
  username: Optional[str] = None
  email: Optional[str] = None
  bio: Optional[str] = None