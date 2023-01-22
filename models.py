from peewee import *

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('books.db')

class Book(BaseModel):
    id = PrimaryKeyField(null=True)
    title = CharField(max_length=100)
    author = CharField(max_length=50)
    year = IntegerField()
    genre = CharField(max_length=50)
    description = TextField()
    img = CharField(max_length=200)

    class Meta:
        db_table = 'book'

if __name__ == '__main__':
    Book.create_table()