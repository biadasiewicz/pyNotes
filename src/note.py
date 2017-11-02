import datetime, re

class Note:
    def __init__(self, text, timestamp = datetime.datetime.now()):
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
