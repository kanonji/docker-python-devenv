from contextlib import contextmanager
import datetime
import os
import string
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, scoped_session

host = os.getenv('MYSQL_HOST')
database = os.getenv('MYSQL_DATABASE')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database_url = f'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4'

Base: DeclarativeMeta = declarative_base()

engine = create_engine(database_url, echo=True)
scoped_session_obj = scoped_session(
    sessionmaker(
        autocommit=False, autoflush=True,
        bind=engine, expire_on_commit=False
    )
)
Base.query = scoped_session_obj.query_property()
@contextmanager
def transaction() -> scoped_session:
    session = scoped_session_obj()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

# class (Base):
#     __tablename__ = ''
