from database import Base
from sqlalchemy import Column,Integer,Boolean,String



class Person(Base):
    __tablename__='persons'
    name=Column(String)
    id=Column(Integer,primary_key=True)

