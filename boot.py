"""
The Bestory Project
"""

import os
import urllib.parse

from thebestory.application import app
from thebestory import config


def boot():
    port = os.environ.get("PORT")

    if port is None:
        raise ValueError("App PORT must be provided by environment")

    config.app.PORT = port

    url = os.environ.get("DATABASE_URL")
    seed = os.environ.get("SEED")

    if url is None:
        raise ValueError("Database URL must be provided by environment")

    parsed = urllib.parse.urlparse(url)

    app.db.HOST = parsed.hostname
    app.db.PORT = parsed.port
    app.db.USER = parsed.username
    app.db.PASSWORD = parsed.password
    app.db.DATABASE = parsed.path[1:]

    app.db.SEED = True if seed == "True" else False

    app.run()


if __name__ == "__main__":
    boot()
