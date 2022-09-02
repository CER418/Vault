from typing import List
from tinydb import TinyDB, where

db = TinyDB('db.json')


def insert_entry(entry: entry):
    count = db.__len__() + 1
    print(count)
    entry.id = count if count else 1
    db.insert({'site': entry.name, 'username': entry.username, 'password': entry.password, 'date': entry.date,
               'id': entry.id})


def remove_entry(id):
    db.remove(where('id') == id)
    for pos in range(id + 1, db.__len__()):
        change_id(pos, pos - 1, False)


def change_id(old_id: int, new_id: int, commit=True):
    if commit:
        pass


def update_entry(id, name, username, password):
    print(db.update(where(id), name, username, password))


def get_all_entrys() -> List[entry]:
    results = db.all()
    entrys = []
    for result in results:
        entrys.append(entry(*result.values()))
    return entrys


def show():
    print(db.all())
