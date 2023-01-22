import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request, redirect, url_for, flash
from models import Book


app = Flask(__name__)
app.config['SECRET KEY'] = '123740981237401732904'

links = [
    {'name': 'Главная', 'url':'/'},
    {'name': 'Каталог', 'url': '/books'},
    {'name': 'Добавить', 'url': '/add'},
    {'name': 'Редактировать', 'url': '/update'}
]

@app.route('/')
def index():
    books = Book.select()
    return render_template('index.html', books=books, links=links)

@app.route('/books', methods=['GET', 'POST'])
def books():
    book = Book.select()
    # books = Book.select()
    return render_template('books.html', links=links, book = book)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        if not Book.select().where(Book.title==title):
            author = request.form['author']
            if title is not None:
                year = request.form['year']
                # if isinstance(year, int):
                genre = request.form['genre']
                description = request.form['description']
                img = request.form['img']
                Book.create(title=title, author=author, year=year, genre=genre, description=description, img=img)
                        # flash(f'"{title}" сохранен')
                flash(f'Сохранено')
                # else:
                #     flash(f'Ошибка ввода')
            else:
                flash('Не введено произведение')
        else:
            flash(f'"{title}" есть в каталоге ')
            return redirect('books')
    return render_template('add.html', books=Book, links=links)

@app.route('/home')
def review():
    title = Book.select
    return render_template('about.html',title=title)

@app.route('/update/<int:id>',methods=["POST","GET"])
def update(id):
    books_upd = Book.get_by_id(id)
    if request.method == 'POST':
        title = request.form['title']
        title_upd = request.form['title_upd']
        author = request.form['author']
        author_upd = request.form['author_upd']
        year = request.form['year']
        year_upd = request.form['year_upd']
        genre = request.form['genre']
        genre_upd = request.form['genre_upd']
        description = request.form['description']
        description_upd = request.form['description_upd']
        img = request.form['img']
        img_upd = request.form['img_upd']
        query=Book.update(title=title_upd, author=author_upd, year=year_upd, genre=genre_upd, description=description_upd, img=img_upd).\
            where(Book.title == title_upd)
        query.execute()
        return redirect(url_for('books'))
    return render_template('update.html', books_upd=books_upd, links=links)

@app.route('/delete/<int:id>',methods = ['POST','GET'])
def delete_book(id):
    Book.delete_by_id(id)
    redirect('/')
    return redirect(url_for('index'))
#
@app.route('/search',methods = ['POST','GET'])
def seacrh_book(id):
    if request.method=='POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        if not seacrh_book.select().where(Book.title==title):
            Book.search(id=id,title=title,author = author,genre=genre)
            print('работает')
    redirect('search')

    return redirect(url_for('books'))

#
#
# @app.route('/filter/<int:id>',methods =['POST','GET'])
# def filter_book(id):
#     if not filter_book.select().where(Book.title=title):
#         Book.filter(id=id,title=title,avtor = avtor,age=age,year=year,edition=edition,janre=janre)

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)