from peewee import *

db = SqliteDatabase('db.db')

class Person(Model):
    userid = IntegerField()
    state = IntegerField()
    data = CharField()
    date = DateTimeField()

    class Meta:
        database = db