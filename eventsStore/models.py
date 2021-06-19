from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapper


class Events(Base):
    __tablename__ = 'events'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), unique=True)
    serveFeeAmount = Column('serviceFeeAmount', Integer)
    serviceFeeCurrency = Column('serviceFeeCurrency', String)

    def __init__(self, name=None, serveFeeAmount=None, serviceFeeCurrency=None):
        self.name = name
        self.serveFeeAmount = serveFeeAmount
        self.serviceFeeCurrency = serviceFeeCurrency


class Products(Base):
    __tablename__ = 'products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50))
    eventId = Column('eventId', Integer, ForeignKey("events.id"))

    def __init__(self, name=None, eventId=None):
        self.name = name
        self.eventId = eventId
