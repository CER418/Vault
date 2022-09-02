import datetime


class Entry:
    def __init__(self, name, username, password, date=None, id=None):
        self.name = name
        self.username = username
        self.password = password
        self.date = date if date is not None else datetime.datetime.now().strftime("%e. %b %Y")
        self.id = id if id is not None else None

    def __repr__(self) -> str:
        return f"({self.name}, {self.username}, {self.password}, {self.date}, {self.id})"
