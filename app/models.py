from functools import partial

from sqlalchemy import (Column, ForeignKey, Integer, String, Table,
                        UniqueConstraint)
from sqlalchemy.orm import relationship

from app.database import Base

ReqColumn = partial(Column, nullable=False)

association_table = Table(
    'association_table',
    Base.metadata,
    Column('items_id', ForeignKey('items.nm_id',
           onupdate='CASCADE', ondelete='CASCADE')),
    Column('colors_id', ForeignKey('colors.id',
           onupdate='CASCADE', ondelete='CASCADE')),
    UniqueConstraint('items_id', 'colors_id', name='items_colors'),
)


class Item(Base):
    __tablename__ = 'items'
    nm_id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = ReqColumn(String, nullable=False)
    brand = ReqColumn(String)
    brand_id = ReqColumn(Integer)
    site_brand_id = ReqColumn(Integer)
    supplier_id = ReqColumn(Integer)
    sale = ReqColumn(Integer)
    price = ReqColumn(Integer)
    sale_price = ReqColumn(Integer)
    rating = ReqColumn(Integer)
    feedbacks = ReqColumn(Integer)
    colors = relationship('Color', secondary=association_table,
                          back_populates='items')


class Color(Base):
    __tablename__ = 'colors'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = ReqColumn(String, nullable=False)
    items = relationship('Item', secondary=association_table,
                         back_populates='colors')
