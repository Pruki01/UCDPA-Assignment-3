import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import db, user 

bp = Blueprint('auth', __name__, url_prefix='/auth')
test_user = user.User(  'email@gmail.com',
                        'password123',
                        'John',
                        'Smith',
                        'New York City',
                        user.UserType.Visitor)

test_user2= user.User(  'email@fmail.com',
                        'password223',
                        'John',
                        'Smith',
                        'New York City',
                        user.UserType.Visitor)

db.add_user(test_user)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    print(request)
    if request.method == 'POST':

        email       = request.form['email']
        password    = db.generate_password_hash(request.form['password'])
        f_name      = request.form['first_name']
        l_name      = request.form['last_name']
        address     = request.form['address']
        user_type   = user.UserType.Visitor

        new_user = user.User(email, password, f_name, l_name, address, user_type)
        new_user.print_details()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))