import sqlite3, os, datetime, src.note

con = sqlite3.connect("dbnote")
cur = con.cursor()
cur.execute("pragma foreign_keys = ON")
cur.execute("""create table if not exists
notes(
noteid integer primary key autoincrement,
notets timestamp not null,
notetext text not null)""")
cur.execute("""create table if not exists
tags(
tagid integer,
tagtext text not null,
FOREIGN KEY(tagid) references notes(noteid))""")

n = src.note.Note("hello #t1 #t2")
n2 = src.note.Note("goodbye #t1 #t3")
n3 = src.note.Note("no tags")
def insert_note(note, id):
    cur.execute("insert into notes(notets, notetext) values(?, ?)",\
    (note.timestamp, note.text))
    for tag in note.tags:
        cur.execute("insert into tags(tagid, tagtext) values(?, ?)", (id, tag))
insert_note(n, 1)
insert_note(n2, 2)
insert_note(n3, 3)

def delete_note(id):
    cur.execute("delete from tags where tagid=?", (id,))
    cur.execute("delete from notes where noteid=?", (id,))
delete_note(1)
cur.execute("select tagid, tagtext from tags")
rows = cur.fetchall()
for r in rows:
    print("%d) %s" % (r[0], r[1]))

"""
cur.execute("select tagid, tagtext from tags")
rows = cur.fetchall()
for r in rows:
    print("%d) %s" % (r[0], r[1]))
cur.execute("select noteid, notetext from notes")
rows = cur.fetchall()
for r in rows:
    print("%d) %s" % (r[0], r[1]))
cur.execute("select tagid from tags where tagtext='t1'")
for row in cur.fetchall():
    cur.execute("select notetext from notes where noteid=?", (row[0],))
    print(cur.fetchone()[0])
    """


cur.close()
con.close()
