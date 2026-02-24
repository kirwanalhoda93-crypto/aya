from pydantic import BaseModel, Field
from typing import Optional, List

class CategoryBase(BaseModel):
    name: str = Field(..., max_length=100)
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    parent_id: Optional[int] = None

class CategoryResponse(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

class CategoryTreeResponse(CategoryResponse):
    children: List['CategoryTreeResponse'] = []
    
    class Config:
        from_attributes = True

CategoryTreeResponse.model_rebuild()
