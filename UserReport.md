# AURELIA - موقع المجوهرات الفاخرة

## نظرة عامة على المشروع
واجهة مستخدم احترافية لموقع تجارة إلكترونية للمجوهرات الفاخرة. التصميم يتبع أفضل ممارسات واجهة المستخدم وتجربة المستخدم الحديثة مع التركيز على الأناقة والاستجابة وعناصر جاهزة للإنتاج.

## التقنيات المستخدمة
- **HTML5** - هيكل دلالي
- **CSS3** - خصائص مخصصة، Flexbox، Grid، رسوم متحركة
- **Font Awesome** - مكتبة الأيقونات
- **Google Fonts** - Cormorant Garamond (العناوين)، Montserrat (النصوص)

## لوحة الألوان
| المتغير | القيمة | الاستخدام |
|---------|--------|-----------|
| `--primary-gold` | #C9A961 | اللون الرئيسي، أزرار الدعوة للعمل |
| `--primary-gold-light` | #E8D5A3 | حالات التمرير |
| `--primary-gold-dark` | #8B7355 | نصوص مميزة |
| `--black` | #0A0A0A | اللون الداكن الرئيسي |
| `--white` | #FFFFFF | اللون الفاتح الرئيسي |
| `--cream` | #F5F0E8 | الخلفيات |
| `--emerald` | #0B4533 | اللافتات الترويجية |

## الصفحات المنفذة

### 1. الصفحة الرئيسية (index.html)
- **قسم البطل**: ارتفاع كامل مع صورة مجوهرات متحركة وخلفية متدرجة
- **شبكة المجموعات**: شبكة من 4 أعمدة للخواتم والقلادات والأساور والأقراط
- **الأكثر مبيعاً**: شبكة من 8 منتجات مع تأثيرات التمرير
- **لافتة ترويجية**: تدرج الزمرد مع دعوة للعمل
- **قسم النشرة الإخبارية**: نموذج اشتراك بالبريد الإلكتروني
- **التذييل**: شبكة من 5 أعمدة مع روابط التواصل الاجتماعي

### 2. صفحة المتجر (shop.html)
- **شريط الفلاتر الجانبي**: الفئة، المادة، الأحجار الكريمة، نطاق السعر، اللون
- **شبكة المنتجات**: شبكة متجاوبة من 4 أعمدة
- **الترتيب**: المميزة، السعر، الأحدث، الأكثر مبيعاً
- **بطاقات المنتجات**: تأثيرات التمرير، إجراءات سريعة، شارات

### 3. صفحة تفاصيل المنتج (product.html)
- **معرض الصور**: الصورة الرئيسية مع تكبير، تنقل الصور المصغرة
- **خيارات المنتج**: محدد الحجم، نوع المعدن، خيارات الألوان
- **محدد الكمية**: أزرار الزيادة والنقصان
- **إضافة إلى السلة**: زر الدعوة الرئيسي مع زر قائمة الأمنيات
- **منتجات ذات صلة**: قسم العناصر المشابهة

### 4. مصمم المجوهرات المخصص (customize.html)
- **لوحة المعاينة المباشرة**: معاينة المنتج المتحركة
- **التخصيص خطوة بخطوة**:
  1. اختيار المعدن (6 خيارات مع الأسعار)
  2. اختيار الأحجار الكريمة (8 خيارات)
  3. اختيار الشكل (8 أشكال)
  4. إدخال النقش (حد 20 حرف)
  5. اختيار مقاس الخاتم
- **تسعير ديناميكي**: حساب السعر في الوقت الفعلي

### 5. صفحة السلة (cart.html)
- **جدول عناصر السلة**: معلومات المنتج، السعر، الكمية، الإزالة
- **ملخص الطلب**: المجموع الفرعي، الشحن، الضريبة، الإجمالي
- **رمز ترويجي**: حقل إدخال الخصم
- **منتجات ذات صلة**: قسم "أكمل إطلالتك"

### 6. صفحة الدفع (checkout.html)
- **معلومات الاتصال**: البريد الإلكتروني، الهاتف
- **عنوان الشحن**: نموذج العنوان الكامل
- **طرق الشحن**: قياسي، سريع، بين عشية وضحاها
- **طرق الدفع**: بطاقة ائتمان، PayPal، Apple Pay
- **ملخص الطلب**: قائمة منتجات قابلة للطي

## نقاط الاستجابة
- **سطح المكتب**: > 1200px
- **الجهاز اللوحي**: 768px - 1200px
- **الجوال**: < 768px
- **الجوال الصغير**: < 480px

