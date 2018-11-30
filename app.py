#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Author, User, Book, Category
import datetime, json

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
    return render_template('category.html', books=books, category=category)


@app.route('/new', methods=['GET', 'POST'])  # Add a new book (item)
def newBook():
    if request.method == 'POST':  # TODO: Correct behavior when no aothor is entered                
        category_id = get_category_id(request.form['category'])      
        book = Book(title=request.form['title'],
                    category_id=category_id,
                    publish_year=request.form['year'],
                    link=request.form['link'],
                    cover_url=request.form['coverUrl'],
                    summary=request.form['summary'],
                    isbn=request.form['isbn'])
        if request.form['authorFName'] or request.form['authorLName']:
            create_author(book.id, request.form['authorFName'], request.form['authorLName'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        categories = Category.query.all()
        return render_template('new.html', categories=categories)


@app.route('/tech/<category>/<title>')  # View details about a book (item)
def viewBook(category, title):
    category = category.replace('-', ' ')
    title = title.replace('-', ' ')
    book = Book.query.filter_by(title=title).one()
    return render_template('book.html', book=book, category=category)


@app.route('/tech/<category>/<title>/edit', methods=['GET', 'POST'])  # Edit a book
def editBook(category, title):
    category = category.replace('-', ' ')
    title = title.replace('-', ' ')
    book = Book.query.filter_by(title=title).one()
    try:
        author = Author.query.filter_by(book_id=book.id).one()
    except:
        author = None
    categories = Category.query.all()
    if request.method == 'POST':
        if request.form['title'] != book.title:
            book.title = request.form['title']
        if get_category_id(request.form['category']) != book.category_id:
            book.category_id = get_category_id(request.form['category'])        
        if request.form['year'] != book.publish_year:
            book.publish_year = request.form['year']
        if request.form['link'] != book.link:
            book.link = request.form['link']
        if request.form['coverUrl'] != book.cover_url:
            book.cover_url = request.form['coverUrl']
        if request.form['summary'] != book.summary:
            book.summary = request.form['summary']
        if request.form['isbn'] != book.isbn:
            book.isbn = request.form['isbn']                
        if author and request.form['authorFName'] != author.first_name:
            author.first_name = request.form['authorFName']            
        if author and request.form['authorLName'] != author.last_name:
            author.last_name = request.form['authorLName']
        
        if author:
            db.session.add(author)
        db.session.add(book)      
        db.session.commit()        
        return redirect(url_for('viewBook', category=get_category_name(book.category_id), title=book.title).replace('%20', '-'))
    else:
        return render_template('editBook.html', book=book, book_category=category, categories=categories, author=author)


@app.route('/tech/<category>/<title>/delete', methods=['GET', 'POST'])  # Delete a book
def deleteBook(category, title):
    category = category.replace('-', ' ')
    title = title.replace('-', ' ')
    book = Book.query.filter_by(title=title).one()
    author = Author.query.filter_by(book_id=book.id).one()
    db.session.delete(author)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('showCategory', category=category).replace('%20', '-'))

@app.route('/tech/<category>/<title>/json')
def bookJSON(category, title):
    category = category.replace('-', ' ')
    title = title.replace('-', ' ')
    book = Book.query.filter_by(title=title).one()
    author = Author.query.filter_by(book_id=book.id).one()
    category = Category.query.filter_by(id=book.category_id).one()
    return jsonify(Book=book.serialize, Author=author.serialize, Category=category.serialize)

@app.route('/tech/<category>/json')
def categoryJSON(category):
    category = category.replace('-', ' ')
    category = Category.query.filter_by(name=category).one()
    books = Book.query.filter_by(category_id=category.id).all()
    booksJson = []
    for book in books:
        author = Author.query.filter_by(book_id=book.id).one()
        booksJson.append({'Book':book.serialize, 'Author':author.serialize, 'Category':category.serialize})
    return jsonify(Books=booksJson)



def create_author(book_id, first_name, last_name):
    author = Author(book_id=book_id, first_name=first_name, last_name=last_name)
    db.session.add(author)
    db.session.commit()


def get_category_id(name):
    category = Category.query.filter_by(name=name).one()
    return category.id

def get_category_name(id):
    category = Category.query.filter_by(id=id).one()
    return category.name

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
