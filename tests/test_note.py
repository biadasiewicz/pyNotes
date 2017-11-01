import note

n = note.Note("hello #tag1 #tag1 #tag2 #tag_3")

def test_tags():
    assert(n.is_tagged('tag1'))
    assert(n.is_tagged('tag2'))
    assert(n.is_tagged('tag_3'))