## الميزات الرئيسية
1. **رأس ثابت**: من شفاف إلى صلب عند التمرير
2. **رسوم متحركة سلسة**: تأثيرات التلاشي والانزلاق والعوم
3. **تأثيرات التمرير**: تكبير الصور، انتقالات الأزرار، الكشف عن التراكب
4. **عناصر تفاعلية**: عناصر التحكم في الكمية، محددات الخيارات، منتقي الألوان
5. **التحقق من النموذج**: الحقول المطلوبة، تنسيق المدخلات
6. **إمكانية الوصول**: HTML دلالي، تسميات مناسبة، نسب التباين

## هيكل الملفات
```
jewelry-website/
├── css/
│   └── styles.css
├── images/
├── index.html
├── shop.html
├── product.html
├── customize.html
├── cart.html
└── checkout.html
```

## دعم المتصفحات
- Chrome (الأحدث)
- Firefox (الأحدث)
- Safari (الأحدث)
- Edge (الأحدث)

## التحسينات المستقبلية
- وظائف JavaScript لإدارة السلة
- تكامل الخلفية لبيانات المنتج
- مصادقة المستخدم
- استمرارية قائمة الأمنيات
- وظيفة البحث
- منطق فلترة المنتجات

---

# المرحلة الثانية: Backend API

## نظرة عامة على Backend
تم بناء واجهة برمجة تطبيقات (API) كاملة باستخدام FastAPI لمنصة تجارة المجوهرات الإلكترونية مع ميزة تصميم المجوهرات بالذكاء الاصطناعي.

## التقنيات المستخدمة
- **Framework**: FastAPI (Python 3.9+)
- **Database**: MySQL (XAMPP)
- **ORM**: SQLAlchemy + Pydantic
- **Authentication**: JWT (python-jose)
- **AI Integration**: Google Gemini API (gemini-2.0-flash-exp)
- **Password Hashing**: bcrypt

## هيكل قاعدة البيانات (12 جدول)

### الجداول الرئيسية:
| الجدول | الوصف |
|--------|-------|
| `users` | المستخدمين (id, username, password, email, first_name, last_name, phone, dob, gender, address, created_at) |
| `jewelers` | الجواهريين (id, name, shop_name, bio, address, phone, email, rating, created_at) |
| `payment_methods` | طرق الدفع (id, method_name, qr_code_image, is_active, notes) |
| `categories` | الفئات (id, name, parent_id) - دعم الفئات الفرعية |
| `products` | المنتجات (id, jeweler_id, name, material, karat, weight, price, stock_quantity, description, image_path) |
| `product_images` | صور المنتجات (id, product_id, image_path, display_order) |
| `product_categories` | علاقة M:N بين المنتجات والفئات |
| `carts` | سلات التسوق (id, user_id, updated_at) |
| `cart_items` | عناصر السلة (id, cart_id, product_id, quantity) |
| `orders` | الطلبات (id, user_id, payment_method_id, order_date, status, total_amount, shipping_address, transfer_receipt) |
| `order_items` | عناصر الطلب (id, order_id, product_id, quantity, unit_price, subtotal) |
| `user_generated_designs` | تصاميم المستخدمين (id, user_id, selected_options, generated_image_url, created_at) |
| `design_requests` | طلبات التصميم (id, user_id, jeweler_id, generated_design_id, request_date, description, attachment_url, estimated_budget, jeweler_price_offer, status) |

### Enums:
- `OrderStatus`: pending, confirmed, processing, shipped, delivered, cancelled
- `DesignRequestStatus`: pending, reviewing, quoted, accepted, rejected, completed
- `Gender`: male, female, other

## نقاط API

### 1. المصادقة (`/api/auth`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| POST | `/register` | تسجيل مستخدم جديد |
| POST | `/login` | تسجيل الدخول والحصول على JWT |
| GET | `/me` | الحصول على بيانات المستخدم الحالي |
| PUT | `/me` | تحديث بيانات المستخدم |

### 2. المنتجات (`/api/products`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | `/` | عرض جميع المنتجات مع الفلاتر |
| GET | `/{id}` | عرض منتج واحد |
| POST | `/` | إضافة منتج جديد |
| PUT | `/{id}` | تحديث منتج |
| DELETE | `/{id}` | حذف منتج |

**فلاتر البحث**: category_id, material, min_price, max_price, karat, jeweler_id

### 3. السلة (`/api/cart`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | `/` | عرض السلة |
| POST | `/add` | إضافة منتج للسلة |
| PUT | `/update/{item_id}` | تحديث الكمية |
| DELETE | `/remove/{item_id}` | إزالة منتج من السلة |
| DELETE | `/clear` | تفريغ السلة |

### 4. الطلبات (`/api/orders`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| POST | `/checkout` | تحويل السلة إلى طلب |
| GET | `/` | عرض طلبات المستخدم |
| GET | `/{id}` | عرض طلب واحد |
| PUT | `/{id}/status` | تحديث حالة الطلب |

