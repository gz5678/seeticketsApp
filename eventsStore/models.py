from sqlalchemy import Column, Integer, String, ForeignKey
from eventsStore.db import Base


class Events(Base):
    __tablename__ = 'events'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), unique=True)
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String)

    def __init__(self, name=None, service_fee_amount=None, service_fee_currency=None):
        self.name = name
        self.service_fee_amount = service_fee_amount
        self.service_fee_currency = service_fee_currency


class Products(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String)

    def __init__(self, name=None, service_fee_amount=None, service_fee_currency=None):
        self.name = name
        self.service_fee_amount = service_fee_amount
        self.service_fee_currency = service_fee_currency


class ProductsToEvents(Base):
    __tablename__ = 'productsToEvents'
    event_id = Column('event_id', Integer, ForeignKey(Events.id))
    product_id = Column('product_id', Integer, ForeignKey(Products.id))

    def __init__(self, event_id=None, product_id=None):
        self.event_id = event_id
        self.product_id = product_id
