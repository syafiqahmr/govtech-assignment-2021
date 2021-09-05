import sqlalchemy.orm as _orm
import models.index as _models
import schemas.index as _schemas
import config.db as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_url(db: _orm.Session, url: _schemas.Url):
    db_url = _models.Url(short_url=url.short_url, long_url=url.long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def count_url_by_shorturl(db: _orm.Session, short_url):
    return db.query(_models.Url).filter(_models.Url.short_url == short_url).count()
