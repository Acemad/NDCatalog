from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String, nullable=False)
    picture = db.Column(db.String)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description
        }


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    summary = db.Column(db.String)
    publish_year = db.Column(db.String(4))
    link = db.Column(db.String)
    cover_url = db.Column(db.String)
    isbn = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    category = db.relationship(Category)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'summary': self.summary,
            'publish_year': self.publish_year,
            'link': self.link,
            'cover_url': self.cover_url,
            'isbn': self.isbn
        }


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False, )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)    

    book = db.relationship(Book)
    
    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
        
        
