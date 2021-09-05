from pydantic import BaseModel


class Url(BaseModel):
    shortUrl: str
    longUrl: str
