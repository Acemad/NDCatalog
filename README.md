# ND Item Catalog Project : AWBooks
### For Full Stack Web Developer Nanodegree Program @ [Udacity](http://www.udacity.com)

![image](/static/logo.png)

This is my submission for Udacity's Item Catalog project. The project is called AWBooks. (AWesome Books)

## Description

AWBooks is a simple curated catalog of books related to computing and technology in general.
It's meant to include the best books in every category, so that visitors wishing to learn about a certain technology
will find an updated list of the most awesome books on the subject.

A user has the ability to add a book to any category after signing-in (through Google Accounts), he can then edit or delete the books he added. 

Supported categories include : Software Engineering, Programming, Web Development ... etc

## Project Structure

AWBooks' backend is written in Python 3 using Flask and a variety of extensions such as Flask-SQLAlchemy. The frontend uses Bootstrap 4.

The project files are structured as illustrated bellow :

```
- static/          # Contains all static files (svg, png, css)
- templates/       # Contains all the html templates
  - base.html      # Base template, parent to all remaining templates
  - book.html      # Displays book info
  - category.html  # Displays all books in a category
  - editBook.html  # Book editing form
  - error.html     # Displays error messages
  - home.html      # Homepage, lists all categogries
  - login.html     # Shows login options (currently, only Google is supported)
  - new.html       # Form for adding a new book
- app.py           # Main application file
- models.py        # Contains models definitions
- techbooks.db     # A sample database
- pipfile          # Used by pipenv to manage dependencies
- pipfile.lock     # Same as above
```


## Getting Started

This project uses pipenv for dependency management.
After cloning this repo, CD into it and run the following command :

```$ pipenv install```

Then type the following to launch the web app :

```$ python app.py```

To use AWBooks, open your web browser and visit : ```http://localhost:8000```

You should be greeted with a homepage listing all the categories available. You can sign-in and add your favorite books.