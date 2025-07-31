from pydantic import BaseModel
from typing import Optional
import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    branch: Optional[str] = None

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    branch: Optional[str] = None
    class Config:
        from_attributes = True

class CameraCreate(BaseModel):
    ip: str
    location: str
    source_name: str

class CameraOut(BaseModel):
    id: int
    ip: str
    location: str
    source_name: str
    added_by: int
    edited_by: Optional[int] = None
    added_on: datetime.datetime
    updated_on: datetime.datetime
    class Config:
        from_attributes = True

class LogOut(BaseModel):
    id: int
    user_id: int
    action: str
    timestamp: datetime.datetime
    details: str
    class Config:
        from_attributes = True
