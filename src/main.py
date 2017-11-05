import os, argparse, note, database

parser = argparse.ArgumentParser(
    prog="notes",
    description="command line application to write tagged notes")
parser.add_argument("action", type=str, help="main action to perform",
    choices=["write", "read", "delete"])
parser.add_argument("-d", "--date", type=str, help="timestamp of note")
parser.add_argument("-t", "--text", type=str, help="text of note")
parser.add_argument("--tag", type=str, help="read notes tagged with")
parser.add_argument("--id", type=int, help="note ID")
parser.add_argument("-v", "--verbose", action="count",
    help="verbose output", default=0)
parser.add_argument("--path", help="application path")
args = parser.parse_args()

path = ""
if args.path:
    path = args.path
else:
    path = os.path.join(os.environ["HOME"])
    path = os.path.join(path, ".pynotes")

if not os.path.exists(path):
    os.makedirs(path)
path = os.path.join(path, "db")

db = database.Database(path)
if args.action == "write":
    if args.text:
        db.insert_note(note.Note(args.text))
    else:
        notes = []
        while True:
            try:
                text = input("notes >>> ")
                notes.append(note.Note(text))
            except EOFError:
                break
        for n in notes:
            db.insert_note(n)
elif args.action == "read":
    notes = None
    if args.tag:
        notes = db.select_tag(args.tag)
    else:
        notes = db.select_all()
    for n in notes:
        print("%d) %s" % (n[0], n[1]))
elif args.action == "delete":
    if args.id:
        db.delete_note(args.id)
    else:
        print("error: --id option missing")
db.close()
