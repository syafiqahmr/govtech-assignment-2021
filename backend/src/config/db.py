import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os

# retrieve db credentials
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
url = os.getenv("DB_URL")
name = os.getenv("DB_NAME")


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" + user + ":" + \
    password + "@" + url + ":" + port + "/" + name
# "mysql+pymysql://admin:321admin!@database-govtech-2021.ckrufll318v7.us-east-1.rds.amazonaws.com:3306/db"

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
