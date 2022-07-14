#for creating users

from getpass import getpass # like input but without printing(for passwords)
import sys # for system function, sys.exit - for right finishing our script with errors(without 'return')

from webapp import create_app
# from webapp.db import db # here should be database
from webapp.user.models import User

app = create_app() # create app for work with database in local (with work in web app)

with app.app_context():
    username = input('Input User name: ')

    if User.query.filter(User.username == username).count(): # check if user exist
        print('User with this name already done')
        sys.exit(0) # exist from app

    password1 = getpass('Input password: ')
    password2 = getpass('Repeat password: ')

    if not password1 == password2:
        print(' passwords are different')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1) # encrypts

    #db.session.add(new_user)
    #db.session.commit()
    print('Created user with id={}'.format(new_user.id))
