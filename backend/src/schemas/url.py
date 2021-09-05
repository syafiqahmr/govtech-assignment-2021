import pydantic as _pydantic


class _UrlBase(_pydantic.BaseModel):
    short_url: str
    long_url: str


class Url(_UrlBase):
    short_url: str
    long_url: str

    class Config:
        orm_mode = True
