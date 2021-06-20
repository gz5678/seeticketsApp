from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from eventsStore import db


association_table = Table('association', db.Model.metadata,
                          Column('event_id', Integer, ForeignKey("events.id")),
                          Column('product_id', Integer, ForeignKey("products.id")))


class Events(db.Model):
    __tablename__ = 'events'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), unique=True)
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String)
    children = relationship("Products",
                            secondary=association_table)

    def __init__(self, name=None, service_fee_amount=None, service_fee_currency=None):
        self.name = name
        self.service_fee_amount = service_fee_amount
        self.service_fee_currency = service_fee_currency


class Products(db.Model):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String)

    def __init__(self, name=None, service_fee_amount=None, service_fee_currency=None):
        self.name = name
        self.service_fee_amount = service_fee_amount
        self.service_fee_currency = service_fee_currency
