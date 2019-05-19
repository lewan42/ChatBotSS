from peewee import *

db = SqliteDatabase('db.db')

class Person(Model):
    userid = IntegerField()
    state = CharField()
    data = CharField()
    date = DateTimeField()

    class Meta:
        database = db