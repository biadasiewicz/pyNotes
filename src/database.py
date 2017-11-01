import note, sqlite3

class Database:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()
        self.cur.execute("pragma foreign_keys = ON")
        self.cur.execute("""create table if not exists
            notes(
            noteid integer primary key autoincrement,
            notets timestamp not null,
            notetext text not null)""")
        self.cur.execute("""create table if not exists
            tags(
            tagid integer,
            tagtext text not null,
            FOREIGN KEY(tagid) references notes(noteid))""")

    def close(self):
        self.cur.close()
        self.con.close()
