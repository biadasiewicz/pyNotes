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
    def insert_note(self, n):
        self.cur.execute("insert into notes(notets, notetext) values(?, ?)",\
            (n.timestamp, n.text))
        self.cur.execute("select max(noteid) from notes")
        id = self.cur.fetchone()[0]
        for tag in n.tags:
            self.cur.execute("insert into tags(tagid, tagtext) values(?, ?)",\
                (id, tag))

    def close(self):
        self.cur.close()
        self.con.close()
