from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime
from models.models import DesignRequestStatus

class DesignGenerateRequest(BaseModel):
    type: str = Field(..., description="Jewelry type: Ring, Necklace, Bracelet, Earrings, Pendant")
    color: str = Field(..., description="Primary color preference")
    shape: str = Field(..., description="Design shape preference")
    material: str = Field(..., description="Material: Gold, Silver, Platinum")
    karat: str = Field(..., description="Karat: 18k, 21k, 22k, 24k")
    gemstone_type: str = Field(default="None", description="Gemstone: Diamond, Ruby, Sapphire, Emerald, None")
    gemstone_color: Optional[str] = Field(None, description="Gemstone color")

class DesignRequestCreate(BaseModel):
    jeweler_id: Optional[int] = None
    generated_design_id: Optional[int] = None
    description: str
    attachment_url: Optional[str] = None
    estimated_budget: Optional[float] = Field(None, ge=0)

class DesignRequestUpdate(BaseModel):
    jeweler_price_offer: Optional[float] = Field(None, ge=0)
    status: Optional[DesignRequestStatus] = None

class UserGeneratedDesignResponse(BaseModel):
    id: int
    user_id: int
    selected_options: Dict[str, Any]
    generated_image_url: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class DesignRequestResponse(BaseModel):
    id: int
    user_id: int
    jeweler_id: Optional[int]
    generated_design_id: Optional[int]
    request_date: datetime
    description: str
    attachment_url: Optional[str]
    estimated_budget: Optional[float]
    jeweler_price_offer: Optional[float]
    status: DesignRequestStatus
    
    class Config:
        from_attributes = True
