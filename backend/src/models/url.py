from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import TEXT, VARCHAR
from config.db import meta

urls = Table(
    'url_mapping', meta,
    Column('shortUrl', VARCHAR(32), primary_key=True),
    Column('longUrl', TEXT)
)
