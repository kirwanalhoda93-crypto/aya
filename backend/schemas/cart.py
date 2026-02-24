from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from schemas.product import ProductResponse

class CartItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1)

class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: ProductResponse
    
    class Config:
        from_attributes = True

class CartResponse(BaseModel):
    id: int
    user_id: int
    updated_at: datetime
    items: List[CartItemResponse] = []
    total: float = 0.0
    
    class Config:
        from_attributes = True
