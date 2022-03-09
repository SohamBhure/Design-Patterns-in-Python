from random import randint, random


class Database:

    _instance = None

    def __init__(self) -> None:
        self.id = randint(1,100)
        print(str(self.id) + ": " + "New DB")

    def __new__(cls, *args, **kwargs) -> None:
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            return cls._instance


db1 = Database()
db2 = Database()

print(db1==db2)