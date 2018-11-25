#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from models import db, Author, User, Book, Category
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techBooks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')  # Display all categories
def home():
    categories = Category.query.all()
    return render_template('home.html', categories=categories)


@app.route('/tech/<category>')  # Display items in the provided category
def showCategory(category):
    category = category.replace('-', ' ')
    cat = Category.query.filter_by(name=category).one()
    books = Book.query.filter_by(category_id=cat.id).all()
    return render_template('category.html', books=books)


@app.route('/new', methods=['GET', 'POST'])  # Add a new book (item)
def newBook():
    if request.method == 'POST':    
        author_id = create_author(request.form['authorFName'], request.form['authorLName'])
        category_id = get_category_id(request.form['category'])
        book = Book(title=request.form['title'],
                    author_id=author_id,
                    category_id=category_id,
                    publish_year=request.form['year'],
                    link=request.form['link'],
                    cover_url=request.form['coverUrl'],
                    summary=request.form['summary'],
                    isbn=request.form['isbn'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        categories = Category.query.all()
        return render_template('new.html', categories=categories)


@app.route('/tech/<category>/<title>')  # View details about a book (item)
def viewBook(title):
    return render_template('book.html')


@app.route('/tech/<category>/<title>/edit', methods=['GET', 'POST'])  # Edit a book
def editBook(title):
    return render_template('editBook.html')


@app.route('/tech/<category>/<title>/delete', methods=['GET', 'POST'])  # Delete a book
def deleteBook(title):
    return render_template('deleteBook.html')


def create_author(first_name, last_name, bio=None):
    author = Author(first_name=first_name, last_name=last_name, bio=bio)
    db.session.add(author)
    db.session.commit()
    return author.id

def get_category_id(name):
    category = Category.query.filter_by(name=name).one()
    return category.id

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
