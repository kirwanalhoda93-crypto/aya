from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from models.models import OrderStatus

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(..., ge=1)
    unit_price: float
    subtotal: float

class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    payment_method_id: int
    shipping_address: str
    transfer_receipt: Optional[str] = None

class OrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None
    shipping_address: Optional[str] = None
    transfer_receipt: Optional[str] = None

class OrderResponse(BaseModel):
    id: int
    user_id: int
    payment_method_id: Optional[int]
    order_date: datetime
    status: OrderStatus
    total_amount: float
    shipping_address: str
    transfer_receipt: Optional[str]
    items: List[OrderItemResponse] = []
    
    class Config:
        from_attributes = True