### 5. الإدارة (`/api/admin`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| GET | `/dashboard` | إحصائيات لوحة التحكم |
| CRUD | `/jewelers` | إدارة الجواهريين |
| CRUD | `/categories` | إدارة الفئات |
| CRUD | `/payment-methods` | إدارة طرق الدفع |
| GET | `/orders` | عرض جميع الطلبات |
| GET/PUT | `/design-requests` | إدارة طلبات التصميم |

### 6. الذكاء الاصطناعي (`/api/ai`)
| Method | Endpoint | الوصف |
|--------|----------|-------|
| POST | `/generate-design` | توليد تصميم مجوهرات بالذكاء الاصطناعي |
| GET | `/my-designs` | عرض تصاميم المستخدم |
| GET | `/designs/{id}` | عرض تصميم واحد |
| POST | `/request-quote` | طلب عرض سعر من جواهري |
| GET | `/my-requests` | عرض طلبات المستخدم |

## ميزة تصميم المجوهرات بالذكاء الاصطناعي

### آلية العمل:
1. استقبال البيانات: `{type, color, shape, material, karat, gemstone_type, gemstone_color}`
2. بناء Prompt تفصيلي للتصميم
3. استدعاء Gemini API
4. حفظ الصورة في `/static/generated_designs/`
5. تخزين السجل في قاعدة البيانات
6. إرجاع رابط الصورة و ID التصميم

### مثال على الطلب:
```json
{
  "type": "Ring",
  "color": "Rose Gold",
  "shape": "Cushion",
  "material": "Gold",
  "karat": "18k",
  "gemstone_type": "Ruby",
  "gemstone_color": "Red"
}
```

## هيكل الملفات
```
backend/
├── main.py              # نقطة دخول FastAPI
├── database.py          # إعدادات قاعدة البيانات
├── seeder.py            # ملء قاعدة البيانات بالبيانات التجريبية
├── requirements.txt     # مكتبات Python
├── .env.example         # قالب متغيرات البيئة
├── models/
│   ├── __init__.py
│   └── models.py        # نماذج SQLAlchemy
├── schemas/
│   ├── __init__.py
│   ├── user.py          # Pydantic schemas للمستخدم
│   ├── jeweler.py       # Pydantic schemas للجواهري
│   ├── product.py       # Pydantic schemas للمنتج
│   ├── category.py      # Pydantic schemas للفئات
│   ├── cart.py          # Pydantic schemas للسلة
│   ├── order.py         # Pydantic schemas للطلبات
│   ├── payment.py       # Pydantic schemas للدفع
│   └── design.py        # Pydantic schemas للتصميم
├── routers/
│   ├── __init__.py
│   ├── auth.py          # مسارات المصادقة
│   ├── products.py      # مسارات المنتجات
│   ├── cart.py          # مسارات السلة
│   ├── orders.py        # مسارات الطلبات
│   ├── admin.py         # مسارات الإدارة
│   └── ai.py            # مسارات الذكاء الاصطناعي
├── utils/
│   ├── __init__.py
│   ├── auth.py          # أدوات JWT والتشفير
│   └── gemini.py        # تكامل Gemini API
└── static/
    ├── generated_designs/  # صور التصاميم المولدة
    └── qr_codes/           # صور QR للدفع
```

## البيانات التجريبية (seeder.py)
- 3 جواهريين (Admin)
- 5 مستخدمين
- 21 فئة (10 رئيسية + 11 فرعية)
- 2 طريقة دفع
- 10 منتجات واقعية مع صور

### بيانات الدخول التجريبية:
| Username | Password |
|----------|----------|
| john_doe | password123 |
| emma_wilson | password123 |
| mohammed_hassan | password123 |

## تعليمات التشغيل

### 1. إعداد قاعدة البيانات:
```bash
# تشغيل XAMPP وإنشاء قاعدة بيانات jewelry_db
```

### 2. تثبيت المكتبات:
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# تحديث GEMINI_API_KEY في .env
```

### 3. ملء البيانات:
```bash
python seeder.py
```

### 4. تشغيل السيرفر:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. الوثائق:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## ربط Frontend بـ Backend

### مثال على تسجيل الدخول:
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

### مثال على توليد تصميم:
```javascript
async function generateDesign(options) {
    const token = localStorage.getItem('token');
    const response = await fetch('http://localhost:8000/api/ai/generate-design', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(options)
    });
    return await response.json();
}
```

## الحالة الحالية
✅ تم الانتهاء من Backend بالكامل
- قاعدة البيانات مع 12 جدول
- 6 Routers مع جميع الـ Endpoints
- نظام مصادقة JWT
- تكامل Gemini API
- Seeder للبيانات التجريبية
- وثائق README.md
