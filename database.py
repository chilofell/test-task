# import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# подключение к бд
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db"
# DATABASE_URL = "sqlite:///./sql_app6.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
