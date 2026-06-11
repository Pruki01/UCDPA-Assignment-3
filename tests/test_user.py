from flaskr.db import db, user

def test_user_creation():
    user = user.User('email@gmail.com',
                     'password123',
                     'John',
                     'Smith',
                     'New York City',
                     user.UserType.Visitor)

    assert user is not None
