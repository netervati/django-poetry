"""
Settings for database type and credentials.

Sqlite is used for development purposes only.
"""

from dotenv import load_dotenv
import os


load_dotenv(".env")


def settings():
    db = os.getenv("DJANGO_DB")

    if db == "postgresql":
        return {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRESQL_DB_NAME"),
            "USER": os.getenv("POSTGRESQL_DB_USER"),
            "PASSWORD": os.getenv("POSTGRESQL_DB_PASS"),
            "HOST": os.getenv("POSTGRESQL_DB_HOST"),
            "PORT": os.getenv("POSTGRESQL_DB_PORT"),
        }
    elif db == "sqlite3":
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        return {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": f"{BASE_DIR}/db.sqlite3",
        }
