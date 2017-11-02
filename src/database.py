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
        id = self.max_id()
        for tag in n.tags:
            self.cur.execute("insert into tags(tagid, tagtext) values(?, ?)",\
                (id, tag))
    def delete_note(self, id):
        self.cur.execute("delete from tags where tagid=?", (id,))
        self.cur.execute("delete from notes where noteid=?", (id,))
    def select_date_range(self, a, b):
        self.cur.execute("""select noteid, notets notetext from notes
            where notets >= (?) and notets <= (?)
            order by notets asc""", (a, b,))
        return self.cur.fetchall()
    def count(self):
        self.cur.execute("select noteid from notes")
        return len(self.cur.fetchall())
    def max_id(self):
        self.cur.execute("select max(noteid) from notes")
        return self.cur.fetchone()[0]
    def close(self):
        self.cur.close()
        self.con.close()
