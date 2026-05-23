from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .config import settings
from .database import init_db
from .routes import products_router, categories_router, cart_router
import os

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs(settings.static_dir, exist_ok=True)
os.makedirs(settings.images_dir, exist_ok=True)

app.mount("/static", StaticFiles(directory=settings.static_dir), name="static")

app.include_router(products_router)
app.include_router(categories_router)
app.include_router(cart_router)


@app.on_event("startup")
def on_startup():
    init_db()
    _seed_if_empty()


def _seed_if_empty():
    """Заполняет БД тестовыми данными если она пустая (нужно при каждом рестарте на Render)"""
    from .database import SessionLocal
    from .models.category import Category
    from .models.product import Product

    db = SessionLocal()
    try:
        if db.query(Category).count() == 0:
            print("БД пустая — запускаем seed...")
            _run_seed(db)
            print("Seed выполнен успешно!")
        else:
            print(f"БД уже содержит данные, seed пропущен")
    except Exception as e:
        print(f"Ошибка seed: {e}")
    finally:
        db.close()


def _run_seed(db):
    from .models.category import Category
    from .models.product import Product

    categories_data = [
        {"name": "Electronics", "slug": "electronics"},
        {"name": "Clothing", "slug": "clothing"},
        {"name": "Books", "slug": "books"},
        {"name": "Home & Garden", "slug": "home-garden"},
    ]
    cats = {}
    for c in categories_data:
        obj = Category(**c)
        db.add(obj)
        db.flush()
        cats[c["slug"]] = obj

    products_data = [
        {
            "name": "Wireless Headphones",
            "description": "Premium noise-cancelling headphones",
            "price": 299.99,
            "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
            "category_slug": "electronics",
        },
        {
            "name": "Smart Watch Pro",
            "description": "Feature-rich smartwatch",
            "price": 399.99,
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
            "category_slug": "electronics",
        },
        {
            "name": "Laptop Stand",
            "description": "Ergonomic aluminum laptop stand",
            "price": 49.99,
            "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400",
            "category_slug": "electronics",
        },
        {
            "name": "Wireless Mouse",
            "description": "Silent ergonomic mouse",
            "price": 39.99,
            "image_url": "https://images.unsplash.com/photo-1527814050087-3793815479db?w=400",
            "category_slug": "electronics",
        },
        {
            "name": "Leather Jacket",
            "description": "Classic black leather jacket",
            "price": 199.99,
            "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400",
            "category_slug": "clothing",
        },
        {
            "name": "Running Shoes",
            "description": "Lightweight performance shoes",
            "price": 129.99,
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
            "category_slug": "clothing",
        },
        {
            "name": "Cotton T-Shirt",
            "description": "Premium cotton t-shirt",
            "price": 29.99,
            "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
            "category_slug": "clothing",
        },
        {
            "name": "The Clean Coder",
            "description": "A code of conduct for professional programmers",
            "price": 34.99,
            "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400",
            "category_slug": "books",
        },
        {
            "name": "Design Patterns",
            "description": "Elements of reusable object-oriented software",
            "price": 44.99,
            "image_url": "https://images.unsplash.com/photo-1589998059171-988d887df646?w=400",
            "category_slug": "books",
        },
        {
            "name": "Coffee Maker",
            "description": "Programmable 12-cup coffee maker",
            "price": 79.99,
            "image_url": "https://images.unsplash.com/photo-1520970014086-2208d157c9e2?w=400",
            "category_slug": "home-garden",
        },
        {
            "name": "Plant Pot Set",
            "description": "Set of 3 ceramic plant pots",
            "price": 24.99,
            "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400",
            "category_slug": "home-garden",
        },
        {
            "name": "Smart Speaker",
            "description": "Voice-controlled smart speaker",
            "price": 89.99,
            "image_url": "https://images.unsplash.com/photo-1543512214-318c7553f230?w=400",
            "category_slug": "electronics",
        },
        {
            "name": "Yoga Mat",
            "description": "Non-slip exercise yoga mat",
            "price": 35.99,
            "image_url": "https://images.unsplash.com/photo-1601925228508-2c53d0ef5e7f?w=400",
            "category_slug": "home-garden",
        },
    ]

    for p in products_data:
        slug = p.pop("category_slug")
        product = Product(**p, category_id=cats[slug].id)
        db.add(product)

    db.commit()


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/debug")
def debug():
    from .database import SessionLocal
    from .models.product import Product
    import os

    db = SessionLocal()
    count = db.query(Product).count()
    db.close()
    return {
        "products_count": count,
        "cwd": os.getcwd(),
        "db_url": settings.database_url,
    }
