from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Book

app = Flask(__name__)
app.config.from_object(Config)
# Initialize the database with the app
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
# Route to display the list of books using the get method
@app.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all() # Route to display the list of books
    return render_template('books.html', books=books) # Render the books.html template with the list of books
# Route to add a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']
        new_book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('list_books'))
        # Render the add_book.html template for GET requests
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
