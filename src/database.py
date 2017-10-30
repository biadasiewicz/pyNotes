import note, sqlite3

class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path, detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists notes(n Note)")
    def close(self):
        self.cur.close()
        self.con.close()
