from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import sqlalchemy_conn_string

Base = declarative_base()


def create_engine_sqlite3(conn_string):
    engine = create_engine(conn_string, echo=True)
    return engine


def create_session():
    engine = create_engine_sqlite3(sqlalchemy_conn_string)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def register_user(table_obj, username, password, role, auth_status=False):
    engine = create_engine_sqlite3(sqlalchemy_conn_string)
    stmt = table_obj.insert().values(username=username, password=password, role=role, auth_status=auth_status)
    conn = engine.connect()
    conn.execute(stmt)
