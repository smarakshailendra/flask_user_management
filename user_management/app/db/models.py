from sqlalchemy import Column, Integer, String, Table, MetaData, Boolean
from sqlalchemy import create_engine

from config import sqlalchemy_conn_string
engine = create_engine(sqlalchemy_conn_string)
metadata = MetaData(engine)

auth_table = Table('auth', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('username', String(254)),
                   Column('role', String(254)),
                   Column('auth_status', Boolean),
                   Column('password', String(254)))

if not engine.dialect.has_table(engine, "auth"):
    metadata.create_all()