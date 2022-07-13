from flask import Blueprint, flash, render_template, redirect, url_for #we import blueprint instead of @app
from flask_login import current_user, login_user, logout_user # login_user - handles login form

from webapp.user.forms import LoginForm
from webapp.user.models import User  # link model with flask

blueprint = Blueprint('user', __name__, url_prefix='/users') # name Blueprint, modul name, start of all urls

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Authorization'
    login_form = LoginForm()  # create object of Class
    return render_template('user/login.html', page_title=title, #user/ from templates
                           form=login_form)  # takes a template, substitutes data there and passes it to the browser


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()  # create form object

    if form.validate_on_submit():  # if we haven't errors with checking form we ask/get user
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):  # if user and password are existed
            login_user(user,
                       remember=form.remember_me.data)  # we are login user and remember it, remember = user remembered (True/false)
            flash('You successfully login!')  # create message for later show on pages
            return redirect(url_for('news.index'))  # redirect user to the main page

    flash('Wrong user name or password')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You are logout.')
    return redirect(url_for('news.index'))