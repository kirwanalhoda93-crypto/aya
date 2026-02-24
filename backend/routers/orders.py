from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from database import get_db
from models import Order, OrderItem, Cart, CartItem, Product, PaymentMethod, User, OrderStatus
from schemas import OrderCreate, OrderResponse, OrderUpdate
from routers.auth import get_current_user

router = APIRouter(prefix="/api/orders", tags=["Orders"])

@router.post("/checkout", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def checkout(
    order_data: OrderCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    cart = db.query(Cart).options(
        joinedload(Cart.items).joinedload(CartItem.product)
    ).filter(Cart.user_id == current_user.id).first()
    
    if not cart or not cart.items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cart is empty"
        )
    
    payment_method = db.query(PaymentMethod).filter(
        PaymentMethod.id == order_data.payment_method_id,
        PaymentMethod.is_active == True
    ).first()
    
    if not payment_method:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Payment method not found or inactive"
        )
    
    total_amount = 0
    order_items_data = []
    
    for cart_item in cart.items:
        if cart_item.product.stock_quantity < cart_item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product: {cart_item.product.name}"
            )
        
        subtotal = cart_item.product.price * cart_item.quantity
        total_amount += subtotal
        order_items_data.append({
            "product_id": cart_item.product_id,
            "quantity": cart_item.quantity,
            "unit_price": cart_item.product.price,
            "subtotal": subtotal
        })
    
    order = Order(
        user_id=current_user.id,
        payment_method_id=order_data.payment_method_id,
        total_amount=total_amount,
        shipping_address=order_data.shipping_address,
        transfer_receipt=order_data.transfer_receipt,
        status=OrderStatus.pending
    )
    db.add(order)
    db.flush()
    
    for item_data in order_items_data:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item_data["product_id"],
            quantity=item_data["quantity"],
            unit_price=item_data["unit_price"],
            subtotal=item_data["subtotal"]
        )
        db.add(order_item)
        
        product = db.query(Product).filter(Product.id == item_data["product_id"]).first()
        product.stock_quantity -= item_data["quantity"]
    
    db.query(CartItem).filter(CartItem.cart_id == cart.id).delete()
    
    db.commit()
    db.refresh(order)
    
    return order

@router.get("/", response_model=List[OrderResponse])
def get_orders(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    orders = db.query(Order).options(
        joinedload(Order.items)
    ).filter(Order.user_id == current_user.id).order_by(Order.order_date.desc()).all()
    return orders

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).options(
        joinedload(Order.items)
    ).filter(Order.id == order_id, Order.user_id == current_user.id).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@router.put("/{order_id}/status", response_model=OrderResponse)
def update_order_status(
    order_id: int,
    order_data: OrderUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    if order_data.status:
        order.status = order_data.status
    if order_data.shipping_address:
        order.shipping_address = order_data.shipping_address
    if order_data.transfer_receipt:
        order.transfer_receipt = order_data.transfer_receipt
    
    db.commit()
    db.refresh(order)
    return order