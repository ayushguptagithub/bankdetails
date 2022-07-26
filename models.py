#use to create table in database 

from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'bankdetails'
    bank_id= Column(Integer, primary_key=True)
    user_id = Column(Integer)
    acc_no= Column(String(256))
    ifcr_no = Column(String(256))
    micr_no = Column(String(256))
    swift = Column(String(256))


    