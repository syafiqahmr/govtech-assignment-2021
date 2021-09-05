import util.shorten as _shorten
import sqlalchemy.orm as _orm
import fastapi as _fastapi
import util.services as _services
import schemas.index as _schemas

url = _fastapi.APIRouter()
_services.create_database()


@url.post("/url", response_model=_schemas.Url)
def write_data(post: _schemas.UrlCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    short_url = _shorten.shorten_url(post.long_url, db)

    url_schema = _schemas.Url(short_url=short_url, long_url=post.long_url)
    return _services.create_url(db, url_schema)
