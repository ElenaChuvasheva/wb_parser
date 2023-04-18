import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_NAME = os.getenv('DB_NAME', 'parser_db')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:'
    f'{DB_PORT}/{DB_NAME}')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
#SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
#engine = create_engine(SQLALCHEMY_DATABASE_URL,
#                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
