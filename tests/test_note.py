import note, datetime

text = "hello #tag1 #tag1 #tag2 #tag_3"

def test_tags():
    n = note.Note(text)
    assert(n.is_tagged('tag1'))
    assert(n.is_tagged('tag2'))
    assert(n.is_tagged('tag_3'))

def test_equal():
    ts = datetime.datetime.now()
    n1 = note.Note(text, ts)
    n2 = note.Note(text, ts)
    print(n2)
    assert(n1 != n2)
