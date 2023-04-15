from functools import partial

from sqlalchemy import Column, Integer, String

from app.database import Base

ReqColumn = partial(Column, nullable=False)


class Item(Base):
    __tablename__ = 'items'
    nm_id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = ReqColumn(String, nullable=False)
    brand = Column(String)
    brand_id = Column(Integer)
    site_brand_id = Column(Integer)
    supplier_id = Column(Integer)
    sale = Column(Integer)
    price = Column(Integer)
    sale_price = Column(Integer)
    rating = Column(Integer)
    feedbacks = Column(Integer)
