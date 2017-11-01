from database import Database
from os import remove
import sqlite3
from note import Note

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

def test_insert():
    db = Database(":memory:")
    n = Note("hello, world #t1 #t2 #t1")
    db.insert_note(n)
    assert(db.count() == 1)
    db.close()
