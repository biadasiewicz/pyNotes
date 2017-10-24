import time, re
import sqlite3

class note:
    def __init__(self, text, timestamp = time.time()):
        self.timestamp = timestamp
        self.set_text(text)
    def set_text(self, text):
        self.tags = set(re.findall(r"#(\w+)", text))
        self.text = text
    def is_tagged(self, tag):
        return tag in self.tags
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return "%f;%s" % (self.timestamp, self.text)
def convert_note(s):
    m = list(map(str, s.split(b";")))
    assert(len(m) == 2)
    n = note(float(m[0]))
    n.set_text(m[1])
    return n

n = note("hello #tag1 #tag1 #tag2 #tag_3")
assert(n.is_tagged('tag1'))
assert(n.is_tagged('tag2'))
assert(n.is_tagged('tag_3'))


