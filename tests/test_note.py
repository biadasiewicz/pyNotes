import note

n = note.Note("hello #tag1 #tag1 #tag2 #tag_3")
def test_tags():
    assert(n.is_tagged('tag1'))
    assert(n.is_tagged('tag2'))
    assert(n.is_tagged('tag_3'))

def test_database():
    import sqlite3
    sqlite3.register_adapter(note.Note, note.adapt_note)
    sqlite3.register_converter("note", note.convert_note)
    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
    cur = con.cursor()
    cur.execute("create table test(n note)")
    cur.execute("insert into test(n) values (?)", (n,))
    cur.execute("select n from test")
    n2 = cur.fetchone()[0]
    assert(n == n2)
    cur.close()
    con.close()
