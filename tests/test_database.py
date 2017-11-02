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

def test_delete():
    db = Database(":memory:")
    n = Note("hello, world #t1 #t2 #t1")
    n2 = Note("goodbye #t1 #3")
    db.insert_note(n)
    db.insert_note(n2)
    assert(db.count() == 2)
    db.delete_note(1)
    assert(db.count() == 1)
    db.delete_note(2)
    assert(db.count() == 0)
    db.close()

def test_select_date_range():
    db = Database(":memory:")
    from datetime import datetime, timedelta
    d1 = datetime.now()
    d2 = datetime.now() + timedelta(days=1)
    d3 = datetime.now() + timedelta(days=2)
    n1 = Note("a", d3)
    n2 = Note("b", d1)
    n3 = Note("c", d2)
    db.insert_note(n1)
    db.insert_note(n2)
    db.insert_note(n3)
    s1 = db.select_date_range(d1, d3)
    assert(db.count() == 3)
    assert(len(s1) == 3)
    s2 = db.select_date_range(d1, d2)
    assert(len(s2) == 2)
