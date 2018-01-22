import note
from datetime import datetime

text = "hello #tag1 #tag1 #tag2 #tag_3"

def test_tags():
    n = note.Note(text, datetime.now())
    assert(n.is_tagged('tag1'))
    assert(n.is_tagged('tag2'))
    assert(n.is_tagged('tag_3'))

def test_equal():
    ts = datetime.now()
    n1 = note.Note(text, ts)
    n2 = note.Note(text, ts)
    assert(n1 == n2)
