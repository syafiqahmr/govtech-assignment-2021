from sqlalchemy import create_engine, MetaData
import os

# retrieve db credentials
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")
url = os.getenv("DB_URL")
name = os.getenv("DB_NAME")


engineUrl = "mysql+pymysql://" + user + ":" + \
    password + "@" + url + ":" + port + "/" + name
# "mysql+pymysql://admin:321admin!@database-govtech-2021.ckrufll318v7.us-east-1.rds.amazonaws.com:3306/db"
engine = create_engine(engineUrl)
meta = MetaData()
conn = engine.connect()
