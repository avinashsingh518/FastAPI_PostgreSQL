from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost:5432/bookstore"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #help to connect with database

'''help to perform actions in database,autocommit=False,autoflush=False means until/unless you not specifying to any changes in database,
 the changes will not be reflect in database...bind=engine means to binding the engine with session'''
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base() #help to create the table

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)