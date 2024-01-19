from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URI = "postgresql+psycopg2://postgres:1111@localhost:3000/patients"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
