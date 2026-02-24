from pydantic import BaseModel, Field
from typing import Optional

class PaymentMethodBase(BaseModel):
    method_name: str = Field(..., max_length=100)
    qr_code_image: Optional[str] = Field(None, max_length=255)
    is_active: bool = True
    notes: Optional[str] = None

class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodUpdate(BaseModel):
    method_name: Optional[str] = Field(None, max_length=100)
    qr_code_image: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None
    notes: Optional[str] = None

class PaymentMethodResponse(PaymentMethodBase):
    id: int
    
    class Config:
        from_attributes = True
