from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.brands import router as brands_router
from app.db.base import Base
from app.db.sessions import SessionLocal, engine
from app.models.brand import Brand
from app.models import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 IMPORTANT: create tables
Base.metadata.create_all(bind=engine)


def seed_default_brands() -> None:
    db = SessionLocal()
    try:
        defaults = [
            {"name": "Heritage", "discount_percentage": 20.0},
            {"name": "Kwality Walls", "discount_percentage": 16.0},
        ]

        for brand_data in defaults:
            existing = db.query(Brand).filter(Brand.name == brand_data["name"]).first()
            if existing is None:
                db.add(Brand(**brand_data))

        db.commit()
    finally:
        db.close()


seed_default_brands()

app.include_router(brands_router)

@app.get("/")
def root():
    return {"message": "Backend running perfectly!"}