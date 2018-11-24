from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)    
    tech_category = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.Date)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    link = db.Column(db.String)
    abstract = db.Column(db.String)

    author = db.relationship(Author)
