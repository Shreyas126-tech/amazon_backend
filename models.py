from db import Base
from sqlalchemy import Column, Integer, String, Boolean

class user(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    address = Column(String)
    phone = Column(Integer)
    alt_phone = Column(Integer)
    isprime = Column(Boolean)