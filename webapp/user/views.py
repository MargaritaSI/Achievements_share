from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.user.forms import LoginForm
from webapp.user.models import User


# name Blueprint, modul name, start of all urls
blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Authorization'
    login_form = LoginForm()  # create object of Class

    # takes a template, substitutes data there and passes it to the browser
    return render_template(
        'user/login.html',
        page_title=title,
        form=login_form
    )


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()  # create form object

    # if we haven't errors with checking form we ask/get user
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            # we are login user and remember it,
            # remember = user remembered (True/false)
            login_user(user, remember=form.remember_me.data)
            # create message for later show on pages
            # flash('You are successfully logged in!')
            # redirect user to the main page
            return redirect(url_for('news.index'))

    flash('Wrong user name or password')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    # flash('You are logged out.')
    return redirect(url_for('news.index'))
