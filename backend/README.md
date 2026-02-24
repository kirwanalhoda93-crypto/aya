# Jewelry E-commerce & AI Design Platform - Backend API

A complete FastAPI backend for a jewelry e-commerce platform with AI-powered jewelry design generation using Google Gemini API.

## Technology Stack

- **Framework**: FastAPI (Python 3.9+)
- **Database**: MySQL (XAMPP)
- **ORM**: SQLAlchemy with Pydantic validation
- **Authentication**: JWT (python-jose)
- **AI Integration**: Google Gemini API
- **API Documentation**: Swagger UI / ReDoc

## Quick Start

### 1. Prerequisites

- Python 3.9 or higher
- XAMPP (MySQL Server)
- Google Gemini API Key

### 2. Database Setup (XAMPP)

1. **Start XAMPP**:
   - Open XAMPP Control Panel
   - Start **Apache** and **MySQL** services

2. **Create Database**:
   - Open browser and go to `http://localhost/phpmyadmin`
   - Click "New" to create a new database
   - Name it `jewelry_db`
   - Click "Create"

### 3. Installation

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
copy .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### 4. Configure Environment

Edit `.env` file:
```env
DATABASE_URL=mysql+pymysql://root:@localhost:3306/jewelry_db
SECRET_KEY=your-super-secret-key-change-in-production
GEMINI_API_KEY=your-gemini-api-key-here
```

### 5. Seed Database

```bash
# Run the seeder to populate test data
python seeder.py
```

### 6. Run Server

```bash
# Start the FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at: `http://localhost:8000`

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication (`/api/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login and get JWT token |
| GET | `/me` | Get current user profile |
| PUT | `/me` | Update current user profile |

### Products (`/api/products`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | List all products (with filters) |
| GET | `/{id}` | Get single product |
| POST | `/` | Create product |
| PUT | `/{id}` | Update product |
| DELETE | `/{id}` | Delete product |
| POST | `/{id}/images` | Add product image |

**Query Parameters for GET `/`:**
- `category_id` - Filter by category
- `material` - Filter by material (Gold, Silver, Platinum)
- `min_price` - Minimum price
- `max_price` - Maximum price
- `karat` - Filter by karat (18k, 21k, etc.)
- `jeweler_id` - Filter by jeweler

### Cart (`/api/cart`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | View cart |
| POST | `/add` | Add item to cart |
| PUT | `/update/{item_id}` | Update item quantity |
| DELETE | `/remove/{item_id}` | Remove item from cart |
| DELETE | `/clear` | Clear entire cart |

### Orders (`/api/orders`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/checkout` | Create order from cart |
| GET | `/` | Get user's orders |
| GET | `/{id}` | Get single order |
| PUT | `/{id}/status` | Update order status |

### Admin (`/api/admin`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard` | Dashboard statistics |
| GET/POST | `/jewelers` | Jewelers CRUD |
| GET/POST | `/categories` | Categories CRUD |
| GET/POST | `/payment-methods` | Payment methods CRUD |
| GET | `/orders` | All orders (with status filter) |
| GET | `/design-requests` | All design requests |

### AI Design (`/api/ai`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/generate-design` | Generate AI jewelry design |
| GET | `/my-designs` | Get user's generated designs |
| GET | `/designs/{id}` | Get single design |
| POST | `/request-quote` | Request jeweler quote |
| GET | `/my-requests` | Get user's quote requests |

## Frontend Integration Guide

### 1. Authentication

**Login:**
```javascript
async function login(username, password) {
    const response = await fetch('http://localhost:8000/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    localStorage.setItem('token', data.access_token);
    return data;
}
```

**Get Current User:**
```javascript
async function getCurrentUser() {
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:8000/api/auth/me', {
        headers: { 'Authorization': `Bearer ${token}` }
    });
    return await response.json();
}
```

### 2. Products

**Get Products with Filters:**
```javascript
async function getProducts(filters = {}) {
    const params = new URLSearchParams();
    if (filters.category) params.append('category_id', filters.category);
    if (filters.material) params.append('material', filters.material);
    if (filters.minPrice) params.append('min_price', filters.minPrice);
    if (filters.maxPrice) params.append('max_price', filters.maxPrice);
    
    const response = await fetch(`http://localhost:8000/api/products?${params}`);
    return await response.json();
}
```

### 3. Cart Management

**Add to Cart:**
```javascript
async function addToCart(productId, quantity = 1) {
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:8000/api/cart/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ product_id: productId, quantity })
    });
    return await response.json();
}
```

### 4. AI Design Generation

**Generate Jewelry Design:**
```javascript
async function generateDesign(designOptions) {
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:8000/api/ai/generate-design', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            type: 'Ring',          // Ring, Necklace, Bracelet, Earrings, Pendant
            color: 'Gold',         // Primary color
            shape: 'Round',        // Design shape
            material: 'Gold',      // Gold, Silver, Platinum
            karat: '18k',          // 18k, 21k, 22k, 24k
            gemstone_type: 'Diamond', // Diamond, Ruby, Sapphire, Emerald, None
            gemstone_color: 'White'   // Gemstone color (optional)
        })
    });
    return await response.json();
}

// Example usage
const result = await generateDesign({
    type: 'Ring',
    color: 'Rose Gold',
    shape: 'Cushion',
    material: 'Gold',
    karat: '18k',
    gemstone_type: 'Ruby',
    gemstone_color: 'Red'
});

console.log('Design ID:', result.design_id);
console.log('Image URL:', result.image_url);
```

### 5. Checkout

**Create Order:**
```javascript
async function checkout(paymentMethodId, shippingAddress) {
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:8000/api/orders/checkout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            payment_method_id: paymentMethodId,
            shipping_address: shippingAddress,
            transfer_receipt: null // Optional: receipt image path
        })
    });
    return await response.json();
}
```

## Test Credentials

After running `seeder.py`:

| Username | Password | Role |
|----------|----------|------|
| john_doe | password123 | Customer |
| emma_wilson | password123 | Customer |
| mohammed_hassan | password123 | Customer |

## Project Structure

```
backend/
├── main.py              # FastAPI application entry
├── database.py          # Database configuration
├── seeder.py            # Database seeder
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── models/
│   ├── __init__.py
│   └── models.py        # SQLAlchemy models
├── schemas/
│   ├── __init__.py
│   ├── user.py          # User Pydantic schemas
│   ├── product.py       # Product schemas
│   ├── cart.py          # Cart schemas
│   ├── order.py         # Order schemas
│   └── design.py        # AI Design schemas
├── routers/
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   ├── products.py      # Product routes
│   ├── cart.py          # Cart routes
│   ├── orders.py        # Order routes
│   ├── admin.py         # Admin routes
│   └── ai.py            # AI design routes
├── utils/
│   ├── __init__.py
│   ├── auth.py          # JWT & password utilities
│   └── gemini.py        # Gemini API integration
└── static/
    ├── generated_designs/  # AI-generated images
    └── qr_codes/           # Payment QR codes
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | MySQL connection string | `mysql+pymysql://root:@localhost:3306/jewelry_db` |
| `SECRET_KEY` | JWT secret key | - |
| `ALGORITHM` | JWT algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time | `1440` (24 hours) |
| `GEMINI_API_KEY` | Google Gemini API key | - |

## Troubleshooting

### Database Connection Error
- Ensure XAMPP MySQL is running
- Check database name is `jewelry_db`
- Verify user `root` has no password (default XAMPP)

### Import Errors
```bash
pip install -r requirements.txt
```

### CORS Issues
- CORS is enabled for all origins (`*`)
- Ensure frontend uses correct API URL

## License

MIT License