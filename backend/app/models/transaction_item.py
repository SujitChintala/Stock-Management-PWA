from sqlalchemy import Column, Integer, Float, ForeignKey
from app.db.base import Base

class TransactionItem(Base):
    __tablename__ = "transaction_items"

    id = Column(Integer, primary_key=True, index=True)

    transaction_id = Column(Integer, ForeignKey("transactions.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    mrp = Column(Float)
    quantity = Column(Integer)

    item_total = Column(Float)
    discount = Column(Float)
    net_price = Column(Float)