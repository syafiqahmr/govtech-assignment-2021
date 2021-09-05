import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import config.db as _database


class Url(_database.Base):
    __tablename__ = "url_mapping"
    short_url = _sql.Column('shortUrl', _sql.VARCHAR(32),
                            primary_key=True, unique=True)
    long_url = _sql.Column('longUrl', _sql.TEXT)

# urls = Table(
#     'url_mapping', meta,
#     Column('shortUrl', VARCHAR(32), primary_key=True),
#     Column('longUrl', TEXT)
# )
