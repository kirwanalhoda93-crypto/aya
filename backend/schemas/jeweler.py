from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class JewelerBase(BaseModel):
    name: str = Field(..., max_length=100)
    shop_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None

class JewelerCreate(JewelerBase):
    pass

class JewelerUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    shop_name: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = None
    address: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[EmailStr] = None
    rating: Optional[float] = Field(None, ge=0, le=5)

class JewelerResponse(JewelerBase):
    id: int
    rating: float
    created_at: datetime
    
    class Config:
        from_attributes = True
