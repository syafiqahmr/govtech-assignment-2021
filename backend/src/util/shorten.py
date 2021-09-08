import hashlib
import sqlalchemy.orm as _orm
import util.services as _services
import random


SHORT_URL_LENGTH = 6


def shorten_url(long_url: str, db: _orm.Session):
    # random counter to prevent same long url generating the same hash
    counter = random.randint(0, 1000)
    long_url_counter = long_url + str(counter)

    # to generate short_url:
    #   use md5 hashing algorithm
    #   take the first x characters
    short_url = hashlib.md5(long_url_counter.encode()).hexdigest()[
        :SHORT_URL_LENGTH]

    # rehash if resulting short url already exist
    while(not verify_unique_short_url(short_url, db)):
        counter += 1
        long_url_counter = long_url + str(counter)
        short_url = hashlib.md5(long_url_counter.encode()).hexdigest()[
            :SHORT_URL_LENGTH]

    return short_url


def verify_unique_short_url(short_url: str, db: _orm.Session):
    # verify short url is unique
    return _services.count_url_by_short_url(db, short_url) == 0
