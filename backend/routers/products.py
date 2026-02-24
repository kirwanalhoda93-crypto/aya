from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional
from database import get_db
from models import Product, Category, Jeweler, ProductImage, product_categories
from schemas import ProductCreate, ProductResponse, ProductUpdate
from routers.auth import get_current_user, get_current_user_optional
from models import User

router = APIRouter(prefix="/api/products", tags=["Products"])

@router.get("/", response_model=List[ProductResponse])
def get_products(
    category_id: Optional[int] = Query(None),
    material: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    karat: Optional[str] = Query(None),
    jeweler_id: Optional[int] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Product).options(
        joinedload(Product.images),
        joinedload(Product.categories),
        joinedload(Product.jeweler)
    )
    
    if category_id:
        query = query.join(product_categories).filter(product_categories.c.category_id == category_id)
    if material:
        query = query.filter(Product.material.ilike(f"%{material}%"))
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if karat:
        query = query.filter(Product.karat == karat)
    if jeweler_id:
        query = query.filter(Product.jeweler_id == jeweler_id)
    
    products = query.offset(skip).limit(limit).all()
    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).options(
        joinedload(Product.images),
        joinedload(Product.categories),
        joinedload(Product.jeweler)
    ).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(
    product_data: ProductCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    jeweler = db.query(Jeweler).filter(Jeweler.id == product_data.jeweler_id).first()
    if not jeweler:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Jeweler not found"
        )
    
    db_product = Product(
        jeweler_id=product_data.jeweler_id,
        name=product_data.name,
        material=product_data.material,
        karat=product_data.karat,
        weight=product_data.weight,
        price=product_data.price,
        stock_quantity=product_data.stock_quantity,
        description=product_data.description,
        image_path=product_data.image_path
    )
    db.add(db_product)
    db.flush()
    
    if product_data.category_ids:
        for cat_id in product_data.category_ids:
            category = db.query(Category).filter(Category.id == cat_id).first()
            if category:
                db_product.categories.append(category)
    
    db.commit()
    db.refresh(db_product)
    return db_product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    for field, value in product_data.model_dump(exclude_unset=True).items():
        if field == "category_ids" and value is not None:
            product.categories.clear()
            for cat_id in value:
                category = db.query(Category).filter(Category.id == cat_id).first()
                if category:
                    product.categories.append(category)
        else:
            setattr(product, field, value)
    
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    db.delete(product)
    db.commit()
    return None

@router.post("/{product_id}/images", response_model=ProductResponse)
def add_product_image(
    product_id: int,
    image_path: str,
    display_order: int = 0,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    image = ProductImage(
        product_id=product_id,
        image_path=image_path,
        display_order=display_order
    )
    db.add(image)
    db.commit()
    db.refresh(product)
    return product

@router.delete("/{product_id}/images/{image_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_image(
    product_id: int,
    image_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    image = db.query(ProductImage).filter(
        ProductImage.id == image_id,
        ProductImage.product_id == product_id
    ).first()
    if not image:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Image not found"
        )
    
    db.delete(image)
    db.commit()
    return None