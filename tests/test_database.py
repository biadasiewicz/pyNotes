from database import Database
from os import remove
import sqlite3

def test_init():
    db = Database(":memory:")
    db.close()
    assert(True)
def test_reopen():
    path = "db"
    db = Database(path)
    db.close()
    db = Database(path)
    db.close()
    remove(path)
    assert(True)
