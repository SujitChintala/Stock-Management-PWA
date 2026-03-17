from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from datetime import datetime
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    stock_taken_at = Column(DateTime, default=datetime.utcnow)

    total_amount = Column(Float)
    online_amount = Column(Float)
    final_amount = Column(Float)
    amount_paid = Column(Float)
    remaining_amount = Column(Float)