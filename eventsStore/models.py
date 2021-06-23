from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from eventsStore import db

DEFAULT_CURRENCY = "EURO"

class Events(db.Model):
    __tablename__ = 'events'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), unique=True)
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String, default=DEFAULT_CURRENCY)
    products = relationship("Products",
                            back_populates='event',
                            cascade='delete')


class Products(db.Model):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    service_fee_amount = Column('service_fee_amount', Integer)
    service_fee_currency = Column('service_fee_currency', String)
    event_id = Column(Integer, ForeignKey('events.id'))
    event = relationship("Events",
                         back_populates='products')
