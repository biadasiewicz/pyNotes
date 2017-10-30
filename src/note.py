import time, re

class Note:
    def __init__(self, text, timestamp = time.time()):
        self.timestamp = timestamp
        self.set_text(text)
    def set_text(self, text):
        self.tags = set(re.findall(r"#(\w+)", text))
        self.text = text
    def is_tagged(self, tag):
        return tag in self.tags
    def __eq__(self, other):
        import math
        return math.isclose(self.timestamp, other.timestamp) and self.text == other.text
    def __str__(self):
        return "%f: %s" % (self.timestamp, self.text)
    def __repr__(self):
        return "(%f;%s)" % (self.timestamp, self.text)

def adapt_note(n):
    return ("%f;%s" % (n.timestamp, n.text)).encode('ascii')
def convert_note(s):
    loaded = list(map(str, s.split(b";")))
    assert(len(loaded) == 2)
    ts = float(loaded[0][2:len(loaded[0]) - 1])
    t = loaded[1][2:len(loaded[1]) - 1]
    n = Note(t, ts)
    return n

