from fastapi import APIRouter
from config.db import conn
from models.index import urls
from schemas.index import Url

url = APIRouter()


@url.get("/")
async def read_data():
    return conn.execute(urls.select()).fetchall()


@url.get("/{shortUrl}")
async def read_data(shortUrl: str):
    return conn.execute(urls.select().where(urls.c.shortUrl == shortUrl)).fetchall()


@url.post("/")
async def write_data(url: Url):
    conn.execute(urls.insert().values(
        shortUrl=url.shortUrl,
        longUrl=url.longUrl
    ))
    return conn.execute(urls.select()).fetchall()
