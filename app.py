#!/usr/bin/env python3
from flask import Flask
from models import db, User, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///techBooks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def home():
    user1 = User(name='Acemad', email='ouessai.aes@gmail.com')
    db.session.add(user1)
    db.session.commit()
    return 'done'

if __name__ == '__main__':    
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
