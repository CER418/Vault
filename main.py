from tinydb import TinyDB, Query
import bcrypt

db = TinyDB(':memory:')

User = Query()


def insert():
    db.insert()


if __name__ == '__main__':
    print(db.all())
