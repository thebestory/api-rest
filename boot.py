"""
The Bestory Project
"""

import os
import urllib.parse

from thebestory.application import app
from thebestory.config import db


def boot():
    db_url = os.environ.get('DATABASE_URL')

    if db_url is None:
        raise ValueError("Database URL must be provided by environment")

    db_parsed_url = urllib.parse.urlparse(db_url)

    db.HOST = db_parsed_url.hostname
    db.PORT = db_parsed_url.port
    db.USER = db_parsed_url.username
    db.PASSWORD = db_parsed_url.password
    db.DATABASE = db_parsed_url.path[1:]

    db.SEED = True

    app.run()


if __name__ == "__main__":
    boot()
