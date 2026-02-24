from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., max_length=200)
    material: Optional[str] = Field(None, max_length=50)
    karat: Optional[str] = Field(None, max_length=10)
    weight: Optional[float] = Field(None, ge=0)
    price: float = Field(..., ge=0)
    stock_quantity: int = Field(default=0, ge=0)
    description: Optional[str] = None
    image_path: Optional[str] = Field(None, max_length=255)

class ProductCreate(ProductBase):
    jeweler_id: int
    category_ids: Optional[List[int]] = []

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200)
    material: Optional[str] = Field(None, max_length=50)
    karat: Optional[str] = Field(None, max_length=10)
    weight: Optional[float] = Field(None, ge=0)
    price: Optional[float] = Field(None, ge=0)
    stock_quantity: Optional[int] = Field(None, ge=0)
    description: Optional[str] = None
    image_path: Optional[str] = Field(None, max_length=255)
    category_ids: Optional[List[int]] = None

class ProductImageResponse(BaseModel):
    id: int
    image_path: str
    display_order: int
    
    class Config:
        from_attributes = True

class ProductResponse(ProductBase):
    id: int
    jeweler_id: int
    images: List[ProductImageResponse] = []
    categories: List['CategorySimple'] = []
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class CategorySimple(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True

class ProductFilter(BaseModel):
    category_id: Optional[int] = None
    material: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    karat: Optional[str] = None

ProductResponse.model_rebuild()
