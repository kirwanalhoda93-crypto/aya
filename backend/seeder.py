import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal, engine, Base
from models import (
    User, Jeweler, PaymentMethod, Category, Product, ProductImage,
    Cart, Order, OrderItem, UserGeneratedDesign, DesignRequest,
    OrderStatus, DesignRequestStatus, Gender
)
from utils import get_password_hash

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

def seed_database():
    print("Seeding database...")
    
    jewelers_data = [
        {
            "name": "Ahmed Al-Rashid",
            "shop_name": "Al-Rashid Jewelers",
            "bio": "Master jeweler with 25 years of experience in crafting exquisite gold and diamond pieces. Specializing in traditional Arabic designs with modern touches.",
            "address": "123 Gold Souk, Downtown Dubai, UAE",
            "phone": "+971-50-123-4567",
            "email": "ahmed@alrashid-jewelers.com",
            "rating": 4.9
        },
        {
            "name": "Sarah Mitchell",
            "shop_name": "Mitchell Fine Jewelry",
            "bio": "Contemporary jewelry designer known for minimalist silver and platinum pieces. Featured in international fashion magazines.",
            "address": "456 Fifth Avenue, New York, NY 10001, USA",
            "phone": "+1-212-555-0123",
            "email": "sarah@mitchell-jewelry.com",
            "rating": 4.7
        },
        {
            "name": "Hiroshi Tanaka",
            "shop_name": "Tanaka Precious Arts",
            "bio": "Third-generation jeweler combining Japanese craftsmanship with cutting-edge design. Expert in pearl and gemstone jewelry.",
            "address": "789 Ginza District, Tokyo 104-0061, Japan",
            "phone": "+81-3-1234-5678",
            "email": "hiroshi@tanaka-arts.jp",
            "rating": 4.8
        }
    ]
    
    jewelers = []
    for data in jewelers_data:
        jeweler = Jeweler(**data)
        db.add(jeweler)
        jewelers.append(jeweler)
    
    db.flush()
    
    users_data = [
        {
            "username": "john_doe",
            "email": "john@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "+1-555-0101",
            "dob": "1990-05-15",
            "gender": Gender.male,
            "address": "123 Main Street, Los Angeles, CA 90001, USA"
        },
        {
            "username": "emma_wilson",
            "email": "emma@example.com",
            "password": "password123",
            "first_name": "Emma",
            "last_name": "Wilson",
            "phone": "+1-555-0102",
            "dob": "1988-08-22",
            "gender": Gender.female,
            "address": "456 Oak Avenue, Chicago, IL 60601, USA"
        },
        {
            "username": "mohammed_hassan",
            "email": "mohammed@example.com",
            "password": "password123",
            "first_name": "Mohammed",
            "last_name": "Hassan",
            "phone": "+971-50-555-0103",
            "dob": "1992-12-01",
            "gender": Gender.male,
            "address": "789 Palm Street, Abu Dhabi, UAE"
        },
        {
            "username": "yuki_sato",
            "email": "yuki@example.com",
            "password": "password123",
            "first_name": "Yuki",
            "last_name": "Sato",
            "phone": "+81-90-5555-0104",
            "dob": "1995-03-10",
            "gender": Gender.female,
            "address": "321 Sakura Road, Kyoto 604-8001, Japan"
        },
        {
            "username": "sophia_brown",
            "email": "sophia@example.com",
            "password": "password123",
            "first_name": "Sophia",
            "last_name": "Brown",
            "phone": "+44-20-5555-0105",
            "dob": "1993-07-28",
            "gender": Gender.female,
            "address": "654 Baker Street, London W1U 8ED, UK"
        }
    ]
    
    users = []
    for data in users_data:
        user = User(
            username=data["username"],
            email=data["email"],
            password=get_password_hash(data["password"]),
            first_name=data["first_name"],
            last_name=data["last_name"],
            phone=data["phone"],
            dob=data["dob"],
            gender=data["gender"],
            address=data["address"]
        )
        db.add(user)
        users.append(user)
    
    db.flush()
    
    categories_data = [
        {"name": "Rings", "parent_id": None},
        {"name": "Necklaces", "parent_id": None},
        {"name": "Bracelets", "parent_id": None},
        {"name": "Earrings", "parent_id": None},
        {"name": "Engagement Rings", "parent_id": None},
        {"name": "Wedding Bands", "parent_id": None},
        {"name": "Diamond Rings", "parent_id": None},
        {"name": "Gold Necklaces", "parent_id": None},
        {"name": "Pearl Necklaces", "parent_id": None},
        {"name": "Charm Bracelets", "parent_id": None},
    ]
    
    categories = []
    for data in categories_data:
        category = Category(**data)
        db.add(category)
        categories.append(category)
    
    db.flush()
    
    subcategories_data = [
        {"name": "Solitaire Rings", "parent_id": 1},
        {"name": "Eternity Rings", "parent_id": 1},
        {"name": "Cocktail Rings", "parent_id": 1},
        {"name": "Pendant Necklaces", "parent_id": 2},
        {"name": "Choker Necklaces", "parent_id": 2},
        {"name": "Chain Necklaces", "parent_id": 2},
        {"name": "Bangle Bracelets", "parent_id": 3},
        {"name": "Tennis Bracelets", "parent_id": 3},
        {"name": "Stud Earrings", "parent_id": 4},
        {"name": "Hoop Earrings", "parent_id": 4},
        {"name": "Drop Earrings", "parent_id": 4},
    ]
    
    for data in subcategories_data:
        category = Category(**data)
        db.add(category)
        categories.append(category)
    
    db.flush()
    
    payment_methods_data = [
        {
            "method_name": "Bank Transfer",
            "qr_code_image": "/static/qr_codes/bank_transfer_qr.png",
            "is_active": True,
            "notes": "Transfer to: First National Bank\nAccount: 1234567890\nRouting: 021000021"
        },
        {
            "method_name": "PayPal",
            "qr_code_image": "/static/qr_codes/paypal_qr.png",
            "is_active": True,
            "notes": "Send payment to: payments@jewelry-store.com"
        }
    ]
    
    payment_methods = []
    for data in payment_methods_data:
        payment = PaymentMethod(**data)
        db.add(payment)
        payment_methods.append(payment)
    
    db.flush()
    
    products_data = [
        {
            "jeweler_id": 1,
            "name": "Royal Diamond Solitaire Ring",
            "material": "Gold",
            "karat": "18k",
            "weight": 5.2,
            "price": 4500.00,
            "stock_quantity": 3,
            "description": "An exquisite 1.5-carat diamond solitaire ring set in 18k white gold. The perfect symbol of eternal love with VS1 clarity and F color grade.",
            "image_path": "/static/products/ring_1.jpg",
            "category_ids": [1, 5, 7]
        },
        {
            "jeweler_id": 1,
            "name": "Oriental Pearl Necklace",
            "material": "Gold",
            "karat": "21k",
            "weight": 28.5,
            "price": 3200.00,
            "stock_quantity": 5,
            "description": "Stunning strand of 45 natural oriental pearls with 21k gold clasp featuring intricate Arabic patterns.",
            "image_path": "/static/products/necklace_1.jpg",
            "category_ids": [2, 9]
        },
        {
            "jeweler_id": 2,
            "name": "Modern Platinum Wedding Band",
            "material": "Platinum",
            "karat": "950",
            "weight": 8.0,
            "price": 2100.00,
            "stock_quantity": 10,
            "description": "Sleek platinum wedding band with a brushed finish. Contemporary design for the modern couple.",
            "image_path": "/static/products/band_1.jpg",
            "category_ids": [6]
        },
        {
            "jeweler_id": 2,
            "name": "Minimalist Silver Tennis Bracelet",
            "material": "Silver",
            "karat": "925",
            "weight": 12.3,
            "price": 890.00,
            "stock_quantity": 8,
            "description": "Elegant tennis bracelet featuring 20 round-cut cubic zirconia stones in sterling silver setting.",
            "image_path": "/static/products/bracelet_1.jpg",
            "category_ids": [3, 8]
        },
        {
            "jeweler_id": 3,
            "name": "Japanese Akoya Pearl Earrings",
            "material": "Gold",
            "karat": "18k",
            "weight": 3.5,
            "price": 1650.00,
            "stock_quantity": 6,
            "description": "Pair of gorgeous Japanese Akoya pearl stud earrings with 18k yellow gold posts. Classic elegance for any occasion.",
            "image_path": "/static/products/earrings_1.jpg",
            "category_ids": [4, 10]
        },
        {
            "jeweler_id": 3,
            "name": "Sakura Diamond Pendant",
            "material": "Gold",
            "karat": "18k",
            "weight": 4.8,
            "price": 2800.00,
            "stock_quantity": 4,
            "description": "Delicate cherry blossom pendant featuring 12 pavé diamonds set in 18k rose gold. Inspired by Japanese spring.",
            "image_path": "/static/products/pendant_1.jpg",
            "category_ids": [2, 12]
        },
        {
            "jeweler_id": 1,
            "name": "Emerald Eternity Ring",
            "material": "Gold",
            "karat": "18k",
            "weight": 6.1,
            "price": 5200.00,
            "stock_quantity": 2,
            "description": "Breathtaking eternity ring featuring 1.5 carats of Colombian emeralds in 18k yellow gold setting.",
            "image_path": "/static/products/ring_2.jpg",
            "category_ids": [1, 12]
        },
        {
            "jeweler_id": 2,
            "name": "Art Deco Choker Necklace",
            "material": "Gold",
            "karat": "14k",
            "weight": 22.0,
            "price": 1950.00,
            "stock_quantity": 4,
            "description": "Vintage-inspired Art Deco choker with geometric patterns in 14k white gold with diamond accents.",
            "image_path": "/static/products/necklace_2.jpg",
            "category_ids": [2, 13]
        },
        {
            "jeweler_id": 3,
            "name": "Zen Garden Bangle",
            "material": "Silver",
            "karat": "925",
            "weight": 35.0,
            "price": 450.00,
            "stock_quantity": 12,
            "description": "Hand-crafted sterling silver bangle with traditional Japanese zen garden motifs. Oxidized finish for depth.",
            "image_path": "/static/products/bangle_1.jpg",
            "category_ids": [3, 15]
        },
        {
            "jeweler_id": 1,
            "name": "Ruby Drop Earrings",
            "material": "Gold",
            "karat": "18k",
            "weight": 5.2,
            "price": 3800.00,
            "stock_quantity": 3,
            "description": "Magnificent drop earrings featuring 2.5 carats of Burmese rubies surrounded by diamond halos in 18k white gold.",
            "image_path": "/static/products/earrings_2.jpg",
            "category_ids": [4, 11]
        }
    ]
    
    for data in products_data:
        category_ids = data.pop("category_ids", [])
        product = Product(**data)
        db.add(product)
        db.flush()
        
        for cat_id in category_ids:
            category = db.query(Category).filter(Category.id == cat_id).first()
            if category:
                product.categories.append(category)
        
        for i in range(3):
            image = ProductImage(
                product_id=product.id,
                image_path=f"/static/products/{product.name.lower().replace(' ', '_')}_{i+1}.jpg",
                display_order=i
            )
            db.add(image)
    
    db.commit()
    
    print("✓ Created 3 Jewelers (Admin)")
    print("✓ Created 5 Users")
    print(f"✓ Created {len(categories_data) + len(subcategories_data)} Categories")
    print(f"✓ Created {len(payment_methods_data)} Payment Methods")
    print(f"✓ Created {len(products_data)} Products with images")
    print("\nDatabase seeding completed successfully!")
    
    print("\n" + "="*50)
    print("TEST CREDENTIALS:")
    print("="*50)
    print("Users:")
    for user_data in users_data[:3]:
        print(f"  Username: {user_data['username']}")
        print(f"  Password: {user_data['password']}")
        print()
    print("="*50)

if __name__ == "__main__":
    try:
        seed_database()
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()