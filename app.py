#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Book, Category

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
        pass
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


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
