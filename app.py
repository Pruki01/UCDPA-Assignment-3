from flaskr import app
from flaskr.db import db, user, book
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

new_book = book.Book(
    'The Stranger',
    'Albert Camus',
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.wixstatic.com%2Fmedia%2Fd53163_c2870aa99b4b43e69e95d7760244d1ed~mv2.jpg%2Fv1%2Ffill%2Fw_980%2Ch_1307%2Cal_c%2Cq_85%2Cusm_0.66_1.00_0.01%2Cenc_avif%2Cquality_auto%2Fd53163_c2870aa99b4b43e69e95d7760244d1ed~mv2.jpg&f=1&nofb=1&ipt=ecae0ec63cdeaf90eb692731dedafed976d839d9dffb81e414314d524654ef44',
    'Fiction',
    'The Stranger also published in English as The Outsider, is a 1942 novella written by French author Albert Camus. The first of Camus\' novels published in his lifetime, the story follows Meursault, an indifferent settler in French Algeria, who, weeks after his mother\'s funeral, kills an unnamed Arab man in Algiers. The story is divided into two parts, presenting Meursault\'s first-person narrative before and after the killing.',
    100
)

db.add_book(new_book)

@app.route('/')
def index():
    return render_template('index.html', book_list=db.load_books())

@app.route('/<uuid:ISBN>')
def book_page(ISBN):
    book = db.load_book(ISBN)

    if book is None:
        return render_template('404.html')
    else:
        return render_template('book.html', book=book)

@app.route('/register', methods=['GET','POST'])
def register():

    if 'user_id' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email       = request.form['email']
        password    = generate_password_hash(request.form['password'])
        f_name      = request.form['first_name']
        l_name      = request.form['last_name']
        address     = request.form['address']

        db.add_user(user.User(
            email,
            password,
            f_name,
            l_name,
            address,
            user.UserType.Visitor
        ))
        return redirect(url_for('index'))

    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if 'user_id' in session:
        return redirect(url_for('index'))

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        error = None

        current_user = db.load_user(email)

        if current_user is None:
            error = "User does not exist!"
        elif not check_password_hash(current_user['Password'], password):
            error = "Incorrect Credentials!"
        else:
            session.clear()
            session['user_id']    = current_user['Id']
            session['user_email'] = current_user['Email']
            session['user_type']  = current_user['User Type']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register_staff', methods=['GET','POST'])
def register_staff():

    if request.method == 'POST':
        email       = request.form['email']
        password    = generate_password_hash(request.form['password'])
        f_name      = request.form['first_name']
        l_name      = request.form['last_name']
        address     = request.form['address']

        db.add_user(user.User(
            email,
            password,
            f_name,
            l_name,
            address,
            user.UserType.Staff
        ))

        return redirect(url_for('login'))
    return render_template('auth/staff_register.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title   = request.form['title']
        author  = request.form['author']
        image   = request.form['image']
        genre   = request.form['genre']
        desc    = request.form['description']

        new_book = book.Book(title, author, image, genre, desc, 0)

        if new_book:
            db.add_book(new_book)
            return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == "__main__":
    app.secret_key = "SECRET"
    app.run(debug=True, port=5000)