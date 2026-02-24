from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from database import get_db
from models import (
    User, Jeweler, Product, Category, PaymentMethod, Order,
    DesignRequest, UserGeneratedDesign, OrderStatus, DesignRequestStatus
)
from schemas import (
    JewelerCreate, JewelerResponse, JewelerUpdate,
    CategoryCreate, CategoryResponse, CategoryUpdate, CategoryTreeResponse,
    PaymentMethodCreate, PaymentMethodResponse, PaymentMethodUpdate,
    OrderResponse, OrderUpdate,
    DesignRequestResponse, DesignRequestUpdate
)
from routers.auth import get_current_user

router = APIRouter(prefix="/api/admin", tags=["Admin"])

async def verify_admin(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/jewelers", response_model=List[JewelerResponse])
def get_jewelers(
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    return db.query(Jeweler).all()

@router.post("/jewelers", response_model=JewelerResponse, status_code=status.HTTP_201_CREATED)
def create_jeweler(
    jeweler_data: JewelerCreate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    jeweler = Jeweler(**jeweler_data.model_dump())
    db.add(jeweler)
    db.commit()
    db.refresh(jeweler)
    return jeweler

@router.put("/jewelers/{jeweler_id}", response_model=JewelerResponse)
def update_jeweler(
    jeweler_id: int,
    jeweler_data: JewelerUpdate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    jeweler = db.query(Jeweler).filter(Jeweler.id == jeweler_id).first()
    if not jeweler:
        raise HTTPException(status_code=404, detail="Jeweler not found")
    
    for field, value in jeweler_data.model_dump(exclude_unset=True).items():
        setattr(jeweler, field, value)
    db.commit()
    db.refresh(jeweler)
    return jeweler

@router.delete("/jewelers/{jeweler_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_jeweler(
    jeweler_id: int,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    jeweler = db.query(Jeweler).filter(Jeweler.id == jeweler_id).first()
    if not jeweler:
        raise HTTPException(status_code=404, detail="Jeweler not found")
    db.delete(jeweler)
    db.commit()
    return None

@router.get("/categories", response_model=List[CategoryTreeResponse])
def get_categories(
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    return db.query(Category).filter(Category.parent_id == None).all()

@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(
    category_data: CategoryCreate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    if category_data.parent_id:
        parent = db.query(Category).filter(Category.id == category_data.parent_id).first()
        if not parent:
            raise HTTPException(status_code=404, detail="Parent category not found")
    
    category = Category(**category_data.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.put("/categories/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    for field, value in category_data.model_dump(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return None

@router.get("/payment-methods", response_model=List[PaymentMethodResponse])
def get_payment_methods(
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    return db.query(PaymentMethod).all()

@router.post("/payment-methods", response_model=PaymentMethodResponse, status_code=status.HTTP_201_CREATED)
def create_payment_method(
    payment_data: PaymentMethodCreate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    payment = PaymentMethod(**payment_data.model_dump())
    db.add(payment)
    db.commit()
    db.refresh(payment)
    return payment

@router.put("/payment-methods/{payment_id}", response_model=PaymentMethodResponse)
def update_payment_method(
    payment_id: int,
    payment_data: PaymentMethodUpdate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    payment = db.query(PaymentMethod).filter(PaymentMethod.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment method not found")
    
    for field, value in payment_data.model_dump(exclude_unset=True).items():
        setattr(payment, field, value)
    db.commit()
    db.refresh(payment)
    return payment

@router.delete("/payment-methods/{payment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment_method(
    payment_id: int,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    payment = db.query(PaymentMethod).filter(PaymentMethod.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment method not found")
    db.delete(payment)
    db.commit()
    return None

@router.get("/orders", response_model=List[OrderResponse])
def get_all_orders(
    status_filter: str = None,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    query = db.query(Order).options(joinedload(Order.items))
    if status_filter:
        try:
            order_status = OrderStatus(status_filter)
            query = query.filter(Order.status == order_status)
        except ValueError:
            pass
    return query.order_by(Order.order_date.desc()).all()

@router.put("/orders/{order_id}/status", response_model=OrderResponse)
def admin_update_order_status(
    order_id: int,
    order_data: OrderUpdate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    if order_data.status:
        order.status = order_data.status
    db.commit()
    db.refresh(order)
    return order

@router.get("/design-requests", response_model=List[DesignRequestResponse])
def get_design_requests(
    status_filter: str = None,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    query = db.query(DesignRequest)
    if status_filter:
        try:
            request_status = DesignRequestStatus(status_filter)
            query = query.filter(DesignRequest.status == request_status)
        except ValueError:
            pass
    return query.order_by(DesignRequest.request_date.desc()).all()

@router.put("/design-requests/{request_id}", response_model=DesignRequestResponse)
def update_design_request(
    request_id: int,
    request_data: DesignRequestUpdate,
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    design_request = db.query(DesignRequest).filter(DesignRequest.id == request_id).first()
    if not design_request:
        raise HTTPException(status_code=404, detail="Design request not found")
    
    if request_data.jeweler_price_offer is not None:
        design_request.jeweler_price_offer = request_data.jeweler_price_offer
        design_request.status = DesignRequestStatus.quoted
    if request_data.status:
        design_request.status = request_data.status
    
    db.commit()
    db.refresh(design_request)
    return design_request

@router.get("/dashboard")
def get_dashboard_stats(
    current_user: User = Depends(verify_admin),
    db: Session = Depends(get_db)
):
    total_users = db.query(User).count()
    total_orders = db.query(Order).count()
    total_products = db.query(Product).count()
    total_jewelers = db.query(Jeweler).count()
    pending_orders = db.query(Order).filter(Order.status == OrderStatus.pending).count()
    total_revenue = db.query(Order).filter(
        Order.status.in_([OrderStatus.delivered, OrderStatus.shipped])
    ).with_entities(
        db.func.sum(Order.total_amount)
    ).scalar() or 0
    
    return {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_products": total_products,
        "total_jewelers": total_jewelers,
        "pending_orders": pending_orders,
        "total_revenue": float(total_revenue)
    }