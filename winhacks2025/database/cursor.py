import sqlite3

from flask import g

DATABASE = "recipes.db"


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_cursor():
    cur = getattr(g, "_cursor", None)
    if cur is None:
        cur = g._cursor = get_db().cursor()
    return cur
