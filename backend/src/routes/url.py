from fastapi import APIRouter
#from config.db import conn
#from models.index import urls
from schemas.index import Url
from util.shorten import shorten_url
import sqlalchemy.orm as _orm
import fastapi as _fastapi
import util.services as _services

url = APIRouter()
_services.create_database()

# @url.get("/")
# async def read_data():
#     return conn.execute(urls.select()).fetchall()


# @url.get("/{shortUrl}")
# async def read_data(shortUrl: str):
#     return conn.execute(urls.select().where(urls.c.shortUrl == shortUrl)).fetchall()


# @url.post("/")
# async def write_data(url: Url):
#     conn.execute(urls.insert().values(
#         shortUrl=url.shortUrl,
#         longUrl=url.longUrl
#     ))
#     return conn.execute(urls.select()).fetchall()


@url.get("/url/{longUrl}")
def write_data(longUrl: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return shorten_url(longUrl, db)
