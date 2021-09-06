import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os as _os

# retrieve db credentials
user = _os.getenv("DB_USER")
password = _os.getenv("DB_PASSWORD")
port = _os.getenv("DB_PORT")
url = _os.getenv("DB_URL")
name = _os.getenv("DB_NAME")


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://" + user + ":" + \
    password + "@" + url + ":" + port + "/" + name

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = _orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
