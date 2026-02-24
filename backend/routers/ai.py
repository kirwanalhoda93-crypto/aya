from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any
from database import get_db
from models import User, UserGeneratedDesign, DesignRequest, Jeweler
from schemas import (
    DesignGenerateRequest, DesignRequestCreate, 
    DesignRequestResponse, UserGeneratedDesignResponse
)
from routers.auth import get_current_user
from utils import generate_jewelry_image

router = APIRouter(prefix="/api/ai", tags=["AI Design"])

@router.post("/generate-design", response_model=Dict[str, Any])
async def generate_design(
    design_request: DesignGenerateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    result = await generate_jewelry_image(
        jewelry_type=design_request.type,
        color=design_request.color,
        shape=design_request.shape,
        material=design_request.material,
        karat=design_request.karat,
        gemstone_type=design_request.gemstone_type,
        gemstone_color=design_request.gemstone_color
    )
    
    if result.get("error"):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result["error"]
        )
    
    selected_options = {
        "type": design_request.type,
        "color": design_request.color,
        "shape": design_request.shape,
        "material": design_request.material,
        "karat": design_request.karat,
        "gemstone_type": design_request.gemstone_type,
        "gemstone_color": design_request.gemstone_color
    }
    
    generated_design = UserGeneratedDesign(
        user_id=current_user.id,
        selected_options=selected_options,
        generated_image_url=result["image_path"]
    )
    db.add(generated_design)
    db.commit()
    db.refresh(generated_design)
    
    return {
        "success": True,
        "design_id": generated_design.id,
        "image_url": result["image_path"],
        "selected_options": selected_options
    }

@router.get("/my-designs", response_model=list[UserGeneratedDesignResponse])
def get_my_designs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    designs = db.query(UserGeneratedDesign).filter(
        UserGeneratedDesign.user_id == current_user.id
    ).order_by(UserGeneratedDesign.created_at.desc()).all()
    return designs

@router.get("/designs/{design_id}", response_model=UserGeneratedDesignResponse)
def get_design(
    design_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    design = db.query(UserGeneratedDesign).filter(
        UserGeneratedDesign.id == design_id,
        UserGeneratedDesign.user_id == current_user.id
    ).first()
    
    if not design:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Design not found"
        )
    return design

@router.post("/request-quote", response_model=DesignRequestResponse, status_code=status.HTTP_201_CREATED)
def request_quote(
    request_data: DesignRequestCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if request_data.jeweler_id:
        jeweler = db.query(Jeweler).filter(Jeweler.id == request_data.jeweler_id).first()
        if not jeweler:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Jeweler not found"
            )
    
    design_request = DesignRequest(
        user_id=current_user.id,
        jeweler_id=request_data.jeweler_id,
        generated_design_id=request_data.generated_design_id,
        description=request_data.description,
        attachment_url=request_data.attachment_url,
        estimated_budget=request_data.estimated_budget
    )
    db.add(design_request)
    db.commit()
    db.refresh(design_request)
    return design_request

@router.get("/my-requests", response_model=list[DesignRequestResponse])
def get_my_requests(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    requests = db.query(DesignRequest).filter(
        DesignRequest.user_id == current_user.id
    ).order_by(DesignRequest.request_date.desc()).all()
    return requests