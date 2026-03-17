from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)