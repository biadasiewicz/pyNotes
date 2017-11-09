import datetime, re

class Note:
    def __init__(self, text, timestamp = datetime.datetime.now()):
        assert(type(timestamp) == datetime.datetime)
        self.timestamp = timestamp
        self.set_text(text)
        self.__num = 123

    def set_text(self, text):
        self.tags = set(re.findall(r"#(\w+)", text))
        self.text = text

    def is_tagged(self, tag):
        return tag in self.tags

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.text == other.text

    def __str__(self):
        ts = self.timestamp.strftime("%d/%m/%Y %H:%M")
        return "%s\n\t %s" % (ts, self.text)
