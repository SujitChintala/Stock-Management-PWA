from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.db.base import Base

class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String)
    active = Column(Boolean, default=True)

    primary_brand_id = Column(Integer, ForeignKey("brands.id"))