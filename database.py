#important code 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creates database engine
#engine = create_engine('sqlite:///item.db')
engine = create_engine('postgresql://postgres:root@localhost:5432/postgres')
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False) #session for db
#postgresql://postgres:password@localhost:5432/demo