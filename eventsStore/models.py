from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper


events = Table('events', metadata,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('name', String(50), unique=True),
               Column('serviceFeeAmount', Integer),
               Column('serviceFeeCurrency', String))

